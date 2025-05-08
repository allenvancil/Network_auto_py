## Netmiko Part 4

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.72',
    'username' : 'david',
    'password' : 'cisco'
}

iosv_l2_s2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.82',
    'username' : 'david',
    'password' : 'cisco'
}

iosv_l2_s3 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.83',
    'username' : 'david',
    'password' : 'cisco'
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3] # each entry is an index in list

for device in all_devices:
    net_connection = ConnectHandler(**device) # connect w/ ssh
## **device passes key value pairs for dict 
##   e.g. device_type='cisco_ios', host='192.168.1.1', username='admin', password='password123'

    # sent list of config commands and print out to switch
    for n in range(2,21):
        print("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connection.send_config_set(config_commands)
        print(output)
