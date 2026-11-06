import unittest

from pathfinding_lab.grid import Ruudukko

class TestRuudukko(unittest.TestCase):

    def setUp(self):
        """Luo uuden ruudukon jokaista testiä varten."""
        self.ruudukko = Ruudukko(10, 10)

    def test_ruudukon_koko(self):
        """Tarkistaa ruudukon leveyden ja korkeuden."""
        self.assertEqual(self.ruudukko.leveys, 10)
        self.assertEqual(self.ruudukko.korkeus, 10)

    def test_esteen_lisaaminen(self):
        """Tarkistaa, että este tallentuu oikeaan sijaintiin."""
        self.ruudukko.lisaa_este(3, 4)

        self.assertTrue(self.ruudukko.on_este(3, 4))

    def test_esteeton_ruutu(self):
        """Tarkistaa, ettei tyhjää ruutua tunnisteta esteeksi."""
        self.assertFalse(self.ruudukko.on_este(2, 2))

    def test_ruudukon_sisalla_oleva_ruutu(self):
        """Tarkistaa ruudukon sisällä olevan koordinaatin."""
        self.assertTrue(self.ruudukko.on_ruudukossa(5, 5))

    def test_ruudukon_ulkopuolinen_ruutu(self):
        """Tarkistaa ruudukon ulkopuolisen koordinaatin."""
        self.assertFalse(self.ruudukko.on_ruudukossa(10, 5))

    def test_esteeton_ruutu_on_kuljettavissa(self):
        """Tarkistaa, että esteettömään ruutuun voi kulkea."""
        self.assertTrue(self.ruudukko.on_kuljettavissa(2, 2))

    def test_esteellinen_ruutu_ei_ole_kuljettavissa(self):
        """Tarkistaa, ettei esteelliseen ruutuun voi kulkea."""
        self.ruudukko.lisaa_este(3, 4)

        self.assertFalse(self.ruudukko.on_kuljettavissa(3, 4))

    def test_esteen_lisaaminen_ruudukon_ulkopuolelle(self):
        """Tarkistaa, että virheellinen esteen sijainti aiheuttaa virheen."""
        with self.assertRaises(ValueError):
            self.ruudukko.lisaa_este(10, 10)

    def test_naapuriruutujen_hakeminen(self):
        """Tarkistaa, että ruudun neljä naapuria löydetään."""
        naapurit = self.ruudukko.hae_naapurit(5, 5)

        odotetut = [
            (5, 4),
            (6, 5),
            (5, 6),
            (4, 5)
        ]

        self.assertEqual(naapurit, odotetut)

    def test_esteellisten_naapurien_poistaminen(self):
        """Tarkistaa, ettei esteellisiä ruutuja palauteta naapureina."""
        self.ruudukko.lisaa_este(5, 4)

        naapurit = self.ruudukko.hae_naapurit(5, 5)

        self.assertNotIn((5, 4), naapurit)
        self.assertEqual(len(naapurit), 3)

    def test_ruudukon_reunalla_olevat_naapurit(self):
        """Tarkistaa, ettei ruudukon ulkopuolisia ruutuja palauteta."""
        naapurit = self.ruudukko.hae_naapurit(0, 0)

        odotetut = [
            (1, 0),
            (0, 1)
        ]

        self.assertEqual(naapurit, odotetut)


if __name__ == "__main__":
    unittest.main()
