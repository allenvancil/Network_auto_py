from netmiko import ConnectHandler
import pprint
import pandas as pd

with open('command_file') as f:
    command_list = f.read().splitlines()

with open('device_file') as f:
    device_list = f.read().splitlines()
    print(device_list)
for devices in device_list:
    print("\nconnecting to Device " + devices + "\n")
    ip_of_device = devices
    ios_device = {
        "device_type" : "cisco_ios",
        "ip" : ip_of_device,
        "username" : "allen",
        "password" : "root",
    }

    df = pd.DataFrame(ios_device,)
    print(df)



    pprint.pprint(ios_device)
# net_connect = ConnectHandler(**ios_device)
# output = net_connect.send_config_set(command_list)
# print(output)