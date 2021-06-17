# https://napalm.readthedocs.io/en/latest/support/index.html

import napalm
import sys
import os
import pprint
import yaml

inventory_file = "inventory.txt"
main_inventory = {}

""" driver = napalm.get_network_driver("ios")
device = driver(hostname="10.10.20.181", username="cisco", password="cisco")
device.open()
device_environment = device.get_environment()
device_interfaces = device.get_interfaces()
device_arp_table = device.get_arp_table()
device.close()
print(device_environment)
print(device_interfaces)
print(device_arp_table) """

with open(inventory_file, 'r') as file:
    inventory_counter = 0
    for line in file:
        inventory_item = line.rstrip().replace(' ','').split(',')
        main_inventory[inventory_counter] = {
            "hostname" : inventory_item[0],
            "driver" : inventory_item[1],
            "ip" : inventory_item[2],
            "username" : inventory_item[3],
            "password" : inventory_item[4]
        }
        inventory_counter += 1

print(yaml.dump(main_inventory))