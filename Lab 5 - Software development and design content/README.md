LAB 5 – Software Development and Design Content

  Part 1: Software Version Control with Git

  Lab netacad: Cisco DEVNET 3.3.11

    • Task preparation and implementation:
    DEVASCM VM

    Local repository user aanmaken
    git config --global user.name "SampleUser"
    git config --global user.email sample@example.com

    git init command om directory (git-intro) als Git repository 

    git status

    echo “…” > bestand.txt

    git add bestand.txt om bestand te stagen
    git commit -m “message” om bestand te commiten (veranderingen beheren)
    git log om alle commits te zien
    git diff <commit ID original> <ID latest> om verschil te zien ( id is de eerste 7 karakters)

    git branch naam om nieuwe branch te maken
    git checkout naam om van branch te switchen
    git log om alle commits te zien in branches
    git merge <branch naam> om <branch naam> te mengen met de branch waarin je zit
    git branch -d <branch-naam> om branch te verwijderen
    sed -i’s/voor/na bestand.txt om de VOOR tekst te veranderen met NA

    Point Git repository to GitHub repository. a. Use the git remote add command to add a Git URL as a remote alias.
    git remote add origin https://github.com/beratakkas/devasc-study-team.git 
    git remote –verbose
    git add bestand.txt
    git commit -m “…”
    git status komt working tree clean te staan
    git push origin master

    • Task troubleshooting:
    -
    • Task verification:
    Zie Lab 5 foto’s

  Part 2: Create a Python Unit Test

  Lab netacad: Cisco DEVNET 3.5.7

    • Task preparation and implementation:

    DEVASC VM

    Python3 -m unittest -h voor informatie 
    In dit gedeelte zal je unittest gebruiken om een functie te testen die een recursieve zoekopdracht uitvoert op een JSON-object. De functie geeft waarden terug die zijn getagd met een specifieke sleutel. Programmeurs moeten vaak dit soort bewerkingen uitvoeren op JSON-objecten die worden teruggegeven door API-oproepen.
    recursive_json_search.py: Dit script bevat de json_search() functie die we willen testen.
    test_data.py: Dit zijn de gegevens waar de json_search() functie naar zoekt.
    test_json_search.py: Dit is het bestand dat je zal aanmaken om de json_search() functie in het recursive_json_search.py script te testen.

    Bekijk test_data.py
    devasc@labvm:~/labs/devnet-src$ more unittest/test_data.py

    creëer json_search() function dat je gaat testen
    Open de ~/labs/devnet-src/unittest/recursive_json_search.py bestand en plak de code erin (Zie lab 5 script)
    Run deze -> het geeft een fout, komt omdat deze fout is gecodeert
    Hoe weten we of dan json_search() werkt
    Open test_data.py -> zoek de key issueSummary, deze toont aan dat er een fout is.

    Schrijf enkele unit tests om te controleren of de functie werkt zoals bedoeld.
    Open de ~ labs/devnet-src/unittest/test_json_search.py bestand ->import de unittest library -> voeg lijnen toe om functies die je test te importeren -> voeg json_search_test clas code toe -> voeg unittest.main() toe 
    ( Zie Lab 5 script)

    Run de test en zie de resultaten
    python3 test_json_search.py
    python3 -m unittest -v test_json_search

    corrigeer dee error in recursive_json_search.py
    verwijder ret_val=[]
    run opnieuw
    python3 -m unittest test_json_search
    Open the test_data.py file and search for issueSummary
      if you search for the value of key2, which is XY&^$#*@!1234%^&, you will only find it at the top where it is defined because it is not in the data JSON object.
    Investigate and correct the second error in the recursive_json_search.py script.  
      To resolve this issue, wrap the json_search() function with an outer function. Delete your existing json_search() function and replace with the code in LAB 5 ScriptsFile
      if you search for the value of key2, which is XY&^$#*@!1234%^&, you will only find it at the top where it is defined because it is not in the data JSON object.
    python3 -m unittest



    • Task troubleshooting:
    -
    • Task verification:
      Zie lab 5 scripts

  Part 3: Parse Different Data Types with Python

  Lab netacad: cisco DEVNET 3.6.6

    • Task preparation and implementation:
    DEVASC VM

    Ontleed XML in Python
    Script maken om XML data te ontleden
    Open de parsexml.py bestand in ~/labs/devnet-src/parsing directory
    Importer de ElementTree module in XML
    Zie Lab 5 script
    python3 parsexml.py

    Ontleed JSON in Python
    Script maken 
    Open de parsejson.py bestand in  ~/labs/devnet-src/parsing directory
    import the json and yaml libraries
    gebruik with statement en gebruik nadien json.load method, voeg een prtin statemnet toe
    python3 parsejson.py
    voeg print statement toe om token value te zien
    rerun python3 parsejson.py
    zie lab 5 script

    ontleed YAML in Python
    Open de parseyaml.py bestand in ~/labs/devnet-src/parsing directory.
    Gebruik python with statement om myfile.yamp te openen en zet de variabel name yaml_file gebruik nadien yaml.safe_load voeg pritn statement toe voeg print statement toe om token value te zien
    Run python3 parseyaml.py

    • Task troubleshooting:
    -
    • Task verification:
      Zie lab 5 scripts
