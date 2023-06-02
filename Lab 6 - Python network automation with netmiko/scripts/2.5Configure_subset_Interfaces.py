print("Connecting via SSH => Configure a subset of Interfaces")
from netmiko import ConnectHandler

switch3 = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.197',
    'username': 'admin',
    'password': 'admin',
    'secret':"admin"
}

router3 = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.191',
    'username': 'admin',
    'password': 'admin',
    'secret':"admin"
}

devices = [switch3, router3]

interfaces = ['GigabitEthernet0/1', 'GigabitEthernet0/2', 'GigabitEthernet0/3']

config_commands = [
    'description gelukt',
    'no shutdown',
]

for device in devices:
    with ConnectHandler(**device) as net_connect:
        net_connect.enable()

        for interface in interfaces:
            interface_commands = [f'interface {interface}']
            interface_commands.extend(config_commands)

            output = net_connect.send_config_set(interface_commands, exit_config_mode=False, enter_config_mode=False)

            print(f"Interface {interface} configuratie-uitvoer op {device['ip']}:")
            print(output)
