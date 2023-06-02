print("Connecting via SSH =>  show command to multiple devices")
from netmiko import ConnectHandler
switch3 = {
	'device_type': 'cisco_ios',
	'ip': '10.125.100.197',
	'username': 'admin',
	'password': 'admin',
}

router3= {
	'device_type': 'cisco_ios',
	'ip': '10.125.100.191',
	'username': 'admin',
	'password': 'admin',
}

all_devices = [switch3, router3]

for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	output=net_connect.send_command("show ip interface g0/1")
	print(output)