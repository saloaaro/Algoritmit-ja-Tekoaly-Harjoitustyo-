"""Toteuttaa A*-reitinhakualgoritmin."""

import heapq
import time

class AStar:
    """Toteuttaa A*-reitinhakualgoritmin."""

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

    def hae_reitti(self, lahto, maali):
        """Etsii lyhimmän reitin lähtöpisteestä maaliin A*-algoritmilla."""

        self.tutkitut_ruudut = []
        self.suoritusaika = 0.0

        if not self.ruudukko.on_kuljettavissa(*lahto):
            raise ValueError("Lähtöpiste ei ole kuljettavissa.")

        if not self.ruudukko.on_kuljettavissa(*maali):
            raise ValueError("Maalipiste ei ole kuljettavissa.")

        alkuaika = time.perf_counter()

        avoimet = []
        heapq.heappush(
            avoimet,
            (self.heuristiikka(lahto, maali), 0, lahto)
        )

        edeltajat = {}
        kustannukset = {lahto: 0}
        tutkitut = set()

        while avoimet:
            _, kustannus, nykyinen = heapq.heappop(avoimet)

            if nykyinen in tutkitut:
                continue

            tutkitut.add(nykyinen)
            self.tutkitut_ruudut.append(nykyinen)

            if nykyinen == maali:
                self.suoritusaika = time.perf_counter() - alkuaika
                return self.muodosta_reitti(edeltajat, nykyinen)

            for naapuri in self.ruudukko.hae_naapurit(*nykyinen):
                uusi_kustannus = kustannus + 1

                if uusi_kustannus < kustannukset.get(naapuri, float("inf")):
                    kustannukset[naapuri] = uusi_kustannus
                    edeltajat[naapuri] = nykyinen

                    arvio = uusi_kustannus + self.heuristiikka(
                        naapuri, maali
                    )

                    heapq.heappush(
                        avoimet,
                        (arvio, uusi_kustannus, naapuri)
                    )

        self.suoritusaika = time.perf_counter() - alkuaika
        return None

    def muodosta_reitti(self, edeltajat, nykyinen):
        """Muodostaa reitin kulkemalla edeltäjiä taaksepäin."""

        reitti = [nykyinen]

        while nykyinen in edeltajat:
            nykyinen = edeltajat[nykyinen]
            reitti.append(nykyinen)

        reitti.reverse()

        return reitti
