#!/usr/bin/python
# openstack example python-let: nova-list.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: GPLv3
# vim: si et sw=4 ts=4

import os
from novaclient import client as nova_client


def get_creds():
    # create a dictionary as e.g.: {'username': env['OS_USERNAME'], ...
    return {key: os.environ.get('OS_{}'.format(key.upper())) for key in
            ('auth_url', 'username', 'password', 'tenant_name', 'region_name')}
    return creds

creds = get_creds()
nova_cli = nova_client.Client(2,
                              creds['username'], creds['password'],
                              creds['tenant_name'], creds['auth_url'],
                              region_name=creds['region_name'])
# For each instance, print its id and name
search_opts = {'all_tenants': 1}
for server in nova_cli.servers.list(search_opts=search_opts):
    print server.id, server.name
