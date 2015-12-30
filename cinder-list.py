#!/usr/bin/python
# openstack example python-let: cinder-list.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: GPLv3
# vim: si et sw=4 ts=4

import os
from cinderclient import client as cinder_client


def get_creds():
    # create a dictionary as e.g.: {'username': env['OS_USERNAME'], ...
    return {key: os.environ.get('OS_{}'.format(key.upper())) for key in
            ('auth_url', 'username', 'password', 'tenant_name', 'region_name')}
    return creds

creds = get_creds()
cinder_cli = cinder_client.Client(1,
                                  creds['username'], creds['password'],
                                  creds['tenant_name'], creds['auth_url'],
                                  region_name=creds['region_name'])
# For each cinder volume, print its id, size and display_name
for vol in cinder_cli.volumes.list():
    print vol.id, vol.size, vol.display_name
