## From Quick Start 12 Backup network devs configs

import getpass
import telnetlib

user = input('input your Telenet username:')
password = getpass.getpass()

f = open('myswitches')
## show the configuration of Switches

for IP in f:
    IP = IP.strip()
    print('get running config from switch ' + (IP)) 
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    ## terminal length 0, show entire length of running config

    tn.write(b'terminal length 0\n')
    tn.write(b'show run \n')
    tn.write(b'exit\n')

    readoutput = tn.read_all()
    saveoutput = open('switch' + HOST, 'w')
    saveoutput = tn.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close
