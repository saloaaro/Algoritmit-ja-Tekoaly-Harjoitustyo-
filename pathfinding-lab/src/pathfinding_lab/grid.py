"""Kuvaa reitinhakuun käytettävää kaksiulotteista ruudukkoa."""

class Ruudukko:
    """Kuvaa reitinhakuun käytettävää kaksiulotteista ruudukkoa."""
    def __init__(self, leveys, korkeus):
        self.leveys = leveys
        self.korkeus = korkeus
        self.esteet = set()

    def lisaa_este(self, x, y):
        """Lisää esteen annettuun koordinaattiin."""
        if not self.on_ruudukossa(x, y):
            raise ValueError("Esteen sijainti on ruudukon ulkopuolella.")

        self.esteet.add((x, y))

    def on_este(self, x, y):
        """Tarkistaa, onko annetussa koordinaatissa este."""
        return (x, y) in self.esteet

    def on_ruudukossa(self, x, y):
        """Tarkistaa, sijaitseeko koordinaatti ruudukon rajojen sisällä."""
        return 0 <= x < self.leveys and 0 <= y < self.korkeus

    def on_kuljettavissa(self, x, y):
        """Tarkistaa, voiko ruutuun kulkea."""
        return self.on_ruudukossa(x, y) and not self.on_este(x, y)

    def hae_naapurit(self, x, y):
        """Palauttaa annetun ruudun kuljettavissa olevat naapuriruudut."""
        suunnat = [
            (0, -1),  # Ylös
            (1, 0),   # Oikealle
            (0, 1),   # Alas
            (-1, 0)   # Vasemmalle
        ]

        naapurit = []

        for dx, dy in suunnat:
            uusi_x = x + dx
            uusi_y = y + dy

            if self.on_kuljettavissa(uusi_x, uusi_y):
                naapurit.append((uusi_x, uusi_y))

        return naapurit
