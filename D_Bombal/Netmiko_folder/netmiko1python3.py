## Netmiko Parrt 3

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.72',
    'username' : 'david',
    'password' : 'cisco',
}

net_connection = ConnectHandler(**iosv_l2) 
#output of show ip int brief
output = net_connection.send_command('show ip int brief')
print(output)

# list of configuration commands
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connection.send_config_set(config_commands)
print(output)

# sent list of config commands and print out to switch
for n in range(2,21):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connection.send_config_set(config_commands)
    print(output)
