from netmiko import Netmiko
from netmiko import ConnectHandler
from datetime import datetime

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

router3 = {
    'device_type': 'cisco_ios',
    'ip': '10.1.0.3',
    'username': 'test',
    'password': 'test123',
     'verbose': True
}

all_devices = [router1, router2, router3]

start_time = datetime.now()
print(start_time)
for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    net_connect.enable()
    net_connect.send_config_from_file('router1.txt')
    net_connect.disconnect()
end_time = datetime.now()
print(end_time)
total_time = end_time - start_time
print(total_time)


start_time = datetime.now()
print(start_time)
for a_device1 in all_devices:
    net_connect_show = ConnectHandler(**a_device1)
    output1 = net_connect_show.send_command('show ip ospf neighbor')
    print(f"\n\n-----{a_device['ip']}----\n\n")
    print(output1)
    net_connect.disconnect()
end_time = datetime.now()
print(end_time)
total_time = end_time - start_time
print(total_time)
