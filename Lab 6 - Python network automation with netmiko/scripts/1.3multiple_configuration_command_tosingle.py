print("Connecting via SSH => multiple config command")
from netmiko import ConnectHandler
cisco_Switch={
    "device_type": "cisco_ios",
    "host":"10.125.100.197",
    "port":"22",
    "username":"admin",
    "password":"admin",
    "secret":"admin"
}

config_commands = [
    'interface g0/1',
    'description Test Interface',
    'no shutdown'
]

with ConnectHandler(**cisco_Switch) as net_connect:

    net_connect.enable()
    output = net_connect.send_config_set(config_commands)

    print (output)
    net_connect.disconnect()
 