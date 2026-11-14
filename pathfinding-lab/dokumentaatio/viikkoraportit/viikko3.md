# Viikkoraportti 3

**Käytetty aika:** 24 tuntia

## Mitä olen tehnyt tällä viikolla?

Tällä viikolla olen jatkanut ohjelman kehittämistä ja tehnyt sille graafisen käyttöliittymän Pygame-kirjastolla. Käyttöliittymän kautta pystyy muokkaamaan ruudukkoa, asettamaan lähtö- ja maalipisteen sekä lisäämään ja poistamaan esteitä. Toteutin myös mahdollisuuden vaihtaa kartan kokoa ja valita käytettävän algoritmin.

Lisäksi tein visualisoinnin, jossa näkee algoritmin tutkimat ruudut ja sen löytämän reitin. Toteutin myös toiminnon, jolla A\*- ja Fringe Search -algoritmien tuloksia voidaan vertailla. Vertailussa algoritmit suoritetaan 30 kertaa, minkä jälkeen ohjelma näyttää suoritusaikojen keskiarvot sekä pienimmät ja suurimmat ajat.

## Miten ohjelma on edistynyt?

Ohjelma on edistynyt hyvin, ja nyt siinä on myös toimiva graafinen käyttöliittymä. A\*- ja Fringe Search -algoritmeja pystyy suorittamaan käyttöliittymän kautta, ja niiden etenemistä voi seurata ruudukossa. Myös algoritmien vertailu toimii ja näyttää tulokset ohjelman sivupaneelissa.

Testasin ohjelmaa uudelleen, ja kaikki 29 yksikkötestiä menivät läpi. Testikattavuus on tällä hetkellä 97 %. Tarkistin myös koodin laatua Pylintillä, jonka tulokseksi sain 9,82/10. Käyttöliittymän toimintaa olen testannut itse ohjelmaa käyttämällä.

## Mitä opin tällä viikolla?

Opin tällä viikolla lisää Pygame-kirjastosta ja siitä, miten Pythonilla voidaan toteuttaa graafinen käyttöliittymä. Erityisesti hiiren ja näppäimistön tapahtumien käsittely, ruudukon piirtäminen ja reitinhaun visualisointi olivat uusia asioita.

Opin myös lisää algoritmien suorituskyvyn mittaamisesta. Vertailua tehdessä piti miettiä, miten tuloksista saadaan mahdollisimman vertailukelpoisia ja miksi algoritmeja kannattaa suorittaa useamman kerran yksittäisen mittauksen sijaan.

## Mikä jäi epäselväksi tai tuotti vaikeuksia?

Suurimmat vaikeudet liittyivät käyttöliittymän rakentamiseen ja sen ulkoasun säätämiseen. Vertailutulokset eivät aluksi mahtuneet kunnolla sivupaneeliin, joten jouduin muuttamaan niiden sijoittelua useamman kerran. Myös eri kokoisten ruudukkojen sovittaminen samaan ikkunaan vaati hieman kokeilua.

Algoritmien vertailussa piti lisäksi ottaa huomioon suoritusaikojen vaihtelu. Yksittäinen mittaus ei välttämättä anna kovin luotettavaa kuvaa algoritmin nopeudesta, minkä vuoksi päädyin käyttämään useita mittauskertoja.

## Mitä teen seuraavaksi?

Seuraavaksi jatkan ohjelman kehittämistä ja testaan sen toimintaa erilaisilla kartoilla ja esteiden määrillä. Tarkoituksena on myös tehdä käyttöliittymään ja algoritmien vertailuun vielä parannuksia. Samalla jatkan dokumentaation ja käyttöohjeiden tekemistä. Seuraavaksi keskityn erityisesti ohjelman kehittämiseen ja vaatimusten läpikäymiseen. Tarkoituksena on myös muuttaa vertailufunktiota niin, että mittausjärjestys vuorottelee eri kierroksilla. Näin algoritmien suoritusjärjestys ei suosi jatkuvasti samaa algoritmia.
