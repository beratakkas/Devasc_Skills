from netmiko import ConnectHandler

switch3 = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.197',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin',
    
}

router3 = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.191',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin',
    
}

devices = [switch3, router3]

def collect_device_info(device):
    with ConnectHandler(**device) as net_connect:
        net_connect.enable()

        hostname = net_connect.send_command('show running-config | include hostname')
        interfaces = net_connect.send_command('show interfaces')
        routing_table = net_connect.send_command('show ip route')

        
        report = f"Device: {device['name']} ({device['ip']})\n"
        report += f"Hostname: {hostname}\n\n"
        report += "Interfaces:\n"
        report += interfaces + "\n\n"
        report += "Routing Table:\n"
        report += routing_table + "\n"

        return report


print("Connecting via SSH => Collecting device information")

for device in devices:
    report = collect_device_info(device)
    print(report)
    