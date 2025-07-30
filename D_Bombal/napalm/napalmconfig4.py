import json
from napalm import get_network_driver

dev_list = ['192.168.122.72', 
            '192.168.122.73']

for ipaddress in dev_list:
    print('connecting  to ' + str(ipaddress))
    driver = get_network_driver('ios')
    iosv = driver(ipaddress, 'allen', 'root')
    iosv.open()

    ## NEED TO GET ACL1.CFG FILE

    iosv.load_merge_candidate(filename='ACL1.cfg')
    diffs = iosv.commit_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No ACL changes required')
        iosv.discard_config()

    ## GET OSPF.CFG FILE

    iosv.load_merge_candidate(filename='ospf1.cfg')

    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print("No OSPF changes required")
        iosv.discard_config()
    iosv.close()
