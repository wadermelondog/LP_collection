# LP kokoelma

## Palautus
Ohjelmoinnin perusteet: Harjoitustyön palautus  
### Turunen Lauri \[AG3154\]  
  
Linkki harjoitustyön dokumentointiin:
 [Linkki](https://gitlab.labranet.jamk.fi/AG3154/loppuprojektitest)

4-5
<br>
ITSEARVIO

Vahvuudet

+ Sovellus toimii halutusti
+ Käytin mielestäni aika hyvin opintojakson tekniikoita
+ csv filen handling toimii hyvin.
+ Syötteiden error handling on mielestäni aika hyvä, vaikka except errorit jäivät vähäiselle.
+ Flowchart on mielestäni hyvä lisä.

Kehitettävää
- Add_record funktiosta tuli jokseenkin turvonnut, siihen olisi voinut tehdä apufunktion keyn handlaamiseen ja syöttää vaikka dictionarylla tietyt arvot tietyn keyn ilmetessä sen sijaa että olisi tuolla lailla elif lausekkeet eri arvoille.
- Missä vaan vaiheessa esc painaminen jotta pääsisi main menuun jäi toteuttamatta.
- Omia luokkia tms ei tullut käytettyä mutta en kyllä niitä tuntunut tarvitsevankaan.


### Perusidea
Python ohjelma joka ylläpitää vinyylikokoelmaani.

### Funktiot
Ainakin:

Hakufunktio kokoelmasta: parametreina täytyy voida olla käytännössä mikä vaan levyn parametri, kunnon perusteella tai vaikka julkaisijan.

Uuden levyn lisääminen: parametreiksi artisti, levyn nimi, labeli, vuosi, tarkka formaatti eli esim: 2lp, 3lp, 180grammanen yms. Hinta? Millä hyllyllä se mulla on/vitriinissä.
tähdet /5 ja vielä lisätieto sekä lisäämispäivämäärä, eli siis käytännössä kaikki mitä discogsissakin on. Alla discogsin parametrit.
Catalog#,Artist,Title,Label,Format,Rating,Released,release_id,CollectionFolder,Date Added,Collection Media Condition,Collection Sleeve Condition,Collection Notes

Levyn tietojen muokkaaminen

Levyn tietojen poistaminen

#### Lauri Turunen 23/09/2024


## 26/10/2024 

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

## 28/11/2024
Nonniin nyt on aika urakoida tämä loppuun
15:40 Locked in
17:40 hyvällä mallilla
21:34 valmis, viel tarkentavia kommentteja ja parsimista sekä outputtien formatoimista, sekä stats kohdassa average year on viel rikki

## 29/11/2024
Average year toimii jotenkuten, jos ei oo tarpeeks levyjä niin tulee zerodivision error, täytyy korjata
lisäilin kamaa, esimerkiksi add record kohdassa condition kohdissa se nyt näyttää suoraan että valitse näistä kunnoista ja sit voi valita minkä kuntonen sleeve on yms.
Ainoa ongelma on että nyt se jäätyy siinä kohdassa :D, Duunailin sitä vähäsen ja formattiin laitoin saman että tulee promptia ja se vaan kysyy mikä laitetaan.
Discogsin formaattilista on vaan niin pitkä että todennäköisesti ainakin tässä tekstipohjaisessa ohjelmassa päädyn siihen että omalla user inputilla sitten laitellaan ne ylimääräset.

![Formaattilista](/Dokumentaatio/image.png)

## 04/12/2024
Hyvää edistystä tänään, oon useamman tunnin tätä rustannut englannin tehtävien sijaan...
Lisää error handlingia, melkein voisin tehdä oman errorin mut en oo jaksanu...
Kaikenlaista...
Paljon viel bugeja mutta sain projektia eteenpäin.

## 10/12/2024
Lisää bugfixejä ja error handlingiä.  
Ajattelin ehkä joskus lisätä sellaisen ominaisuuden että voisi olla asetukset tiedosto johon se tallentaa mm. kokoelman filename ja se osaa sitten ladata sen aina.  
Ehkä jos joskus oikein innostun voisin API:n avulla hakea kokoelman keskiarvon tms. Tähän vaatis vaan aika paljon error handlingiä yms ja sinänsä discogsin sivulla on jo se suoraan niin emt.
Hieman tulee kyseenalaistettua tuota list collection ominaisuutta, sitä ei ehkä tuu käytettyä yhtä paljon kuin searchia kun search on sen verran hyvä funktio... 
TODO: case insensitive handling kaikkeen  
klo 23:34, implementoin uutta funktiota, confirmation. Käytän tuota yes or no hässäkkää niin paljon että teen sen vaan suoraan omaan funktioon niin helpompaa.
Otin kans wakatime käyttöön

![Flowchart](/Dokumentaatio/flowchart.png)

## 11/12/2024
Case insensitive handling ja confirmation funktio hoidettu.
Sain idean että viimeinen funktio minkä toteutan on handle folders funktio et vois tos search funktiossa vaikka siirtää kaikki hakutulokset eri folderiin tms. Tän teen ehkä joskus myöhemmin, jätän tän nyt tälläisekseen.



