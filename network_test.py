from netmiko import Netmiko

connection = Netmiko(host='192.168.10.2', username='test', password='test123', device_type='cisco_ios')

output = connection.send_command('show ip int brief')
print(output)
#connection.send_command('enable')
#connection.send_command('test1234')

#output = connection.send_command('show version')
#print(output)
connection.disconnect()

connection = Netmiko(host='10.0.0.2', username='test', password='test123', device_type='cisco_ios')

output = connection.send_command('show version | in IOS')
print(output)
#connection.send_command('enable')
#connection.send_command('test1234')

#output = connection.send_command('show version')
#print(output)
connection.disconnect()

