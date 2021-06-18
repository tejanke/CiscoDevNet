# https://napalm.readthedocs.io/en/latest/support/index.html
# https://buildmedia.readthedocs.org/media/pdf/napalm/latest/napalm.pdf

import napalm
import sys
import os
import pprint
import yaml

inventory_file = "inventory.txt"

def get_inventory(inventory_file):
    """Create inventory"""
    inventory = {}
    with open(inventory_file, 'r') as file:
        inventory_counter = 0
        for line in file:
            inventory_item = line.rstrip().replace(' ','').split(',')
            inventory[inventory_counter] = {
                    "hostname" : inventory_item[0],
                    "driver" : inventory_item[1],
                    "ip" : inventory_item[2],
                    "username" : inventory_item[3],
                    "password" : inventory_item[4]
                }
            inventory_counter += 1
    return inventory

def get_environment(device_number, device):
    """Grab environment variables"""
    print("Opening a connection to {} at {}.".format(device['hostname'], \
        device['ip']))
    driver = napalm.get_network_driver(device['driver'])
    if device['driver'] != 'asa':
        with driver(hostname = device['ip'], username = device['username'], \
            password = device['password'], optional_args = \
            {'secret' : 'cisco'}) as conn:
                device_environment = conn.get_environment()
    else:
        print("\tget_environment not supported")
        device_environment = {}
    return device_environment

main_inventory = get_inventory(inventory_file)
for device_number, device in main_inventory.items():
    device_environment = get_environment(device_number, device)
    print(yaml.dump(device_environment))