print("Connecting via SSH => single show command")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="10.125.100.197",
    port="22",
    username="admin",
    password="admin"
    )
output=sshCli.send_command("show ip interface brief")
print(output)
