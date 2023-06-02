LAB 2 – EXPLORE REST APIs WITH API SIMULATOR AND POSTMAN

  LAB NETACAD : CISCO DEVNET 4.5.5-lab---explore-rest-apis-with-api-simulator-and-postman

  Part 1: Explore API Documentation Using the API Simulator 

    • Task preparation and implementation: 

    DEVASC VM, Postman
    Open de Chromium Web browser -> schrijf als URL library.demo.local -> klik rechtboven op Click here for API docs
    /api/list kun je klikken om de api list te verbergen. Het slot is voor als je wilt dat de API een token nodig heeft voor gebruik. Klik op GET/books het geeft een lijst of boeken terug in de school library. Duid application/json aan bij Response content type; Hiermee wordt de type van weergave bepaalt. De code 200 toont aan dat de API request is gelukt. Klik vervolgens op Try it out laat de vakjes leeg en klik op execute.
    • Curl: Met behulp van het curl-commando kun je toegang krijgen tot dezelfde informatie voor de /books API.
    • Request URL: Deze URL wordt gebruikt in het API-verzoek en kan worden gebruikt om dezelfde informatie op te vragen met behulp van curl, Postman en Python.
    • Code: Dit is de HTTP-responscode. Een code van 200 geeft een succesvolle oproep aan.
    • Response body: Een lijst van boeken in JSON-indeling.
    • Response headers: Informatie over de API die wordt teruggestuurd vanaf de server.
    In de Response body zie je een lijst van boeken in JSON-indeling: zie resultaat
    Plak de curl commando in een terminal 
    Ga terug naar GET-/books API kies bij parameters includeISBN true en execute hierdoor worden de boeken gelijst met hun ISBN. In de curl en request URL zie je dat ?includeISBN=true is bijgekomen.
    Klik op POST /loginViaBasic -> execute -> vul username cisco password Cisco123! Vervolgens krijg je een token. Klik boven op authorize plak de token hierin en klik weer Authorize en sluit het venster.
    Klik op POST/books om een boek toe te voegen -> content type op JSON -> try it out > verander de id titel en author -> execute en de boek wordt gemaakt.
    Lijst van boeken weergeven: GET/books -> try it out -> execute in de response body zie je de boek staan.
    Klik op GET/books{id} -> try it out -> vul 4 in als id parameter -> execute. E zo krijg je de specifike boek dat je wilt zien.
    Om eenn boek te verwijderen. Klik op DELETE/books{id} -> try it out -> vul 4 in als id parameter -> execute. 

    • Task troubleshooting:
    -
    • Task verification:
    Zie LAB 2 foto’s P1


  Part 2: Use Postman to Make API Calls to the API Simulator Document your findings in 3 steps:

    • Task preparation and implementation: 

    DEVASC VM, Postman
    Boeken listen met GET/books API: open Postamn -> klik op + om een request te creëeren -> laat het op GET -> ga terug naar school library API _> kopieer de request URL onder GET/books -> plak deze in postman waar URL staat -> klik op send 
    Token krijggen via POST/LoginViaBasic API: klik op + -> klik op GET en zet dit naaar POST -> kopieer de URL onder POST/LoginViaBasic -> plak deze in postman URL -> klik authorize -> type kies je basis Auth -> username cisco password Cisco123! -> send
    Boek toevoegen met POST/books API: klik + -> kopieer de url bij POST/books -> plak deze in postman URL -> type kies je API Key -> key vul je X-API-KEY in-> ga naar Post tab plak hier de token die je voorheen heb gekregen. Inderaan bij body klik je op raw -> klik tekst verander naar JSON -> vul de JSON object in voor boeken zolas eerdere opdracht -> send
    Additionele parameters GET/books: doe het zelfde als vorige opdracht GET/books -> klik op Params onder KEY vile je includeISBN in en Value true -> onder nieuwe key sortBy Value author -> send 

    • Task troubleshooting:
    -
    • Task verification:
    Zie LAB 2 foto’s P2

  Part 3: Use Python to Add 100 Books to the API Simulator 

    • Task preparation and implementation: 

    DEVASC VM, Visual Studio Code
    Open VS Code –> open folder labs/devnet-src/school-library -> klik in explorer op add100RandomBooks.py om het te openen -> zet interpreter en libraries in de script -> open terminal -> start python 3 -> voer volgende commandos uit om Faker te krijgen 
    >>> from faker import Faker
    >>> fake = Faker()
    >>> fake. catch_phrase(), isbn13(), en name().
    Run de script ( zie script LAB 2 script)
    • Task troubleshooting:
    -
    • Task verification:
    zie LAB 2 scripts
