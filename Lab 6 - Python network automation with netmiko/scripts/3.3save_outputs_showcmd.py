print("Connecting via SSH => save show command to multiple devices")
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

output_file = 'showoutput.txt'

with open(output_file, 'w') as file:
    for device in all_devices:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command("show ip interface g0/1")
        file.write(f"Output van {device['ip']}:\n\n")
        file.write(output)
        file.write('\n\n')

print(f"Output is opgeslagen in het bestand: {output_file}")
