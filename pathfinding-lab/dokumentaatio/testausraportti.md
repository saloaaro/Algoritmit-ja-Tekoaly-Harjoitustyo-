# Testausraportti

## 1. Testauksen tavoitteet

Testauksen tarkoituksena on varmistaa, että Pathfinding Lab toimii oikein ja että molemmat toteutetut reitinhakualgoritmit löytävät reittejä odotetulla tavalla. Testasin erityisesti ruudukon toimintaa, A\*- ja Fringe Search -algoritmeja sekä ohjelman käyttöliittymän eri toimintoja.

## 2. Testausympäristö

Testaus toteutettiin seuraavassa ympäristössä:

- Ohjelmointikieli: Python 3.11
- Riippuvuuksien hallinta: Poetry
- Käyttöliittymä: Pygame
- Testauskirjasto: unittest
- Testikattavuus: coverage.py

## 3. Yksikkötestaus

Kirjoitin ohjelmalle yksikkötestejä Pythonin unittest-kirjastolla. Testit on jaettu kolmeen tiedostoon, jotta eri osien testaaminen pysyy selkeänä.

- `test_grid.py` testaa ruudukon toimintaa, esteitä ja naapuriruutujen hakemista.
- `test_astar.py` testaa A\*-algoritmin toimintaa ja reitin löytämistä.
- `test_fringe_search.py` testaa Fringe Search -algoritmin toimintaa ja reitin löytämistä.

Testeissä käydään läpi esimerkiksi tilanteita, joissa reitti löytyy normaalisti tai esteiden kiertämisen kautta. Testeissä tarkistetaan myös tilanne, jossa reittiä ei ole mahdollista löytää. Lisäksi testasin esimerkiksi sitä, mitä tapahtuu, kun lähtö- ja maalipiste ovat samassa ruudussa tai niiden kohdalla on este.

Testit suoritettiin seuraavalla komennolla:

`poetry run python -m unittest discover -s tests -v`

Kaikki 29 testiä menivät läpi, eikä testien suorittamisessa tullut virheitä.

## 4. Testikattavuus

Testikattavuutta mittasin coverage.py-työkalulla. Käytin seuraavia komentoja:

`poetry run coverage run -m unittest discover -s tests`

`poetry run coverage report -m`

Testikattavuuden tulokset olivat seuraavat:

| Tiedosto                | Kattavuus |
| ----------------------- | --------: |
| `__init__.py`           |     100 % |
| `astar.py`              |      98 % |
| `fringe_search.py`      |      92 % |
| `grid.py`               |     100 % |
| `test_astar.py`         |      98 % |
| `test_fringe_search.py` |      98 % |
| `test_grid.py`          |      98 % |
| **Yhteensä**            |  **97 %** |

Kattavuus oli mielestäni hyvä. Kaikkia koodin rivejä ei kuitenkaan saatu testien kautta suoritettua. On myös hyvä huomioida, että käyttöliittymän `visualizer.py`-tiedostoa ei ole mukana tässä kattavuustuloksessa, vaan testasin sen toimintaa erikseen käyttämällä ohjelmaa.

## 5. Käyttöliittymän manuaalinen testaus

Käyttöliittymää testasin käynnistämällä ohjelman ja kokeilemalla sen eri toimintoja. Tarkistin, että ruudukko näkyy oikein ja että sitä pystyy muokkaamaan hiirellä.

Testasin seuraavia toimintoja:

- Eri kokoisten karttojen avaaminen.
- Lähtö- ja maalipisteen asettaminen.
- Esteiden lisääminen ja poistaminen.
- A\*- ja Fringe Search -algoritmien valitseminen.
- Reitinhaun suorittaminen.
- Tutkittujen ruutujen ja löydetyn reitin näyttäminen.
- Molempien algoritmien vertailun käynnistäminen.
- Vertailutulosten näyttäminen sivupaneelissa.

## 6. Yhteenveto

Testauksen perusteella ohjelman tärkeimmät toiminnot toimivat tällä hetkellä suunnitellusti. Kaikki 29 yksikkötestiä menivät läpi ja testikattavuudeksi saatiin 97 %. Erityisesti ruudukon ja reitinhakualgoritmien toiminta on testattu useilla erilaisilla tilanteilla.

Käyttöliittymän toiminta on lisäksi tarkistettu manuaalisesti. Testauksen aikana löytyneet pienet ongelmat on korjattu. Testausta on tarkoitus jatkaa vielä projektin seuraavien viikkojen aikana, kun ohjelmaa kehitetään eteenpäin.
