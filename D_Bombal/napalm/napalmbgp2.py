import json
from napalm import get_network_driver

bgplist = ['192.168.122.72', 
           '192.168.122.73']

for ip_address in bgplist:
    print('Connecting to ' + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'allen', 'root')
    iosv_router.open()
    bgp_neighbors = iosv_router.get_bgp_neighbors()
    print(json.dumps(bgp_neighbors, indent=4))
    iosv_router.close()