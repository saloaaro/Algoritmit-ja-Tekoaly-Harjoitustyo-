
"""Pygame-käyttöliittymä reitinhakualgoritmien visualisointiin."""

from statistics import mean

import pygame

from .astar import AStar
from .fringe_search import FringeSearch
from .grid import Ruudukko


# Ikkunan asetukset
IKKUNAN_LEVEYS = 1300
IKKUNAN_KORKEUS = 850

# Ruudukon sijainti
RUUDUKON_X = 20
RUUDUKON_Y = 80

# Ruudukon enimmäiskoko
MAKSIMI_RUUDUKON_LEVEYS = 840
MAKSIMI_RUUDUKON_KORKEUS = 740

# Algoritmien vertailuasetukset
VERTAILU_TOISTOT = 30

# Karttakoot
KARTTAKOOT = {
    pygame.K_F1: (30, 20),
    pygame.K_F2: (50, 50),
    pygame.K_F3: (100, 100),
}

# Värit
TAUSTA = (245, 247, 250)
VALKOINEN = (255, 255, 255)
MUSTA = (30, 30, 30)
HARMAA = (190, 195, 200)
PANEELIN_REUNA = (220, 224, 230)
ESTEEN_VARI = (55, 55, 65)
LAHDON_VARI = (50, 180, 90)
MAALIN_VARI = (220, 65, 65)
TUTKITUN_VARI = (150, 205, 245)
REITIN_VARI = (255, 205, 65)


def piirra_teksti(ikkuna, fontti, teksti, x, y, vari=MUSTA):
    """Piirtää tekstin annettuun sijaintiin."""
    pinta = fontti.render(teksti, True, vari)
    ikkuna.blit(pinta, (x, y))


def laske_ruudun_koko(leveys, korkeus):
    """Laskee kartalle sopivan yksittäisen ruudun koon."""
    leveydelle_sopiva = MAKSIMI_RUUDUKON_LEVEYS // leveys
    korkeudelle_sopiva = MAKSIMI_RUUDUKON_KORKEUS // korkeus

    return max(1, min(25, leveydelle_sopiva, korkeudelle_sopiva))


def piirra_ruudukko(
    ikkuna,
    ruudukko,
    lahto,
    maali,
    tutkitut,
    reitti,
    ruudun_koko
):
    """Piirtää ruudukon ja sen sisältämät reitinhaun tiedot."""
    for y in range(ruudukko.korkeus):
        for x in range(ruudukko.leveys):
            koordinaatti = (x, y)
            vari = VALKOINEN

            if ruudukko.on_este(x, y):
                vari = ESTEEN_VARI
            elif koordinaatti in tutkitut:
                vari = TUTKITUN_VARI

            if reitti and koordinaatti in reitti:
                vari = REITIN_VARI

            if koordinaatti == lahto:
                vari = LAHDON_VARI
            elif koordinaatti == maali:
                vari = MAALIN_VARI

            ruutu = pygame.Rect(
                RUUDUKON_X + x * ruudun_koko,
                RUUDUKON_Y + y * ruudun_koko,
                ruudun_koko,
                ruudun_koko
            )

            pygame.draw.rect(ikkuna, vari, ruutu)

            if ruudun_koko >= 6:
                pygame.draw.rect(ikkuna, HARMAA, ruutu, 1)


