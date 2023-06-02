from netmiko import ConnectHandler

switch3 = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.197',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin'
}

router3 = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.191',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin'
}

devices = [switch3, router3]

interface = 'GigabitEthernet0/1'
config_command = 'no shutdown'

for device in devices:
    with ConnectHandler(**device) as net_connect:
        net_connect.enable()

        output = net_connect.send_command(f"show running-config interface {interface}")

        if 'no shutdown' not in output:
            config_commands = [
                f"interface {interface}",
                config_command
            ]
            output = net_connect.send_config_set(config_commands)
            print(f"Interface {interface} on device {device['ip']} has been configured with 'no shutdown'")
        else:
            print(f"Interface {interface} on device {device['ip']} is already in 'no shutdown' state")
