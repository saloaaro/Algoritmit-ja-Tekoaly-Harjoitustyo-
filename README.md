# Algoritmit-ja-Tekoaly-Harjoitustyo

Projektin kuvaus

Pathfinding Lab on Pythonilla toteutettu sovellus, jossa voidaan kokeilla ja vertailla kahta reitinhakualgoritmia: A*-algoritmia ja Fringe Search -algoritmia.

Sovelluksessa reitinhakua tarkastellaan ruudukolla, jossa käyttäjä voi määrittää lähtö- ja maalipisteen sekä lisätä esteitä. Algoritmien toimintaa visualisoidaan näyttämällä niiden tutkimat ruudut ja löytämä reitti.

Projektin tavoitteena on tutustua reitinhakualgoritmien toimintaan ja vertailla niiden suorituskykyä erilaisissa tilanteissa.

# Asennus ja käynnistys

Projektin suorittamiseen tarvitaan Python ja Poetry.

Kloonaa ensin repositorio:

git clone https://github.com/saloaaro/Algoritmit-ja-Tekoaly-Harjoitustyo-.git

Siirry projektihakemistoon:

cd Algoritmit-ja-Tekoaly-Harjoitustyo-/pathfinding-lab

Asenna projektin riippuvuudet:

poetry install

Ohjelman käynnistäminen

Käynnistä sovellus projektihakemistossa seuraavalla komennolla:

poetry run python -m pathfinding_lab.visualizer

Oikealla painikkeella poistetaan este ruudukolta.

# Testien suorittaminen

Projektin yksikkötestit suoritetaan projektihakemistossa seuraavalla komennolla:

poetry run python -m unittest discover -s tests -v

Testikattavuuden voi mitata komennoilla:

poetry run coverage run -m unittest discover -s tests
poetry run coverage report -m
