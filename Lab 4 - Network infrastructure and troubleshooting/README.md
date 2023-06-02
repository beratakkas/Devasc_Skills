Lab 4 - Network Infrastructure and troubleshooting

	• Task preparation and implementation:

		Benodigde apparatuur Router en Switch

		Router: 
		Bij de router hebben we volgende onderdelen geconfigureerd.  Vlans,router on a stick, HSRP, OSPF, SSH, TFTP, een eigen DHCP pool. Beveiliging: wachtwoord voor toegang en de gencyrpteerd, login blokkeren na x aantal pogingen, lokale authenticatie voor de console en VTY-lijnen
		Switch: Vlans, trunkpoort, SSH, beveilinging: wachtwoord voor toegang en de gencyrpteerd, lokale authenticatie voor de console en VTY-lijnen

		Configuratie van TFTP-server afhalen:
		router: conf t
			   int g0/1
			   ip address 10.199.66.109 255.255.255.224
			no shutdown
		ex
		ip route 0.0.0.0 0.0.0.0 10.199.66.100
		Copy tftp running config
		  10.199.64.134
		  lab-ra09-c-r03-conf
		Na het kopiëren altijd de poorten die nodig zijn open zetten.
		crypto key generate rsa
		1024

		switch: conf t
		vlan 10
		int vlan 10 
		ip address 172.16.9.7 255.255.225.240
		exit
		int g0/1
		switchport mode trunk 
		switchport trunk allowed vlan 10
		no shutdown
		Copy tftp running config
		  10.199.64.134
		  lab-ra08-a-sw03-conf
		Na het kopiëren altijd de poorten die nodig zijn open zetten.

	• Task troubleshooting:
		na het kopiëren altijd de poorten die nodig zijn open zetten.
		bij de router na het kopiëren van config file nieuwe key maken.
		crypto key generate rsa
		1024

	• Task verification:
		De complete Running configuratie van beide apparaten vind je bij LAB 4 scripts.
