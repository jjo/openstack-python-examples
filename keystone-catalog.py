#!/usr/bin/python
# openstack example python-let: keystone-catalog.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: GPLv3
# vim: si et sw=4 ts=4

import os
from keystoneclient.v2_0 import client as keystone_client


def get_creds():
    # create a dictionary as e.g.: {'username': env['OS_USERNAME'], ...
    return {key: os.environ.get('OS_{}'.format(key.upper())) for key in
            ('auth_url', 'username', 'password', 'tenant_name', 'region_name')}
    return creds

creds = get_creds()
keystone_cli = keystone_client.Client(**creds)
# For each service name in catalog, print its name and its
# (potentially multiple) id, publicURL
for ep_name, ep_values in keystone_cli.service_catalog.get_endpoints().items():
    print '{:16} {}'.format(ep_name,
                            [(ep_val['id'], ep_val['publicURL'])
                             for ep_val in ep_values])
