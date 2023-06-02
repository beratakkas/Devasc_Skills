print("Connecting via SSH => multiple show command")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="172.16.9.7",
    port="22",
    username="admin",
    password="admin"
    )
output1=sshCli.send_command("show ip interface g0/1")
output2=sshCli.send_command("show ip interface g0/2")
print(output1 +  "\n\n" + output2)