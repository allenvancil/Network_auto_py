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
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")

for n in range(2, 11):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")  #encode n, integer, as ascii text
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))