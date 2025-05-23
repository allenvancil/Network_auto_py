## Netmiko Part 4

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.84',
    'username' : 'david',
    'password' : 'cisco'
}

iosv_l2_s2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.85',
    'username' : 'david',
    'password' : 'cisco'
}

iosv_l2_s3 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.86',
    'username' : 'david',
    'password' : 'cisco'
}

with open('iosv_l2_cisco_design', 'r') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)