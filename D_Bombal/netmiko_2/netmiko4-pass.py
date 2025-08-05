from getpass import getpass
from netmiko import ConnectHandler

username = input(r'Enter your SSH username:  ')
password = getpass()

with open('command_file') as f:
    command_list = f.read().splitlines()

with open('device_file') as f:
    device_list = f.read().splitlines()

for devices in device_list:
    print("Connecting to device ... " + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type' : 'cisco_ios',
        'ip' : ip_address_of_device,
        'username' : username,
        'password' : password
    }

net_connect = ConnectHandler(**ios_device)
output = net_connect.send_config_set(command_list)
print(output)