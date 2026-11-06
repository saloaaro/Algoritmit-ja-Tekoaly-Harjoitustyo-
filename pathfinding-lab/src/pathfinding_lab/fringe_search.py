"""Toteuttaa Fringe Search -reitinhakualgoritmin."""

import time

class FringeSearch:
    """Toteuttaa Fringe Search -reitinhakualgoritmin."""

    def __init__(self, ruudukko):
        self.ruudukko = ruudukko
        self.tutkitut_ruudut = []
        self.suoritusaika = 0.0

    def heuristiikka(self, nykyinen, maali):
        """Laskee Manhattan-etäisyyden nykyisestä ruudusta maaliin."""
        return (
            abs(nykyinen[0] - maali[0])
            + abs(nykyinen[1] - maali[1])
        )

    def muodosta_reitti(self, edeltajat, nykyinen):
        """Muodostaa reitin kulkemalla edeltäjiä taaksepäin."""

        reitti = [nykyinen]

        while nykyinen in edeltajat:
            nykyinen = edeltajat[nykyinen]
            reitti.append(nykyinen)

        reitti.reverse()

        return reitti

    def hae_reitti(self, lahto, maali):
        """Etsii reitin lähtöpisteestä maaliin Fringe Search -algoritmilla."""

        self.tutkitut_ruudut = []
        self.suoritusaika = 0.0

        if not self.ruudukko.on_kuljettavissa(*lahto):
            raise ValueError("Lähtöpiste ei ole kuljettavissa.")

        if not self.ruudukko.on_kuljettavissa(*maali):
            raise ValueError("Maalipiste ei ole kuljettavissa.")

        alkuaika = time.perf_counter()

        edeltajat = {}
        kustannukset = {lahto: 0}

        raja = self.heuristiikka(lahto, maali)
        nykyinen_jono = [lahto]

        while nykyinen_jono:
            seuraava_raja = float("inf")
            seuraava_jono = []

            while nykyinen_jono:
                nykyinen = nykyinen_jono.pop(0)
                self.tutkitut_ruudut.append(nykyinen)

                kustannus = kustannukset[nykyinen]
                arvio = kustannus + self.heuristiikka(nykyinen, maali)

                if arvio > raja:
                    seuraava_raja = min(seuraava_raja, arvio)
                    seuraava_jono.append(nykyinen)
                    continue

                if nykyinen == maali:
                    self.suoritusaika = time.perf_counter() - alkuaika
                    return self.muodosta_reitti(edeltajat, nykyinen)

                for naapuri in self.ruudukko.hae_naapurit(*nykyinen):
                    uusi_kustannus = kustannus + 1

                    if uusi_kustannus < kustannukset.get(
                        naapuri, float("inf")
                    ):
                        kustannukset[naapuri] = uusi_kustannus
                        edeltajat[naapuri] = nykyinen

                        arvio = uusi_kustannus + self.heuristiikka(
                            naapuri, maali
                        )

                        if arvio <= raja:
                            nykyinen_jono.append(naapuri)
                        else:
                            seuraava_raja = min(seuraava_raja, arvio)
                            seuraava_jono.append(naapuri)

            if not seuraava_jono:
                self.suoritusaika = time.perf_counter() - alkuaika
                return None

            raja = seuraava_raja
            nykyinen_jono = list(dict.fromkeys(seuraava_jono))

        self.suoritusaika = time.perf_counter() - alkuaika
        return None
