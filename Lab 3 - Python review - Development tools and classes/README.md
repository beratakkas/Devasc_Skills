Lab 3 - Python review - Development tools and classes

 Part 1: Python Programming Review

 Lab netacad: Cisco DEVNET 1.3.3

 • Task preparation and implementation: DEVASC VM , Python, VS CODE

  Voer python3 in terminal voor in Python’s interactieve interpreter tegaan.
  Wiskundige uitvoering kun je al doen door bv. 2+3 te schrijven.
  Open VS Code maak een bestand aan en schrijf ‘Hello World!’ vervolgen run je dit en krijg je hetzelfde als uitvoer, je kunt dit ook in terminal doen door ‘python3 ~/labs/devnet-src/python/hello-world.py’
  • Integer – voor gehele getallen, zoals 1, 2, 3.
  • Float – voor decimalen getallen zoals 3.14159.
  • String – voor karakters, symbolen.
  • Boolean - data type dat juist of fout als waarde heeft.

  > groter dan
  < Kleiner dan
  == gelijk aan
  != niet gelijk aan
  >= groten dan of gelijk aan
  <= Kleiner dan of gelijk aan

  Variabelen maak je door Naam=waarde
  Voor een data type te geven aan waarde x=str(waarde)
  Een lijst maken met [] hostnames=["R1","R2","R3","S1","S2"]
  Dictionary met {} ipAddress={"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
   
  Create a script to collect personal information. 
  Zie LAB 3 personal-info.py
  Create an if/else function
  Zie LAB 3 if-vlan.py
  Create an if/elif/else function
  Zie LAB 3 if-acl.py
  For loop 
  for item in devices:
  if "R" in item:
  print(item)
  While Loop
  Zie LAB 3 while-loop.py
  Create a program that reads an external file.
  Zie LAB 3 file-access.py
  Create a script to allow the user to add devices.
  Zie LAB3 file-access-input.py

 • Task troubleshooting:
  -
 • Task verification:

  Zie LAB 3 foto’s en scripts



Part 2: Explore Python Development Tools
Lab netacad: Cisco DEVNET 3.1.12

 • Task preparation and implementation:

  DEVASC VM, Python
  Open terminal
  Python 3 enviroment maken: python3 -m venv devfun activeer de enviroment: source devfun/bin/activate
  pip3 freeze voor te zien dat er geen additionele Python pakketen zijn
  pip3 install requests voor de nodige pakketen te installeren 
  nadien weer pip3 freeze en je ziet de pakketen geïnstalleerd
  om de virtual enviroment de sluiten: deactivate
  ge terug in devfun
  zet de uitvoer van pip3 freeze in een bestand: pip3 freeze > requirements.txt
  deacvtivate
  maak een nieuw environment genaamd devnew en activeer
  gebruik volgende commande om de zelfde pakketen te installeren als in devfun:
  pip3 install -r requirements.txt
  pip3 freeze en je ziet ze geïnstalleerd

 • Task troubleshooting:
  -
 • Task verification:
   Zie LAB 3 foto’s 

Part 3: Explore Python Classes

Lab netacad: cisco DEVNET 3.4.6

 • Task preparation and implementation:

  DEVASC VM

  Een functie is een zelfstandig blok code dat wordt aangeroepen met een naam
  # Define the function
  def functionName:
   ...blocks of code...
  # Call the function
  functionName()

  Een methode kan niet zelfstandig worden opgeroepen, omdat het afhankelijk is van het object waarin het is gedefinieerd.

  Een functie:
  Zie lab 3 myCity.py
  Class met Methods:
  Zie lab 3 myLocation.py
  een klasse maken die de omtrek van een cirkel berekent en vervolgens de berekende waarde afdrukt:
  zie lab 3 circleClass.py

 • Task troubleshooting:
  -
 • Task verification:
  Zie LAB 3 foto’s en scripts
