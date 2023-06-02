Lab 1 - Python Experiments

	1.1 Install different tools/packages on Ubuntu DEVASC-LABVM:

		• Task preparation and implementation: 

		DEVASC VM

		- Python 3.8 and PIP
		- Visual Studio Code
		- Jupyter Notebook
		- Python IDLE
		sudo apt update
		-Python 3.8 install
			-python3.8 version (om huidige versie te tonen)
			-sudo apt install python3.8 (voor installatie of update)
		-PIP install
			-pip3 –version
			-sudo apt install python3-pip (voor installatie of update)
		- Visual Studio Code
			-code –version
		- Jupyter Notebook
			-pip install notebook (of install jupyter)
			-jupyter notebook --version
		- Python IDLE
			-sudo apt install idle3

		• Task troubleshooting:
		-
		• Task verification:

		Zie Lab 1 foto’s
		-Python 3.8 install
			-python3.8 version (om huidige versie te tonen)
		-PIP install
			-pip3 –version
		- Visual Studio Code
			-code –version
		- Jupyter Notebook
			-jupyter notebook –version
		- Python IDLE

	1.2 Run geopy and timedate Python Scipts on the DEVASC-LABVM using the tools above (1.1):

		• Task preparation and implementation: 

		Zie lab 1 scripts
		- timedate.py 
		- geopy-geocoders_location.py
		- location.py

		In VS code
		1.	Geef de folder mee waarin je  wilt werken
		2.	Klik op het plusje maak nieuwe file
		3.	Plak hierin je code
		4.	Run
		In jupyter
		1.	Open Jupyter notebook (opent website)
		2.	Kies de folder 
		3.	Klik rechtsboven op nieuw  pyhton3 (lpykernel)
		4.	Plak je code 
		5.	run

		• Task troubleshooting:

		- timedate.py
			ModuleNotFoundError: No module named “geopy”
			Oplossing: pip install geopy
			ModuleNotFoundError: No module named “folium”
			Oplossing: pip install folium
		- geopy-geocoders_location.py
		Map wordt niet getoont 
		Oplossing: schrijf onderaan de script in een nieuwe lijn het woord: map

		• Task verification:

		Zie  Lab 1 foto’s
		- timedate.py	
		- geopy-geocoders_location.py via jupyter
		- location.py


	1.3 Install different tools/packages on Windows OS (deep dive exercise) ++

		• Task preparation and implementation:

		- Python 3.8 and PIP
		Download Python 3.8 installatieprogramma voor Windows vanuit de website van Python. Tijdens de installatie moet je de optie PIP installeren selecteren.
		- Visual Studio Code
		Download Visual Studio Code installatie voor Windows via de website van  VisualStudio. Voer de installatie uit.
		- Jupyter Notebook
		Pip install jupyter commando uitvoerin in opdrachtprompt.
		- Python IDLE
		Bij het downloaden van Python 3.8 heb je de idle ook.

		• Task troubleshooting:
		-
		• Task verification:

		1.4 Install different tools/packages on Ubuntu 22.04.01 LTS (deep dive exercise) ++

		• Task preparation and implementation:

		- Python 3.8 and PIP
		sudo apt update
		sudo apt install python3.8 python3-pip

		- Visual Studio Code
		sudo apt install software-properties-common apt-transport-https wget -y
		wget -O- https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor | sudo tee /usr/share/keyrings/vscode.gpg
		echo deb [arch=amd64 signed-by=/usr/share/keyrings/vscode.gpg] https://packages.microsoft.com/repos/vscode stable main | sudo tee /etc/apt/sources.list.d/vscode.list
		sudo apt update
		sudo apt install code

		- Jupyter Notebook
		sudo pip3 install --upgrade pip
		sudo pip3 install virtualenv
		mkdir jupy
		cd jupy
		virtualenv jup_notebook
		source jup_notebook/bin/activate
		pip3 install jupyter
		Jupyter notebook

		- Python IDLE
		sudo apt update
		sudo apt install idle3

		• Task troubleshooting:
		-
		• Task verification
