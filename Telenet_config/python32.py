import getpass
import telnetlib

HOST = "192.168.122.71"
user = input("Enter your Telnet username:  ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")  # will enter username input from above
tn.write(user.encode('ascii') + b"\n")  # will write username into terminal

# if password config will enter
if password:
    tn.read_until(b"Password: ")  #  terminal password prompt
    tn.write(password.encode('ascii') + b"\n")  # enter password

## enter commands, be sure to try manually first
tn.write(b"enable\n")  # cisco command
tn.write(b"cisco\n")  # enable password to enter "cisco"
tn.write(b"conf t\n")  # conf t command into terminal
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN_3\n")
tn.write(b"vlan 4\n")
tn.write(b"name Python_VLAN_4\n")
tn.write(b"vlan 5\n")
tn.write(b"name Python_VLAN_5\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))