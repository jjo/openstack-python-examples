#!/usr/bin/env python
# openstack example python-let: neutron-net-list.sdk.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: http://www.apache.org/licenses/LICENSE-2.0
# vim: si et sw=4 ts=4

import os
from openstack import connection
from openstack import profile


def get_creds():
    # create a dictionary as e.g.: {'username': env['OS_USERNAME'], ...
    return {key: os.environ.get('OS_{}'.format(key.upper())) for key in
            ('auth_url', 'username', 'password', 'tenant_name', 'region_name')}


creds = get_creds()
# SDK uses project_name instead of tenant_name
creds['project_name'] = creds['tenant_name']
# SDK handles region_name, services versions via profile
prof = profile.Profile()
prof.set_region(profile.Profile.ALL, creds['region_name'])
prof.set_version('network', 'v2')
conn = connection.Connection(profile=prof, **creds)
for net in conn.network.networks():
    print net.id, net.name, net.subnets
