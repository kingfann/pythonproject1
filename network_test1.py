from netmiko import Netmiko
from netmiko import ConnectHandler



router1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.2',
    'username': 'test',
    'password': 'test123',
#     'port': '22',
    'secret': 'test1234',
    'verbose': True
}

router2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.2',
    'username': 'test',
    'password': 'test123',
#     'port': '22',
    'secret': 'test1234',
    'verbose': True
}


connection = ConnectHandler(**router1)
#output = connection.send_command('show ip int brief')
#print(output)
prompt = connection.find_prompt()
print(prompt)
if '>' in prompt:
    connection.enable()

output1 = connection.send_command('show run | in hostname')
print(output1)
connection.disconnect()

connection1 = ConnectHandler(**router2)
prompt1 = connection1.find_prompt()
print(prompt1)
if '>' in prompt1:
    connection1.enable()

output2 = connection1.send_command('show run | in username')
print(output2)

mode = connection1.check_config_mode()
print(mode)
if not mode:
    connection1.config_mode()

mode = connection1.check_config_mode()
print(mode)
#output = connection1.send_command('username test1 password test123\n')
connection.disconnect()
