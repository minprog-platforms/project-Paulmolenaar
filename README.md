# Programmeerproject Paul Molenaar

# Project: Thuiswerkmeubilair

### Beschrijving

Thuiswerkmeubels.nl biedt de gebruiker een flexibele, duurzame en betaalbare thuiswerkmeubilair verhuurdienst aan. De gebruiker dient de beschikbare ruimte voor de meubels (afmetingen) op te geven. Vervolgens geeft de website  een selectie met producten die in de beschikbare ruimte passen en dat moment beschikbaar zijn. De gebruiker kan vervolgens de producten toevoegen aan zijn winkelwagen en naar de betaalpagina navigeren. 

Op de betaalpagina dient de gebruiker zijn locatie op te geven. Aan de hand van de locatie wordt middels een API de afstand berekend tussen het magazijn (gestationeerd in Utrecht) en de opgegeven locatie. Op basis van deze afstand wordt een transport/verzendkosten component toegevoegd tijdens de betaalprocedure.
 

#### Datasets
* Een zelf opgemaakte data-set van thuiswerkmeubilair. Hier bij wordt de afmeting, afbeelding, prijs, beschikbaarheid en locatie opgeslagen.

#### Features
* Een landingpage waarbij de kernwaarden van het bedrijf uiteengezet worden. 
* Overzicht van het gehele assortiment meubels die op dat moment beschikbaar zijn.
* Een samenstel pagina, waarbij de afmetingen van de beschikbare ruimte ingevoerd dienen te worden. Op basis van deze afmetingen worden beschikbare producten uiteengezet, die vervolgens toegevoegd kunnen worden aan de winkelwagen. 
* Op het moment dat er een product gekozen wordt, wordt daarmee de beschikbare ruimte gereduceerd. Dit wordt weergeven middels het vollopen van de plattegrond. 
* Een betaalpagina waarbij de geselecteerde winkelwagen-producten afgerekend dienen te worden. Middels de opgegeven locatie worden de transportkosten berekend.
* Pagina met het overzicht van één specifieke meubel met diens specificaties.
* Een 'over ons' pagina waarbij het team wordt geïntroduceerd.
* Een registratie en inlog systeem.

#### Screenshots relevante pagina's
<img src="https://github.com/minprog-platforms/project-Paulmolenaar/blob/main/meubels/static/meubels/images/Samenstel_pagina.PNG" width=50% height=50%>
<img src="https://github.com/minprog-platforms/project-Paulmolenaar/blob/main/meubels/static/meubels/images/Bestel_pagina.PNG" width=50% height=50%>

#### Potential features:
* Marktplaats idee dat er tevens in tweede hands meubels 'gehandeld' kan worden.
* Klachten verwerken.
* Het vroegtijdig retourneren van de meubels.

#### Similar webapps
* Skepp.nl: Een bedrijf die de thuiswerkmeubilar met name aanbiedt aan bedrijven. Het voorziet van een meubilair voor de gehele thuiswerkplek.
* Flexitrentdistribution.com: Een bedrijf die zowel meubilair als apparatuur aanbiedt. 

#### Hardest parts
* Het bepalen van geschatte transportkosten van de meubel op basis van de locatie van het product en de user. 
* Het genereren van de mogelijke meubels op basis van de kamerafmetingen die de gebruiker opgeeft.
* Het gebruik van bootstrap in de styling.

#### Acknowledgements
De afbeeldingen van de homepagina zijn afkomstig van onderstaande pagina's en (indien nodig) bijgewerkt in paint.net.
* https://dnob.nl/wp-content/uploads/2021/12/Kantoor-inrichten-doe-je-met-de-juiste-meubels-780x470.jpeg;
* https://thomas.gaspersz.nl/thuiskantoor-inspiratie-werkkamer-inrichten/
* https://www.in-lease.com/nl

Verder wil ik een speciaal dankwoord uitspreken voor de volgende websites/kanalen:
* Het YouTube kanaal 'ROOTs Technology', waarbij uitgelegd werd  hoe je middels element inspecteren direct de layout van de website kunt wijzigen.
* www.W3Schools.com, die mij enorm op weg hebben  geholpen met bootstrapping in CSS. 
* www.positionstack.com voor het beschikbaar stellen voor de API locatie bepaler. 

#### Copyrights
Alle rechten zijn voorbehouden. Niets van de op deze website gepubliceerde code mag worden verveelvoudigd, opgeslagen in een geautomatiseerd gegevensbestand en/of openbaar worden gemaakt, in enige vorm of op enige wijze zonder uitdrukkelijke voorafgaande toestemming van Paul Molenaar.

