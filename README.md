# Loppuprojektitest
Tämä on projekti python kurssille. Se on vasta aloitusvaiheessa

Perusidea
Python ohjelma joka ylläpitää vinyylikokoelmaani.

Funktiot
Ainakin:

Hakufunktio kokoelmasta: parametreina täytyy voida olla käytännössä mikä vaan levyn parametri, kunnon perusteella tai vaikka julkaisijan.

Uuden levyn lisääminen: parametreiksi artisti, levyn nimi, labeli, vuosi, tarkka formaatti eli esim: 2lp, 3lp, 180grammanen yms. Hinta? Millä hyllyllä se mulla on/vitriinissä.
tähdet /5 ja vielä lisätieto sekä lisäämispäivämäärä, eli siis käytännössä kaikki mitä discogsissakin on. Alla discogsin parametrit.
Catalog#,Artist,Title,Label,Format,Rating,Released,release_id,CollectionFolder,Date Added,Collection Media Condition,Collection Sleeve Condition,Collection Notes

Levyn tietojen muokkaaminen

Levyn tietojen poistaminen

Lauri Turunen 23/09/2024


26/10/2024 

Ideointia projektia varten,
Funktioihin muutoksia.
Menu: Näyttää statseja kokoelmasta tällä hetkellä, mm levyjen määrä
1. Lisää uusi levy
2. Hae levyjä
    Alaohjelmat hakutoimintoon, Muokkaa levyn tietoja ja poista levy
3. Luettele kaikki levyt, tähän mahdollisuus listata vaan tietyt tiedot levyistä
4. Lataa kokoelma, mahdollisuus luoda uusi kokoelma
5. Wish list, alkeellinen tapa pitää kirjaa levyista jota haluaisin

Päätin toteuttaa projektin niin että ohjelma lataa .csv tiedoston aina alussa dictionaryksi jolloin sen käsittely on helpompaa ja sitten aina suljettaessa tallentaa sen takaisin .csv:ksi, pythonissa on DictReader metodi jolla voidaan lukea tiedosto listaksi dictionaryja ja se syöttää niihin dictionaryihin ylimmästä rivistä avaimiksi ne catalog, nimi yms
