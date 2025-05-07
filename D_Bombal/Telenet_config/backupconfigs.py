## This program is for backing up ip interface configs to txt doc for devices in 'myswitches'

import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account:  ")
password = getpass.getpass()

f = open('myswitches')

for IP in f:
    IP = IP.strip()
    print("Getting running config for Switch  " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
# Getting/saving running config
    tn.write(b'terminal length 0\n')
    tn.write(b'show run\n')
    tn.write(b'exit')

    readoutput = tn.read_all()
    saveoutput = open('switch' + HOST, 'w') ## HOST =  config IP interface
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write('\n')
    saveoutput.close