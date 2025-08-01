from netmiko import ConnectHandler

with open('command_file') as f:
    commands_to_send = f.read().splitlines()
    print(commands_to_send)

ios_devices = {
    'device_type' : 'cisco_ios', 
    'ip' : '192.168.122.72', 
    'username' : 'allen', 
    'password' : 'root',
}

all_devices = [ios_devices]
print('\nthis is all_devices\n')
print(all_devices)

# for devices in all_devices:
#     net_connetion = ConnectHandler(**devices)
#     output = net_connetion.send_config_set(commands_to_send)
#     print(output)