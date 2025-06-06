from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.72',
    'username' : 'allen',
    'password' : 'root'
}

iosv_l2_s2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.82',
    'username' : 'allen',
    'password' : 'root'
}

iosv_l2_s3 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.83',
    'username' : 'allen',
    'password' : 'root'
}

iosv_l2_s4 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.84',
    'username' : 'allen',
    'password' : 'root'
}

iosv_l2_s5 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.85',
    'username' : 'allen',
    'password' : 'root'
}

iosv_l2_s6 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.86',
    'username' : 'allen',
    'password' : 'root'
}

# with open('iosv_l2_cisco_design', 'r') as f:
#     lines = f.read().splitlines()
# print(lines)

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]


print(all_devices[2]['ip'])
# for devices in all_devices:
#     net_connect = ConnectHandler(**devices)
#     output = net_connect.send_config_set(lines)
#     print(output)