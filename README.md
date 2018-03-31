


# Image recognition hackathon

## Data downloaden
**Let op: de data voor opdracht 1 en 2 staan niet meer in deze GitHub repository.** Ze waren te groot. Je kunt ze nu via Google Drive downloaden.     
[Download hier de data voor de hackathon](https://drive.google.com/drive/folders/1QstBfDuQKXfY8C3P3wK507CgE4tBUGQB).

## Antwoorden van Wetterskip Fryslan op vragen

_Wat is de vergrotingsfactor van de foto's van diatomeeën?_
De foto's zijn allemaal gemaakt met een vergrotingsfactor 1000.

_Waar zijn meer foto's van diatomeeën te vinden?_
* [ADIA Diatom Image Database](http://rbg-web2.rbge.org.uk/ADIAC/db/adiacdb.htm)
* [GENERA - Diatoms of the United States](https://westerndiatoms.colorado.edu/genera)
* [Diatom Flora of Britain and Ireland](https://naturalhistory.museumwales.ac.uk/diatoms/taxalist.php?-action=search&-genus=Achnanthidium&-max=100&-skip=0&#top)

## Openstaande vragen

*	Is het mogelijk om meer beeldmateriaal van diatomeeën te krijgen van andere noordelijke waterschappen?
*	Hoe is er omgegaan met de naamgeving als er meerder diatomeeënsoorten op een beeld staan, bijvoorbeeld bij foto `Eolimna subminuscula.jpg`?
* Is het mogelijk om extra luchtfoto's (100x100 tegels) beschikbaar te stellen? Kan het script dat gebruikt is voor het klaarzetten van de data ook gedeeld worden?
* Kunnen de infrarood beelden van de 100x100 tegels ook gedeeld worden?
* Is er metadata beschikbaar van de luchtfototegels? Bijvoorbeeld datum en tijd van opname.

## BGT-waterdelen voor extra training en test data
Je kunt nu ook een [ZIP-bestand downloaden](https://drive.google.com/open?id=1eMRib4FvU_ICus16KmYupVXF7g8JGsu1) met daarin een shape met alle [BGT-waterdelen](http://imgeo.geostandaarden.nl/def/imgeo-object/waterdeel) in Fryslân.     
BGT staat voor Basisregistratie Grootschalige Topografie. De BGT is een digitale basiskaart, opgebouwd uit objecten als wegen, water, groen en spoor die in veel werkprocessen van de overheid nodig zijn. De BGT is open data.     
De gegevens zijn in EPSG:28992 oftewel in het [Amersfoort/RD New coordinatensysteem](https://nl.wikipedia.org/wiki/Rijksdriehoeksco%C3%B6rdinaten).     
Voor de hackathon kun je de BGT-waterdelen samen met [luchtfoto's](https://www.pdok.nl/nl/producten/pdok-services/overzicht-urls/l) of [satellietbeelden](http://www.satellietbeeld.nl/) gebruiken om meer training of test data te genereren.

## Casussen
De casussen zijn ingebracht door Wetterskip Fryslân. Het gaat om het ontwikkelen van een image recognition algoritme voor
* [het classificeren van land en water in luchtfoto's](https://drive.google.com/drive/folders/1QstBfDuQKXfY8C3P3wK507CgE4tBUGQB) of
* [het onderscheiden van datomeeën in microscoopbeelden](https://drive.google.com/drive/folders/1QstBfDuQKXfY8C3P3wK507CgE4tBUGQB).      

Klik op de link om de data te downloaden.     
Bij vragen over de casussen of trainingsdata kun je contact opnemen met Marcel Adema: madema(apestaartje)wetterskipfryslan(punt)nl.

## Bestanden delen via GitHub
Teams kunnen bestanden delen via een GitHub repository van Kennisnetwerk Data Science.    
Neem hiervoor contact op met Willy Tadema: w(punt)tadema(apestaartje)provinciegroningen(punt)nl.    
Er zijn al repo's voor [team 2](https://github.com/KennisnetwerkDataScience/teampje2) en [team 5](https://github.com/KennisnetwerkDataScience/team5).    

## Interessant links
Image recognition:
* [Image Segmentation with Tensorflow using CNNs and Conditional Random Fields](http://warmspringwinds.github.io/tensorflow/tf-slim/2016/12/18/image-segmentation-with-tensorflow-using-cnns-and-conditional-random-fields/)

Open data:
* [Open data portaal RUG](http://opendata.rug.nl/)
* [Nationaal Georegister](http://www.nationaalgeoregister.nl)
* [Publieke Dienstverlening op de Kaart (PDOK)](http://www.pdok.nl)
* [Actueel Hoogtebestand Nederland (AHN3)](https://www.pdok.nl/nl/ahn3-downloads)
* [Basisregistratie Grootschalige Topografie (BGT)](https://www.pdok.nl/nl/producten/pdok-downloads/download-basisregistratie-grootschalige-topografie)

Luchtfoto's en satellietbeelden:
* [Luchtfoto](https://www.pdok.nl/nl/producten/pdok-services/overzicht-urls/l) (alleen de 25 cm infrarood en RGB foto zijn open data)
* [Project beeldmateriaal](http://www.beeldmateriaal.nl/index.html)
* [Satellietportaal](https://www.spaceoffice.nl/nl/satellietdataportaal/)
* [Copernicus Open Access Hub](https://scihub.copernicus.eu)

MOOCs:
* [Deep Learning for Natural Language Processing](http://cs224d.stanford.edu/)
* [Machine Learning](https://www.coursera.org/learn/machine-learning)
* [Deep Learning for Self-Driving Cars](https://www.youtube.com/watch?v=1L0TKZQcUtA)
* [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
* [Deep Learning Nanodegree Program](https://eu.udacity.com/course/deep-learning-nanodegree--nd101)
* [Convolutional Neural Networks](https://www.coursera.org/learn/convolutional-neural-networks)
* [Convolutional Neural Networks for Visual Recognition](https://www.youtube.com/watch?v=vT1JzLTH4G4)

## Bijeenkomsten
Data: Maandag 26 maart, 9 april en maandag 23 april 2018.     
Aanvang: 16.00 uur.     
Einde: 20.30 uur.    
Catering: Er wordt gezorgd voor een hapje en een drankje.  

![1ste meetup - 27 maart 2018](/images/hackathon.JPG)
