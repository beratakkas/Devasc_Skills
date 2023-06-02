print("Connecting via SSH => config command to multiple devices")
from netmiko import ConnectHandler

switch3 = {
    'device_type': 'cisco_xe',
    'ip': '10.125.100.197',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin'
}

router3 = {
    'device_type': 'cisco_xe',
    'ip': '10.125.100.191',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin'
}

config_commands = [
    'interface g0/1',
    'description Test Interface',
    'no shutdown'
]

all_devices = [switch3, router3]

for device in all_devices:
    with ConnectHandler(**device) as net_connect:
        net_connect.enable()
        output = net_connect.send_config_set(config_commands)
        print(output)

        net_connect.disconnect()
