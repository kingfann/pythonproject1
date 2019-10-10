import math
import netmiko
print('pi is', math.pi)

f = open('c:/users/Mohamed Sadath/Desktop/network_automation/files/router.txt', 'r')
content = f.read(11)
print(content)
content = f.read(3)

print(content)
print(f.tell())
f.seek(15)
content = f.read(10)
print(content)
print(f.closed)
f.close()
print(f.closed)

with open('c:/users/Mohamed Sadath/Desktop/network_automation/files/router.txt') as file:
    my_list = file.read().splitlines()
    print(my_list)

with open('c:/users/Mohamed Sadath/Desktop/network_automation/files/router.txt') as file:
    my_list = file.read()
    print(my_list)

with open('c:/users/Mohamed sadath/Desktop/network_automation/files/router.txt') as file:
    for line in file    :
        print(line, end='')

with open('files/router1.txt', 'a') as file:
    file.write('this is the new line\n')

with open('files/router1.txt', 'r') as file:
    my_list = file.read()
    print(my_list)
