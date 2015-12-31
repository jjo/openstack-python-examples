#!/usr/bin/python
# openstack example python-let: keystone-catalog.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: http://www.apache.org/licenses/LICENSE-2.0
# vim: si et sw=4 ts=4

import os
import sys
from keystoneclient.v2_0 import client as keystone_client


def get_creds():
    "return a dictionary as: {'username': os.environ['OS_USERNAME'], ...}"
    try:
        return {key: os.environ['OS_{}'.format(key.upper())] for key in
                ('auth_url', 'username', 'password', 'tenant_name',
                 'region_name')}
    except KeyError as e:
        print >> sys.stderr, ("ERROR: missing from environment: {}, "
                              "need to load your openrc.sh".format(e))
        sys.exit(1)

creds = get_creds()
keystone_cli = keystone_client.Client(**creds)
# For each service name in catalog, print its name and its
# (potentially multiple) id, publicURL
for ep_name, ep_values in keystone_cli.service_catalog.get_endpoints().items():
    ep_info = [(ep_val['id'], ep_val['publicURL']) for ep_val in ep_values]
    print '{:16} {}'.format(ep_name, ep_info)
