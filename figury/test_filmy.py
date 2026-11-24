#!/usr/bin/env python3
"""Testy renderera filmow percepcji na malej syntetycznej siatce (bez swiata, logow i ffmpeg).

Uruchomienie:  cd figury && python3 -m unittest test_filmy -v
"""
import math
import tempfile
import unittest
from pathlib import Path

import filmy as M


def siatka(bloki, znane=None):
    """bloki: dict (x,y,z) -> nazwa; poza bloki: powietrze w znanym pudle, NIEZNANE poza nim."""
    znane = znane or (-10, -2, -10, 10, 8, 10)

    def blok(x, y, z):
        if (x, y, z) in bloki:
            return bloki[(x, y, z)]
        x0, y0, z0, x1, y1, z1 = znane
        if x0 <= x <= x1 and y0 <= y <= y1 and z0 <= z <= z1:
            return "stone" if y < 0 else "air"
        return M.NIEZNANE
    return blok


class TestPromien(unittest.TestCase):
    def test_sciana_na_wprost(self):
        # blok w z = -5 zajmuje z od -5 do -4; oko w z = 0,5: promien na N trafia w sciane z = -4 po 4,5 m (sciana typu z = 2)
        b = siatka({(0, 1, -5): "stone"})
        r = M.promien_dda(0.5, 1.5, 0.5, 0.0, 0.0, -1.0, b)
        self.assertIsNotNone(r)
        self.assertAlmostEqual(r[0], 4.5, places=6)
        self.assertEqual(r[1], 2)
        self.assertEqual(r[2], "stone")

    def test_nieznane_to_mgla(self):
        b = siatka({}, znane=(-3, -2, -3, 3, 8, 3))
        r = M.promien_dda(0.5, 1.5, 0.5, 1.0, 0.0, 0.0, b)
        self.assertEqual(r[2], M.NIEZNANE)
        self.assertAlmostEqual(r[0], 3.5, places=6)

    def test_poza_zasiegiem(self):
        b = siatka({}, znane=(-50, -2, -50, 50, 8, 50))
        self.assertIsNone(M.promien_dda(0.5, 1.5, 0.5, 1.0, 0.0, 0.0, b, maxd=20))

    def test_rosliny_przezroczyste(self):
        b = siatka({(2, 1, 0): "short_grass", (4, 1, 0): "oak_log"})
        r = M.promien_dda(0.5, 1.5, 0.5, 1.0, 0.0, 0.0, b)
        self.assertEqual(r[2], "oak_log")


class TestOczy(unittest.TestCase):
    def test_obraz_i_glebia(self):
        b = siatka({(x, y, -4): "stone" for x in range(-6, 7) for y in range(0, 5)})
        img, gl = M.render_oczu(b, (0.5, 1.62, 0.5), 0, 0, res=(32, 18))
        self.assertEqual(img.size, (32, 18))
        srodek = gl[9 * 32 + 16]
        self.assertAlmostEqual(srodek, 3.5, delta=0.2)   # sciana z = -3 (blok z = -4)
        # na srodku kolor sciany (szary, cieniowanie z), nie mgla
        self.assertNotEqual(img.getpixel((16, 9)), M.MGLA)

    def test_mgla_dla_nieznanego(self):
        b = siatka({}, znane=(-1, -2, -1, 1, 8, 1))
        img, _ = M.render_oczu(b, (0.5, 1.62, 0.5), 90, 0, res=(16, 9))
        self.assertIn(img.getpixel((8, 4)), (M.MGLA, (40, 46, 58)))

    def test_rzut_punktu_przed_i_za(self):
        oko = (0.5, 1.62, 0.5)
        p = M.rzut_punktu(oko, 0, 0, (0.5, 1.62, -9.5), res=(160, 90))
        self.assertAlmostEqual(p[0], 80, delta=0.5)
        self.assertAlmostEqual(p[1], 45, delta=0.5)
        self.assertIsNone(M.rzut_punktu(oko, 0, 0, (0.5, 1.62, 9.5)))

    def test_kierunek_wzroku_kompas(self):
        fwd, prawo, _ = M.kierunek_wzroku(90, 0)   # E: x rosnie
        self.assertAlmostEqual(fwd[0], 1, places=6)
        self.assertAlmostEqual(prawo[2], 1, places=6)   # prawa reka patrzacego na E to S (z rosnie)


class TestIzo(unittest.TestCase):
    def test_widoczne_sciany_od_sw(self):
        b = siatka({(0, 0, 0): "stone"}, znane=(-2, 0, -2, 2, 3, 2))
        sc, mg = M.sciany_izo(b, (0.5, 1.0, 0.5), 2, 0, 2, 0.0)
        # pojedynczy szescian: gora, sciana W (-x) i S (+z) jak w figury.rzut_izo
        self.assertEqual(len(sc), 3)
        self.assertEqual(mg, [])

    def test_obrot_180_zmienia_sciany(self):
        b = siatka({(0, 0, 0): "stone"}, znane=(-2, 0, -2, 2, 3, 2))
        P0, _, w0 = M.projekcja_izo(0, 10, 0, 0, (0.5, 1.0, 0.5))
        P1, _, w1 = M.projekcja_izo(180, 10, 0, 0, (0.5, 1.0, 0.5))
        self.assertTrue(w0((-1, 0, 0)) and not w0((1, 0, 0)))
        self.assertTrue(w1((1, 0, 0)) and not w1((-1, 0, 0)))

    def test_kolumny_nieznane_jako_mgla(self):
        b = siatka({}, znane=(0, 0, 0, 0, 3, 0))
        _, mg = M.sciany_izo(b, (0.5, 1.0, 0.5), 1, 0, 2, 0.0)
        self.assertIn((1, 0), mg)
        self.assertNotIn((0, 0), mg)


