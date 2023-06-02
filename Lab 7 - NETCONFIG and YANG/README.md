• Lab 7 - NETCONFIG and YANG

• Part 1: Install the CSR1000v VM

Lab netacad: Cisco DEVNET 7.0.3

• Task preparation and implementation:

Een devasc VM
VMware voor nieuwe VM
CSR1000v_for_VMware.ova bestand
Csr1000v_universalk9.16.09.05.iso bestand
• Task troubleshooting:
-
• Task verification:
Zie Lab 7 foto’s


• Part 2: Explore YANG Models

Lab netacad: Cisco DEVNET 8.3.5

• Task preparation and implementation:

DEVASC VM
Mkdir pyang
Cd pyang
Wget wget https://raw.githubusercontent.com/YangModels/yang/master/vendor/cisco/xe/1693/ietf-interfaces.yang

• Task troubleshooting:
-
• Task verification:
Zie Lab 7 foto’s

• Part 3: Use NETCONF to Access an IOS XE Device

Lab netacad: cisco DEVNET 8.3.6

• Task preparation and implementation:

DEVASC VM
CSR1000v VM
SSH connective tussen beide
SSH sessie met specifieke poort en netconf als subsysteem
ssh cisco@192.168.56.101 -p 830 -s Netconf
NETCONF sessie beëindigen :
<rpc message-id="9999999" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<close-session />
</rpc>

Ncclient op DEVASCVM
ncclient-netconf.py bestand maken met volgende script:
m = manager.connect(
 host="192.168.56.101",
 port=830,
 username="cisco",
 password="cisco123!",
hostkey_verify=False
 ) ’’’
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
 print(capability)
’’’

Voeg onderstaande toe om configuratie te krijgen van CSR1000v:
netconf_reply = m.get_config(source="running")
print(netconf_reply)
om een leesbare XML te krijgen verander 
print(netconf_reply) naar print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
Voeg een filter toe om specifieke data terug te krijgen:
netconf_filter = """
<filter>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

Voeg onderstaande toe om configuratie aan te passen en als het gelukt is OK geeft:
netconf_hostname = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>CSR1kv</hostname>
 </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
voeg onderstaande toe om een nieuwe loopback interface te maken:
netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>My first NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.1.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

• Task troubleshooting:
-
• Task verification:
Zie Lab 7 foto’s


• Part 4: Use RESTCONF to Access an IOS XE Device

Lab netacad: cisco DEVNET 8.3.7

• Task preparation and implementation:

DEVASC en CSR1000v VM met ssh connective
postman
Volgende deamons runnend zijn: confd, nesd, syncfd, dmiauthd, nginx, ndbmand, pubd
Activeren RESTCONF: configure terminal
			Restconf
Activeren https service: configure terminal
CSR1kv(config)# ip http secure-server
CSR1kv(config)# ip http authentication local
Disable SSL certification verification:
 Open Postman Click File > Settings -> onder de General tab, zet SSL certificate verification naar OFF.
Open een Get Request -> type de IP van CSR1kv in het vak waar URL staat
Ga naar de Authorization tab -> kies basic auth vul de username cisco en wachtwoord cisco123! In -> ga naar Headers tab daar zie je de Authorization Key -> voeg onderaan in de Key vak Content-Type en bij Value application/yang-data+json hierdoor verzend postmann JSON data naar CSR1kv -> daaronder z-schrijf je bij Key Accept en Value application/yang-data+json -> klik op Send en je ziet een JSON response
Gebruik GET Request voor info over alle interfaces van CSR1kv:
Dubplicate de vorige Get tab -> voeg data/ietf-interfaces:interfaces toe achetraan de URL -> klik Send 
Voeg interface=GigabitEthernet1 toe achter de URL en klik Send voor info over specifieke interface
Postman voor PUT Request:
Dupliceer de vorige Get request -> zet PUT i.p.v. GET -> voor de achter de URL interface= schrijf je =Loopback1 ->klik op Body endan RAW voeg onderstaan script toe om een Loopback te creëeren. De interface moet gezet worden naar softwareLoopback.
{
      "ietf-interfaces:interface": {
         "name": "Loopback1",
      "description": "My first RESTCONF loopback",
      "type": "iana-if-type:softwareLoopback",
      "enabled": true,
      "ietf-ip:ipv4": {
          "address": [
 {
    "ip": "10.1.1.1",
                  "netmask": "255.255.255.0"
 	}
        ]
    },
    "ietf-ip:ipv6": {}
  }
} 
Python script om GET request te verzenden
Open VS Code ga naar devnet-src open een terminal en maak een subdirectory ‘restconf’ -> maak een nieuwe file onder restconf genaamd restconf-get.py zet de volgende erin voor nodige modules en SSL certificaat waarschuwingen uitschakelen.
import json
import requests
requests.packages.urllib3.disable_warnings()
creëer een variebale api_url
api_url = https://192.168.229.128/restconf/data/ietf-interfaces:interfaces
maak een dictionary genaamd ‘headers’ dat keys heeft voor Accept en Content-type.
headers = { "Accept": "application/yang-data+json",
 	      "Content-type":"application/yang-data+json"
 } maak een Phyton tuple variabele dat 2 keys nodig heeft voor authenticatie username en password.
basicauth = ("cisco", "cisco123!")
een HTTP GET request maken naar de RESTCONF API op CSR1kv
	resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
	print(resp) en run deze.
Voor JSON formaat te krijgen voeg onderstaande toe
response_json = resp.json()
print(response_json)
om het te verfijnen vervang de print(response_json) door
print(json.dumps(response_json, indent=4))
Een Python script voor PUT request
Maak een nieuwe file
Importeer modules json, request -> maak een dictionary dat 2 keys heft voor Accept en Content-type -> maak een python tuple  variabele -> maak een dictionary variabele dat YANG data houdt die nodig is om een Loopback interface te maken -> maak een variabele dat HTTP PUT requeqt stuurt naar de RESTCONF -> we voegen code toe dat de response behandelt, als het een HTTP succes bericht is komt status ok te staan de rest wordt als error weergeven.

• Task troubleshooting:
Het kan zijn dat je bij een specifieke interface geen ipv4 addres ziet. Dit komt omdat dhcp gegeven is. Creëer een nieuwe interface met zelfde ip address in de interface. Klik vervolgens opnieuw op Send en nu zie je wel een IP address.

• Task verification:
Zie Lab 7 foto’s
