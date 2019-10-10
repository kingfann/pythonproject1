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
##add the extra line
router3 = {
     'device_type': 'cisco_ios',
    'ip': '10.1.0.3',
    'username': 'test',
    'password': 'test123',
#     'port': '22',
    'secret': 'test1234',
    'verbose': True
}
all_devices = [router1, router2]

start_time = datetime.now()
print(start_time)
for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    
#   output_arp = net_connect.send_command('show ip arp')
#    output_route = net_connect.send_command('show ip route')
    output_showipintbrief = net_connect.send_command('show ip int brief')
#    print(f"\n\n------------Device {a_device['ip']}-show ip arp------\n\n")
#    print(output_arp)
#    print(f"\n\n------------Device {a_device['ip']}-show ip route------\n\n")
#    print(output_route)
    print(f"\n\n----------Device {a_device['ip']}-show ip int brief ----\n\n")
    print(output_showipintbrief)
    print(f"\n\n------------END-----------")
    net_connect.disconnect()
end_time = datetime.now()
print(end_time)
total_time = end_time - start_time
print(total_time)

#connection = ConnectHandler(**router2)
#connection.enable()
#commands = ['int fa0/1', 'no shutdown', 'ip address 10.1.0.2 255.255.255.0', 'description**dummy test interface***']
#connection.send_config_set(commands)

#output = connection.send_command_expect('write memory')
#print(output)
#connection.disconnect()