class TestRadar(unittest.TestCase):
    def test_typy_promieni(self):
        bl = {(3, 1, 0): "stone", (3, 2, 0): "stone",              # E: przeszkoda w 3 m
              (0, 1, -2): "oak_door", (0, 2, -2): "oak_door"}       # N: drzwi w 2 m
        for x in range(-4, -1):                                       # W: dziura (spadek) od 2 m
            for y in (-1, -2, 0):
                bl[(x, y, 0)] = "air"
        b = siatka(bl)
        r = {k: (t, d) for k, t, d in M.radar(b, (0.5, 1.0, 0.5), zas=6, n=4)}
        self.assertEqual(r[0][0], "drzwi")
        self.assertEqual(r[90][0], "przeszkoda")
        self.assertEqual(r[180][0], "wolne")
        self.assertEqual(r[270][0], "spadek")
        self.assertLessEqual(r[90][1], 3)


class TestWiedza(unittest.TestCase):
    def test_pamiec_i_kopia(self):
        pam = {(0, 0, 0): ("log", 100), (1, 0, 0): ("air", 500)}
        w = M.Wiedza(pam, lambda x, y, z: "oak_log", {(1, 0): 200, (5, 5): 50}, 1000)
        self.assertEqual(w.blok(0, 0, 0, 150), "log")            # widziany przed t: z pamieci
        self.assertEqual(w.blok(0, 0, 0, 50), M.NIEZNANE)         # jeszcze nie widziany, kolumna bez sladu
        self.assertEqual(w.blok(1, 0, 0, 300), "oak_log")        # ostatnio widziany pozniej, kolumna w zasiegu od 200: kopia
        self.assertEqual(w.blok(1, 0, 0, 600), "air")            # po widzeniu: pamiec (np. sciete drzewo)
        self.assertEqual(w.blok(5, 0, 5, 900), M.NIEZNANE)        # brak w pamieci przed koncem zapisu
        self.assertEqual(w.blok(5, 0, 5, 1100), "oak_log")       # po zapisie pamieci: rekonstrukcja ze sladu

    def test_czytaj_pamiec_tokeny(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "mapa.txt"
            p.write_text("AGENT-MOST-MAPA v1\nP 1 air\nP 2 chest\nS 0 0 0\n1:10*3 2:20 0:0*4092\n", encoding="utf-8")
            pam, mx = M.czytaj_pamiec(p)
        self.assertEqual(pam[(3, 0, 0)], ("chest", 20))
        self.assertEqual(pam[(0, 0, 0)], ("air", 10))
        self.assertNotIn((4, 0, 0), pam)
        self.assertEqual(mx, 20)

    def test_pierwsze_widzenie(self):
        pw = M.pierwsze_widzenie([(10, 0.0, 0.0), (20, 30.0, 0.0)], promien=5)
        self.assertEqual(pw[(0, 0)], 10)
        self.assertEqual(pw[(30, 0)], 20)
        self.assertNotIn((15, 0), pw)


class TestDane(unittest.TestCase):
    def test_ekwipunek_i_przyrosty(self):
        self.assertEqual(M.parsuj_ekw("bread x1, wooden_axe x1"), {"bread": 1, "wooden_axe": 1})
        self.assertEqual(M.parsuj_ekw("ekwipunek pusty"), {})
        d = M.przyrost_ekw("kupiono x2 oferty #1: dostales emerald x2, ostatnia cena 1 leather, zostalo 9")
        self.assertEqual(d, {"emerald": 2, "leather": -2})
        d = M.przyrost_ekw("zabito polowanie: cow zabity, ciosy 2 ; przejeto: leather x2, beef x2")
        self.assertEqual(d, {"leather": 2, "beef": 2})
        self.assertEqual(M.przyrost_ekw("birch_planks x8 (crafty: birch_planks x8), w ekwipunku 8"), {"birch_planks": 8})

    def test_wzgl_po_polsku(self):
        self.assertEqual(M.wzgl_txt((0.5, 64, 0.5), -9, 64, 8), "12 m SW")
        self.assertEqual(M.wzgl_txt((0.5, 64, 0.5), 0, 67, -5), "5 m N, +3 w górę")

    def test_drzewo_wymaga_lisci(self):
        belka = siatka({(2, 1, 0): "oak_log"})
        self.assertIsNone(M.najblizsze_drzewo(belka, (0.5, 1.0, 0.5), r=4))
        las = siatka({(2, 1, 0): "oak_log", (2, 4, 0): "oak_leaves"})
        self.assertEqual(M.najblizsze_drzewo(las, (0.5, 1.0, 0.5), r=4)[1:4], (2, 1, 0))


if __name__ == "__main__":
    unittest.main()
