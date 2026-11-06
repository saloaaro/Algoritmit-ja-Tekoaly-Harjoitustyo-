import unittest

from pathfinding_lab.grid import Ruudukko
from pathfinding_lab.fringe_search import FringeSearch

class TestFringeSearch(unittest.TestCase):

    def setUp(self):
        """Luo uuden ruudukon ja Fringe Search -algoritmin jokaista testiä varten."""
        self.ruudukko = Ruudukko(5, 5)
        self.algoritmi = FringeSearch(self.ruudukko)

    def test_heuristiikka(self):
        """Tarkistaa Manhattan-etäisyyden laskemisen."""
        etaisyys = self.algoritmi.heuristiikka((1, 1), (4, 3))

        self.assertEqual(etaisyys, 5)

    def test_reitin_loytaminen(self):
        """Tarkistaa, että algoritmi löytää reitin lähtöpisteestä maaliin."""
        reitti = self.algoritmi.hae_reitti((0, 0), (4, 4))

        self.assertIsNotNone(reitti)
        self.assertEqual(reitti[0], (0, 0))
        self.assertEqual(reitti[-1], (4, 4))
        self.assertEqual(len(reitti), 9)

    def test_reitin_loytaminen_esteen_ympari(self):
        """Tarkistaa, että algoritmi osaa kiertää esteen."""
        self.ruudukko.lisaa_este(1, 0)

        reitti = self.algoritmi.hae_reitti((0, 0), (2, 0))

        self.assertIsNotNone(reitti)
        self.assertNotIn((1, 0), reitti)
        self.assertEqual(reitti[0], (0, 0))
        self.assertEqual(reitti[-1], (2, 0))

    def test_reitin_loytaminen_epaonnistuu(self):
        """Tarkistaa, että algoritmi palauttaa None, jos reittiä ei ole."""
        for y in range(5):
            self.ruudukko.lisaa_este(2, y)

        reitti = self.algoritmi.hae_reitti((0, 0), (4, 0))

        self.assertIsNone(reitti)

    def test_lahtopiste_esteessa(self):
        """Tarkistaa, ettei esteestä voi aloittaa reitinhakua."""
        self.ruudukko.lisaa_este(0, 0)

        with self.assertRaises(ValueError):
            self.algoritmi.hae_reitti((0, 0), (4, 4))

    def test_maalipiste_esteessa(self):
        """Tarkistaa, ettei esteeseen voi päättää reittiä."""
        self.ruudukko.lisaa_este(4, 4)

        with self.assertRaises(ValueError):
            self.algoritmi.hae_reitti((0, 0), (4, 4))

    def test_lahtopiste_on_sama_kuin_maali(self):
        """Tarkistaa, että sama lähtö- ja maalipiste palauttaa yhden ruudun."""
        reitti = self.algoritmi.hae_reitti((2, 2), (2, 2))

        self.assertEqual(reitti, [(2, 2)])

    def test_lyhimman_reitin_loytaminen_useilla_esteilla(self):
        """Tarkistaa lyhimmän reitin löytämisen useiden esteiden ympäriltä."""

        for y in range(4):
            self.ruudukko.lisaa_este(2, y)

        reitti = self.algoritmi.hae_reitti((0, 0), (4, 0))

        self.assertIsNotNone(reitti)
        self.assertEqual(reitti[0], (0, 0))
        self.assertEqual(reitti[-1], (4, 0))

        # Lyhin reitti kiertää esteen alapuolelta.
        self.assertEqual(len(reitti), 13)

        # Jokaisen peräkkäisen ruudun välillä pitää olla yksi askel.
        for i in range(len(reitti) - 1):
            nykyinen = reitti[i]
            seuraava = reitti[i + 1]

            etaisyys = (
                abs(nykyinen[0] - seuraava[0])
                + abs(nykyinen[1] - seuraava[1])
            )

            self.assertEqual(etaisyys, 1)

        # Reitti ei saa kulkea esteiden kautta.
        for ruutu in reitti:
            self.assertFalse(self.ruudukko.on_este(*ruutu))

    def test_tutkittujen_ruutujen_tallentaminen(self):
        """Tarkistaa, että algoritmi tallentaa tutkimansa ruudut."""

        self.algoritmi.hae_reitti((0, 0), (4, 4))

        self.assertGreater(len(self.algoritmi.tutkitut_ruudut), 0)
        self.assertIn((0, 0), self.algoritmi.tutkitut_ruudut)
        self.assertIn((4, 4), self.algoritmi.tutkitut_ruudut)

if __name__ == "__main__":
    unittest.main()
