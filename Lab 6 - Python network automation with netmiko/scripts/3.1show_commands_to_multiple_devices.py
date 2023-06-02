print("Connecting via SSH => show command to multiple devices")
from netmiko import ConnectHandler

switch3 = {
    'device_type': 'cisco_xe',
    'ip': '10.125.100.197',
    'username': 'admin',
    'password': 'admin',
}

router3 = {
    'device_type': 'cisco_xe',
    'ip': '10.125.100.191',
    'username': 'admin',
    'password': 'admin',
}

all_devices = [switch3, router3]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip interface g0/1")
    print(output)
    net_connect.disconnect()
