# Vaatimusmäärittely – Pathfinding Lab

**Opinto-ohjelma:** Tietojenkäsittelytiede, kandidaatin tutkinto

Projektin tavoitteena on toteuttaa Pythonilla sovellus, jolla voidaan tutkia ja vertailla kahta reitinhakualgoritmia: A\*:aa ja Fringe Searchia. Sovelluksessa käyttäjä voi luoda kaksiulotteisen ruudukon, määrittää lähtö- ja maalipisteen sekä lisätä ruudukkoon esteitä. Tämän jälkeen käyttäjä voi suorittaa valitsemansa algoritmin ja tarkastella sen löytämää reittiä sekä hakuprosessin etenemistä.

Projektin keskeinen osa on algoritmien toteuttaminen ja niiden oikean toiminnan varmistaminen. Visualisointi toimii algoritmien tutkimista ja vertailua tukevana ominaisuutena.

## Tekninen toteutus

- Ohjelmointikieli: Python.
- Sovellus toteutetaan graafisella käyttöliittymällä.
- Sovellus ja dokumentaatio toteutetaan suomeksi.
- Riippuvuuksien hallintaan käytetään Poetryä.
- Testaus toteutetaan Pythonin unittest-kehyksellä.
- Vertaisarviointia pystyn tekemään myös JavaScript- ja TypeScript-projekteista.

Algoritmien toteutuksessa käytetään ruudukon esittämiseen kaksiulotteista tietorakennetta. A\* hyödyntää prioriteettijonoa tutkittavien solmujen järjestämiseen. Molemmissa algoritmeissa tarvitaan lisäksi tietorakenteita käsiteltyjen solmujen, kustannusten ja löydetyn reitin tallentamiseen.

## Toiminnalliset vaatimukset

Sovelluksen tulee mahdollistaa:

- Kaksiulotteisen ruudukon luominen ja muokkaaminen.
- Lähtö- ja maalipisteen määrittäminen.
- Esteiden lisääminen ja poistaminen.
- A\*- ja Fringe Search -algoritmin valitseminen ja suorittaminen.
- Hakuprosessin ja löydetyn reitin visualisointi.
- Tilanteen ilmoittaminen, jos reittiä ei löydy.
- Algoritmien tulosten vertailu ja mittaustietojen näyttäminen.

## Algoritmien vertailu ja vaativuudet

Algoritmeja vertaillaan samoilla ruudukoilla ja samoilla lähtö- ja maalipisteillä. Vertailussa tarkastellaan löydetyn reitin pituutta, tutkittujen solmujen määrää ja suoritusaikaa.

A\*:n aikavaativuuden yleinen graafihakutoteutukseen perustuva arvio on \(O((V+E)\log V)\), kun käytössä on binäärikeolla toteutettu prioriteettijono ja tietyt algoritmin toimintaan liittyvät oletukset. Tilavaativuus on \(O(V)\).

Fringe Searchin hakupuun pahimman tapauksen kokoa voidaan kuvata yleisellä arviolla \(O(b^d)\). Sen muistinkäyttö riippuu hakurintaman ja tallennettavien solmukohtaisten tietojen määrästä.

Algoritmien todelliseen suorituskykyyn vaikuttavat muun muassa ruudukon koko, esteiden määrä ja kartan rakenne.

## Testaus ja rajaukset

Algoritmien oikeellisuus varmistetaan automatisoiduilla yksikkötesteillä. Testeissä tarkastellaan esimerkiksi reitin löytymistä, esteiden huomioimista, reitin laillisuutta ja tilanteita, joissa reittiä ei ole mahdollista löytää.

Sovellus rajataan kaksiulotteisiin ruudukoihin ja kahteen reitinhakualgoritmiin. Projektin ulkopuolelle jätetään esimerkiksi kolmiulotteiset kartat, liikkuvat esteet ja verkkopohjaiset karttapalvelut. Mahdolliset lisäominaisuudet toteutetaan vasta ydintoiminnallisuuksien valmistuttua.

## Lähteet

- [A\* Search Algorithm – Red Blob Games](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
- [A\* Search Algorithm – Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Fringe Search: Beating A\* at Pathfinding on Game Maps – Björnsson ym. (2005)](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf)
- [Fringe Search – Wikipedia](https://en.wikipedia.org/wiki/Fringe_search)
