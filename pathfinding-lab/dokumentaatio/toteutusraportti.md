# Toteutusraportti

## Ohjelman rakenne

Työn tavoitteena on toteuttaa sovellus, jolla voidaan vertailla kahta reitinhakualgoritmia, A\*:aa ja Fringe Searchia. Sovelluksessa käyttäjä voi luoda ruudukon, lisätä siihen esteitä sekä määrittää lähtö- ja maalipisteen. Tämän jälkeen algoritmi etsii reitin pisteiden välille ja näyttää löydetyn reitin graafisesti.

Ohjelma on toteutettu Pythonilla ja käyttöliittymässä käytetään Pygame-kirjastoa. Koodi on jaettu eri tiedostoihin toimintojen mukaan. Ruudukon käsittelyyn liittyvät toiminnot sijaitsevat `grid.py`-tiedostossa. A\*-algoritmi on toteutettu `astar.py`-tiedostossa ja Fringe Search omassa `fringe_search.py`-tiedostossaan. Käyttöliittymästä ja algoritmien visualisoinnista vastaa `visualizer.py`.

Ruudukko koostuu kaksiulotteisista koordinaateista, ja esteiden sijainnit tallennetaan set-tietorakenteeseen. Molemmat algoritmit käyttävät sanakirjoja reitin kustannusten ja edeltävien ruutujen tallentamiseen. A\* käyttää lisäksi `heapq`-kirjaston tarjoamaa kekorakennetta seuraavan tutkittavan ruudun valintaan. Fringe Search puolestaan käsittelee ruutuja listoissa kustannusrajan perusteella.

## Algoritmien aikavaativuudet ja suorituskyky

A*-algoritmin toimintaan vaikuttavat erityisesti tutkittavien ruutujen määrä ja prioriteettijonon käsittely. Prioriteettijonon alkioiden lisääminen ja poistaminen toimii aikavaativuudella O(log n), missä n on jonon koko. A*:n kokonaisaikavaativuus riippuu heuristiikasta ja ruudukon rakenteesta. Pahimmassa tapauksessa se voi tutkia suuren osan ruudukosta.

Fringe Search käyttää kustannusrajoihin perustuvaa käsittelyä prioriteettijonon sijaan. Sen suorituskykyyn vaikuttavat muun muassa käsittelykierrosten määrä ja ruutujen mahdollinen uudelleenkäsittely. Molempien algoritmien suorituskykyä voidaan vertailla sovelluksen mittaustoiminnolla, joka suorittaa algoritmit useita kertoja ja laskee suoritusaikojen keskiarvon.

## Käytettävyys ja visualisointi

Sovelluksessa on graafinen käyttöliittymä, jonka avulla käyttäjä voi muokata ruudukkoa hiirellä ja käynnistää algoritmit näppäimistön avulla. Eri ruututyypit, kuten esteet, lähtöpiste, maalipiste ja löydetty reitti, esitetään eri väreillä. Näin algoritmien toimintaa on helpompi seurata.

Käyttöliittymässä voidaan myös vertailla molempia algoritmeja samalla ruudukolla. Vertailussa näytetään suoritusaikojen keskiarvo, pienin ja suurin suoritusaika sekä löydetyn reitin pituus ja tutkittujen ruutujen määrä.

## Puutteet ja jatkokehitys
