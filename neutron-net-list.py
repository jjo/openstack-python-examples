#!/usr/bin/python
# openstack example python-let: neutron-net-list.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: GPLv3
# vim: si et sw=4 ts=4

import os
from neutronclient.v2_0 import client as neutron_client


def get_creds():
    # create a dictionary as e.g.: {'username': env['OS_USERNAME'], ...
    return {key: os.environ.get('OS_{}'.format(key.upper())) for key in
            ('auth_url', 'username', 'password', 'tenant_name', 'region_name')}
    return creds

creds = get_creds()
neutron_cli = neutron_client.Client(**creds)
# For each neutron network, print its id and value
for net in neutron_cli.list_networks().get('networks'):
    print net['id'], net['name']
