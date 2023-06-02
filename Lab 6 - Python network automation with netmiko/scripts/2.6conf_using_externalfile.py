print("Connecting via SSH => Send device configuration using an external file")
from netmiko import ConnectHandler

switch3 = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.197',
    'username': 'admin',
    'password': 'admin',
    'secret':'admin'
}

router3 = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.191',
    'username': 'admin',
    'password': 'admin',
    'secret':'admin'
}

devices = [switch3, router3]

config_file = 'config_file.txt'

for device in devices:
    with ConnectHandler(**device) as net_connect:
        net_connect.enable()

        output = net_connect.send_config_from_file(config_file)

        print(f"Configuratie-uitvoer op {device['ip']}:")
        print(output)
