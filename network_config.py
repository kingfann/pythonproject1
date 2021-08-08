from netmiko import Netmiko
from netmiko import ConnectHandler
from datetime import datetime

router1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.10.2',
    'username': 'test',
    'password': 'test123',
    'port': '22',
    'secret': 'test1234',
    'verbose': True
}

router2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.2',
    'username': 'test',
    'password': 'test123',
    'port': '22',
    'secret': 'test1234',
    'verbose': True
}

start_time = datetime.now()
print(start_time)

connection = ConnectHandler(**router2)
connection.enable()
commands = ['int fa0/1', 'no shutdown', 'ip address 10.1.0.2 255.255.255.0', 'description**dummy test interface***']
connection.send_config_set(commands)

output = connection.send_command_expect('write memory')
print(output)
output1 = connection.send_command('show run int fa0/1')
print(output1)
connection.disconnect()
