# Vaatimusmäärittely – Pathfinding Lab

**Opinto-ohjelma:** Tietojenkäsittelytiede, kandidaatin tutkinto

## Projektin kuvaus

Pathfinding Lab on Pythonilla toteutettava sovellus, jonka avulla voidaan tutkia ja havainnollistaa reitinhakualgoritmien toimintaa. Sovelluksen ideana on näyttää, miten algoritmi etenee lähtöpisteestä kohti maalipistettä ja miten ympäristössä olevat esteet vaikuttavat reitin löytämiseen.

Käyttäjä voi muodostaa kaksiulotteisen ruudukon, määrittää siihen lähtö- ja maalipisteen sekä lisätä esteitä vapaasti valitsemiinsa kohtiin. Tämän jälkeen käyttäjä voi suorittaa valitsemansa algoritmin ja tarkastella haun etenemistä käyttöliittymässä.

Projektissa toteutetaan A\*-algoritmi ja Fringe Search. Niiden toimintaa vertaillaan erilaisilla kartoilla, jotta voidaan selvittää, miten kartan rakenne ja esteiden määrä vaikuttavat reitinhakuun. Vertailussa hyödynnetään esimerkiksi löydetyn reitin pituutta, tutkittujen solujen määrää ja suoritusaikaa.

Tavoitteena on saada aikaan toimiva ja selkeä sovellus, jonka avulla reitinhakualgoritmien toimintaa voidaan tarkastella käytännössä.

## Tekninen toteutus

- Sovellus toteutetaan Python-ohjelmointikielellä.
- Käyttöliittymä toteutetaan graafisena, jotta algoritmien etenemistä voidaan havainnollistaa visuaalisesti.
- Ohjelma ja projektin dokumentaatio kirjoitetaan suomeksi.
- Ohjelman rakenne suunnitellaan siten, että algoritmit, kartan käsittely ja käyttöliittymä ovat mahdollisimman selkeästi erotettuja toisistaan.
- Algoritmien toimintaa varmistetaan automaattisilla yksikkötesteillä.
- Projektista laaditaan asennus- ja käyttöohjeet.

## Toiminnalliset vaatimukset

Sovelluksen tulee sisältää seuraavat ominaisuudet:

- Käyttäjä voi luoda ja muokata kaksiulotteista ruudukkoa.
- Käyttäjä voi määrittää lähtöpisteen ja maalipisteen.
- Käyttäjä voi lisätä ja poistaa esteitä, jotka rajoittavat mahdollisia kulkureittejä.
- Käyttäjä voi valita suoritettavan algoritmin A\*-algoritmin ja Fringe Searchin väliltä.
- Sovellus etsii reitin lähtöpisteestä maalipisteeseen valitulla algoritmilla.
- Käyttöliittymä näyttää haun etenemisen, jotta käyttäjä pystyy seuraamaan algoritmin toimintaa.
- Sovellus näyttää löydetyn reitin selkeästi kartalla.
- Jos reittiä ei ole mahdollista löytää, sovellus ilmoittaa siitä käyttäjälle.
- Käyttäjä voi tyhjentää tai palauttaa kartan ja suorittaa uuden haun.
- Sovellus kerää haun aikana tietoa, jonka avulla algoritmien toimintaa voidaan vertailla.

## Algoritmien vertailu

Algoritmien vertailu on yksi projektin keskeisistä tavoitteista. Vertailu toteutetaan suorittamalla algoritmit samoilla kartoilla ja samoista lähtö- ja maalipisteistä.

Vertailussa tarkastellaan seuraavia asioita:

- **Reitin pituus:** kuinka monta askelta löydetty reitti sisältää.
- **Tutkitut solut:** kuinka monta ruudukkosolua algoritmi käsittelee haun aikana.
- **Suoritusaika:** kuinka kauan reitin löytäminen kestää.

Tulosten avulla voidaan tarkastella, miten algoritmien toiminta eroaa toisistaan ja millaisissa tilanteissa erot tulevat esiin. Vertailussa huomioidaan myös se, että reitin pituus ja suoritusaika eivät yksinään kerro kaikkea algoritmin toiminnasta.

## Testaus ja luotettavuus

Ohjelman keskeiset toiminnot testataan automaattisilla testeillä. Testauksessa varmistetaan, että algoritmit löytävät kelvollisen reitin silloin, kun sellainen on olemassa, ja tunnistavat tilanteet, joissa reittiä ei löydy.

Lisäksi testataan erilaisten karttojen käsittelyä, esteiden vaikutusta reitinhakuun sekä löydetyn reitin oikeellisuutta. Reitti ei saa kulkea esteiden läpi, ja sen tulee noudattaa sovelluksessa määriteltyjä liikkumissääntöjä.

Ohjelman tulee käsitellä virheelliset käyttötilanteet hallitusti niin, etteivät ne aiheuta sovelluksen odottamatonta kaatumista.

## Rajaukset

Projektin ensimmäinen versio keskittyy kaksiulotteiseen ruudukkoon ja kahden reitinhakualgoritmin toimintaan. Sovellukseen ei toteuteta esimerkiksi kolmiulotteisia ympäristöjä, liikkuvia esteitä, verkkopohjaisia karttoja tai käyttäjätilejä.

Mahdolliset lisäominaisuudet toteutetaan vasta, kun keskeiset algoritmit, käyttöliittymä ja testaus toimivat luotettavasti.

## Lähteet

- [A\* Search Algorithm – Red Blob Games](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
- [Fringe Search – Wikipedia](https://en.wikipedia.org/wiki/Fringe_search)
