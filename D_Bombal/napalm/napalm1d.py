from napalm import get_network_driver
import json


driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'david', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print(json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_interfaces()
print(json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosvl2.get_interfaces_counters()
print(json.dumps(ios_output, sort_keys=True, indent=4))

iosvl2.close()