def suorita_vertailu(ruudukko, lahto, maali):
    """Vertaa algoritmeja vuorottelevilla mittausajoilla."""
    algoritmit = {
        "A*": AStar,
        "Fringe Search": FringeSearch
    }

    ajat = {
        "A*": [],
        "Fringe Search": []
    }

    viimeiset_reitit = {
        "A*": None,
        "Fringe Search": None
    }

    viimeiset_tutkitut = {
        "A*": [],
        "Fringe Search": []
    }

    # Molemmille algoritmeille yksi lämmittelyajo.
    for algoritmiluokka in algoritmit.values():
        algoritmi = algoritmiluokka(ruudukko)
        algoritmi.hae_reitti(lahto, maali)

    # Algoritmien mittausjärjestys vuorottelee. (tekemättä).
    for _ in range(VERTAILU_TOISTOT):
        for nimi, algoritmiluokka in algoritmit.items():
            algoritmi = algoritmiluokka(ruudukko)
            reitti = algoritmi.hae_reitti(lahto, maali)

            ajat[nimi].append(algoritmi.suoritusaika * 1000)
            viimeiset_reitit[nimi] = reitti

            viimeiset_tutkitut[nimi] = list(
                dict.fromkeys(algoritmi.tutkitut_ruudut)
            )

    tulokset = {}

    for nimi in algoritmit:
        reitti = viimeiset_reitit[nimi]
        tutkitut = viimeiset_tutkitut[nimi]

        tulokset[nimi] = {
            "keskiarvo": mean(ajat[nimi]),
            "min": min(ajat[nimi]),
            "max": max(ajat[nimi]),
            "reitti": reitti,
            "reitin_pituus": len(reitti) - 1 if reitti else None,
            "tutkitut": len(tutkitut),
            "hakujarjestys": tutkitut
        }

    return tulokset


