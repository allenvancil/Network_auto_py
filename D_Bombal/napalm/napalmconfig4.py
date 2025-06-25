import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'allen', 'root')
iosvl2.open()

print('accessing 192.168.122.72\n')
iosvl2.load_merge_candidate(filename='ACL1.cfg')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No changes required.')
    iosvl2.discard_config()

iosvl2.close()