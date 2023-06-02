print("Connecting via SSH => Backup device configurations")
from netmiko import ConnectHandler

switch3 = {
    'device_type': 'cisco_xe',
    'ip': '10.125.100.197',
    'username': 'admin',
    'password': 'admin',
    "secret": "admin"
}

router3 = {
    'device_type': 'cisco_xe',
    'ip': '10.125.100.191',
    'username': 'admin',
    'password': 'admin',
    "secret": "admin"
}

all_devices = [switch3, router3]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    output = net_connect.send_command("show running-config")

    filename = f"{device['ip']}_config.txt"
    with open(filename, 'w') as file:
        file.write(output)

    print(f"Configuratie van apparaat {device['ip']} is opgeslagen in {filename}")
