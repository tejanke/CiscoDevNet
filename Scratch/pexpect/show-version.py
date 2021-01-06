#!/usr/bin/python3

import pexpect

ip = input("Enter device IP: ")
#user = input("Enter username: ")
#password = input("Enter password to connect to {}: ".format(ip))
conn = "ssh " + ip
print(conn)
child = pexpect.spawn(conn)
child.expect("Username:")