class PathfindingSovellus:
    """Hallinnoi reitinhakualgoritmien käyttöliittymää."""

    def __init__(self):
        pygame.init()

        self.ikkuna = pygame.display.set_mode(
            (IKKUNAN_LEVEYS, IKKUNAN_KORKEUS)
        )
        pygame.display.set_caption("Pathfinding Lab - Reitinhaku")

        # Fontit
        self.otsikko_fontti = pygame.font.SysFont(None, 27)
        self.fontti = pygame.font.SysFont(None, 23)
        self.pieni_fontti = pygame.font.SysFont(None, 19)

        self.kello = pygame.time.Clock()

        # Ruudukon asetukset
        self.ruudukon_leveys = 30
        self.ruudukon_korkeus = 20

        self.ruudukko = Ruudukko(
            self.ruudukon_leveys,
            self.ruudukon_korkeus
        )

        self.ruudun_koko = laske_ruudun_koko(
            self.ruudukon_leveys,
            self.ruudukon_korkeus
        )

        self.lahto = (1, 1)
        self.maali = (
            self.ruudukon_leveys - 2,
            self.ruudukon_korkeus - 2
        )

        # Käyttöliittymän valinnat
        self.valittu_algoritmi = "A*"
        self.toimintatila = "este"

        # Reitinhaun tulokset
        self.tutkitut = set()
        self.reitti = None
        self.vertailutulokset = None

        # Animaation tiedot
        self.animaation_ruudut = []
        self.animaation_indeksi = 0
        self.seuraava_animaatio = 0
        self.animaatio_valmis = True
        self.animaation_askel = 1

        self.tulosviesti = (
            "Valitse pisteet ja kaynnista reitinhaku."
        )

        self.kaynnissa = True

    def suorita(self):
        """Käynnistää käyttöliittymän pääsilmukan."""
        while self.kaynnissa:
            self.kasittele_tapahtumat()
            self.paivita_animaatio()
            self.piirra()
            self.kello.tick(60)

        pygame.quit()

    def kasittele_tapahtumat(self):
        """Käsittelee käyttöliittymän tapahtumat."""
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                self.kaynnissa = False

            elif tapahtuma.type == pygame.KEYDOWN:
                self.kasittele_nappain(tapahtuma.key)

            elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                self.kasittele_hiiri(tapahtuma)

    def kasittele_nappain(self, nappain):
        """Käsittelee näppäimistön painallukset."""
        if nappain == pygame.K_ESCAPE:
            self.kaynnissa = False

        elif nappain == pygame.K_s:
            self.toimintatila = "lahto"

        elif nappain == pygame.K_g:
            self.toimintatila = "maali"

        elif nappain == pygame.K_e:
            self.toimintatila = "este"

        elif nappain == pygame.K_1:
            self.valittu_algoritmi = "A*"

        elif nappain == pygame.K_2:
            self.valittu_algoritmi = "Fringe Search"

        elif nappain in KARTTAKOOT:
            self.vaihda_kartta(KARTTAKOOT[nappain])

        elif nappain == pygame.K_c:
            self.tyhjenna_esteet()

        elif nappain == pygame.K_r:
            self.suorita_haku()

        elif nappain == pygame.K_v:
            self.vertaa_algoritmit()

    def kasittele_hiiri(self, tapahtuma):
        """Käsittelee ruudukkoon kohdistuvat hiiritapahtumat."""
        hiiri_x, hiiri_y = tapahtuma.pos

        ruudukon_oikea = (
            RUUDUKON_X + self.ruudukon_leveys * self.ruudun_koko
        )
        ruudukon_ala = (
            RUUDUKON_Y + self.ruudukon_korkeus * self.ruudun_koko
        )

        if not (
            RUUDUKON_X <= hiiri_x < ruudukon_oikea
            and RUUDUKON_Y <= hiiri_y < ruudukon_ala
        ):
            return

        x = (hiiri_x - RUUDUKON_X) // self.ruudun_koko
        y = (hiiri_y - RUUDUKON_Y) // self.ruudun_koko
        koordinaatti = (x, y)

        if tapahtuma.button == 3:
            self.ruudukko.esteet.discard(koordinaatti)

        elif tapahtuma.button == 1:
            self.muokkaa_ruutua(x, y, koordinaatti)

        self.tyhjenna_hakutulokset()
        self.tulosviesti = (
            "Kartta muuttui. Suorita haku uudelleen."
        )

    def muokkaa_ruutua(self, x, y, koordinaatti):
        """Asettaa lähtö- tai maalipisteen tai muokkaa estettä."""
        if self.toimintatila == "lahto":
            self.lahto = koordinaatti
            self.ruudukko.esteet.discard(koordinaatti)

        elif self.toimintatila == "maali":
            self.maali = koordinaatti
            self.ruudukko.esteet.discard(koordinaatti)

        elif self.toimintatila == "este":
            if koordinaatti in self.ruudukko.esteet:
                self.ruudukko.esteet.remove(koordinaatti)

            elif koordinaatti not in (self.lahto, self.maali):
                self.ruudukko.lisaa_este(x, y)

    def vaihda_kartta(self, koko):
        """Luo uuden ruudukon valitulla koolla."""
        self.ruudukon_leveys, self.ruudukon_korkeus = koko

        self.ruudukko = Ruudukko(
            self.ruudukon_leveys,
            self.ruudukon_korkeus
        )

        self.ruudun_koko = laske_ruudun_koko(
            self.ruudukon_leveys,
            self.ruudukon_korkeus
        )

        self.lahto = (1, 1)
        self.maali = (
            self.ruudukon_leveys - 2,
            self.ruudukon_korkeus - 2
        )

        self.tyhjenna_hakutulokset()
        self.tulosviesti = "Karttakoko vaihdettu."

    def tyhjenna_hakutulokset(self):
        """Tyhjentää edellisen haun tulokset ja animaation."""
        self.tutkitut.clear()
        self.animaation_ruudut = []
        self.animaation_indeksi = 0
        self.animaatio_valmis = True
        self.reitti = None
        self.vertailutulokset = None

    def tyhjenna_esteet(self):
        """Poistaa kaikki esteet ruudukosta."""
        self.ruudukko.esteet.clear()
        self.tyhjenna_hakutulokset()
        self.tulosviesti = "Esteet ja hakutulokset tyhjennetty."

    def suorita_haku(self):
        """Suorittaa valitun reitinhakualgoritmin."""
        if self.valittu_algoritmi == "A*":
            algoritmi = AStar(self.ruudukko)
        else:
            algoritmi = FringeSearch(self.ruudukko)

        self.reitti = algoritmi.hae_reitti(
            self.lahto,
            self.maali
        )

        self.valmistele_animaatio(algoritmi.tutkitut_ruudut)
        self.vertailutulokset = None

        if self.reitti:
            self.tulosviesti = "Reitti löytyi!"
        else:
            self.tulosviesti = "Reittiä ei löytynyt."

    def vertaa_algoritmit(self):
        """Suorittaa algoritmien vertailun samalla ruudukolla."""
        self.vertailutulokset = suorita_vertailu(
            self.ruudukko,
            self.lahto,
            self.maali
        )

        tulokset = self.vertailutulokset[self.valittu_algoritmi]

        self.reitti = tulokset["reitti"]
        self.valmistele_animaatio(tulokset["hakujarjestys"])

        if self.reitti:
            self.tulosviesti = "Vertailu valmis: reitti löytyi."
        else:
            self.tulosviesti = "Vertailu valmis: reittiä ei löytynyt."

    def valmistele_animaatio(self, hakujarjestys):
        """Alustaa tutkittujen ruutujen animaation."""
        self.animaation_ruudut = list(hakujarjestys)
        self.tutkitut.clear()
        self.animaation_indeksi = 0
        self.seuraava_animaatio = pygame.time.get_ticks()

        self.animaation_askel = max(
            1,
            len(self.animaation_ruudut) // 180
        )

        self.animaatio_valmis = not self.animaation_ruudut

    def paivita_animaatio(self):
        """Päivittää tutkittujen ruutujen animaatiota."""
        nykyinen_aika = pygame.time.get_ticks()

        if (
            self.animaatio_valmis
            or nykyinen_aika < self.seuraava_animaatio
        ):
            return

        seuraava_indeksi = min(
            self.animaation_indeksi + self.animaation_askel,
            len(self.animaation_ruudut)
        )

        self.tutkitut.update(
            self.animaation_ruudut[
                self.animaation_indeksi:seuraava_indeksi
            ]
        )

        self.animaation_indeksi = seuraava_indeksi
        self.seuraava_animaatio = nykyinen_aika + 15

        if self.animaation_indeksi >= len(self.animaation_ruudut):
            self.animaatio_valmis = True

    def piirra(self):
        """Piirtää käyttöliittymän yhden ruudun."""
        self.ikkuna.fill(TAUSTA)

        self.piirra_ylatunniste()
        self.piirra_ruudukko()
        self.piirra_sivupaneeli()

        pygame.display.flip()

    def piirra_ylatunniste(self):
        """Piirtää ohjelman otsikon ja lyhyen kuvauksen."""
        piirra_teksti(
            self.ikkuna,
            self.otsikko_fontti,
            "PATHFINDING LAB",
            20,
            25
        )

        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "Valitse toiminto ja muokkaa ruudukkoa hiirella.",
            20,
            50
        )

    def piirra_ruudukko(self):
        """Piirtää ruudukon nykyisen tilanteen."""
        naytettava_reitti = (
            self.reitti if self.animaatio_valmis else None
        )

        piirra_ruudukko(
            self.ikkuna,
            self.ruudukko,
            self.lahto,
            self.maali,
            self.tutkitut,
            naytettava_reitti,
            self.ruudun_koko
        )

    def piirra_sivupaneeli(self):
        """Piirtää oikean reunan ohje- ja tulospaneelin."""
        paneeli = pygame.Rect(880, 20, 400, 810)

        pygame.draw.rect(
            self.ikkuna,
            VALKOINEN,
            paneeli,
            border_radius=8
        )

        pygame.draw.rect(
            self.ikkuna,
            PANEELIN_REUNA,
            paneeli,
            1,
            border_radius=8
        )

        self.piirra_karttaohjeet()
        self.piirra_muokkausohjeet()
        self.piirra_algoritmiohjeet()
        self.piirra_toimintoohjeet()
        self.piirra_vertailutulokset()

    def piirra_erotin(self, y):
        """Piirtää paneeliin osioita erottavan viivan."""
        pygame.draw.line(
            self.ikkuna,
            PANEELIN_REUNA,
            (900, y),
            (1260, y),
            1
        )

    def piirra_karttaohjeet(self):
        """Piirtää karttakokojen ohjeet."""
        x = 900

        piirra_teksti(
            self.ikkuna,
            self.otsikko_fontti,
            "KARTTAKOKO",
            x,
            35
        )

        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "F1: 30 x 20",
            x,
            75
        )
        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "F2: 50 x 50",
            x,
            98
        )
        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "F3: 100 x 100",
            x,
            121
        )

        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            f"Nykyinen: {self.ruudukon_leveys} x "
            f"{self.ruudukon_korkeus}",
            x,
            151
        )

        self.piirra_erotin(185)

    def piirra_muokkausohjeet(self):
        """Piirtää ruudukon muokkaamiseen liittyvät ohjeet."""
        x = 900

        piirra_teksti(
            self.ikkuna,
            self.otsikko_fontti,
            "RUUDUKON MUOKKAUS",
            x,
            200
        )

        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "S: Aseta lähtöpiste",
            x,
            238
        )
        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "G: Aseta maalipiste",
            x,
            261
        )
        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "E: Lisää tai poista este",
            x,
            284
        )
        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "Oikea klikkaus: Poista este",
            x,
            307
        )

        self.piirra_erotin(340)

    def piirra_algoritmiohjeet(self):
        """Piirtää algoritmin valintaan liittyvät ohjeet."""
        x = 900

        piirra_teksti(
            self.ikkuna,
            self.otsikko_fontti,
            "ALGORITMI",
            x,
            355
        )

        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "1: A*",
            x,
            393
        )
        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "2: Fringe Search",
            x,
            416
        )
        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            f"Valittu: {self.valittu_algoritmi}",
            x,
            443
        )

        self.piirra_erotin(475)

    def piirra_toimintoohjeet(self):
        """Piirtää ohjelman toimintojen näppäinohjeet."""
        x = 900

        piirra_teksti(
            self.ikkuna,
            self.otsikko_fontti,
            "TOIMINNOT",
            x,
            490
        )

        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "R: Suorita valittu algoritmi",
            x,
            528
        )
        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "V: Vertaa molempia algoritmeja",
            x,
            551
        )
        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "C: Tyhjennä esteet",
            x,
            574
        )
        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            "ESC: Sulje ohjelma",
            x,
            597
        )

        self.piirra_erotin(630)

    def piirra_vertailutulokset(self):
        """Piirtää algoritmien vertailutulokset tiiviissä muodossa."""
        x = 900

        piirra_teksti(
            self.ikkuna,
            self.otsikko_fontti,
            f"VERTAILUTULOKSET ({VERTAILU_TOISTOT} ajoa)",
            x,
            635
        )

        if self.vertailutulokset is None:
            piirra_teksti(
                self.ikkuna,
                self.pieni_fontti,
                self.tulosviesti,
                x,
                675
            )
            return

        astar = self.vertailutulokset["A*"]
        fringe = self.vertailutulokset["Fringe Search"]

        self.piirra_algoritmin_tulos("A*", astar, x, 665)
        self.piirra_algoritmin_tulos(
            "Fringe Search",
            fringe,
            x,
            730
        )

        if astar["keskiarvo"] < fringe["keskiarvo"]:
            nopeampi = "A*"
        elif fringe["keskiarvo"] < astar["keskiarvo"]:
            nopeampi = "Fringe Search"
        else:
            nopeampi = "Tasapeli"

        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            f"Nopeampi keskiarvolla: {nopeampi}",
            x,
            795
        )

    def piirra_algoritmin_tulos(self, nimi, tulos, x, y):
        """Piirtää yhden algoritmin vertailutiedot."""
        piirra_teksti(
            self.ikkuna,
            self.fontti,
            nimi,
            x,
            y
        )

        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            (
                f"KA {tulos['keskiarvo']:.4f} ms"
                f" | min {tulos['min']:.4f}"
                f" | max {tulos['max']:.4f}"
            ),
            x,
            y + 21
        )

        reitin_pituus = tulos["reitin_pituus"]
        if reitin_pituus is None:
            reitin_pituus = "-"

        piirra_teksti(
            self.ikkuna,
            self.pieni_fontti,
            (
                f"Reitti: {reitin_pituus} askelta"
                f" | Tutkitut: {tulos['tutkitut']} ruutua"
            ),
            x,
            y + 41
        )


def main():
    """Käynnistää reitinhakualgoritmien käyttöliittymän."""
    sovellus = PathfindingSovellus()
    sovellus.suorita()


if __name__ == "__main__":
    main()
