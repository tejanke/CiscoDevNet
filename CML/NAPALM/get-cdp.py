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
            inventory_item = line.rstrip().replace(' ', '').split(',')
            inventory[inventory_counter] = {
                "hostname": inventory_item[0],
                "driver": inventory_item[1],
                "ip": inventory_item[2],
                "username": inventory_item[3],
                "password": inventory_item[4]
            }
            inventory_counter += 1
    return inventory


def get_cdp(device_number, device):
    """Grab cdp variables"""
    print("Checking {}.".format(device['hostname']))
    driver = napalm.get_network_driver(device['driver'])
    if device['driver'] == 'asa':
        print("ASA does not support get_cdp.")
        device_cdp = {}
    elif device['hostname'] == 'edge-sw01':
        print("NAPALM requires a username to login.")
        device_cdp = {}
    elif device['driver'] == 'iosxr':
        print("iosxr not supported.")
        device_cdp = {}
    else:
        with driver(hostname=device['ip'], username=device['username'], \
            password=device['password'], optional_args= \
            {'secret': 'cisco'}) as conn:
                print("Connecting to {}.".format(device['ip']))
                commands = ['show cdp nei']
                device_cdp = conn.cli(commands)
    return device_cdp


main_inventory = get_inventory(inventory_file)
for device_number, device in main_inventory.items():
    device_cdp = get_cdp(device_number, device)
    if bool(device_cdp):
        print(yaml.dump(device_cdp))
        print(device_cdp)