#!/usr/bin/python
# openstack example python-let: nova-list.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: http://www.apache.org/licenses/LICENSE-2.0
# vim: si et sw=4 ts=4

import os
import sys
from novaclient import client as nova_client


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
nova_cli = nova_client.Client(2,
                              auth_url=creds['auth_url'],
                              username=creds['username'],
                              api_key=creds['password'],
                              project_id=creds['tenant_name'],
                              region_name=creds['region_name'])
# For each instance, print below attrs
search_opts = {'all_tenants': 1}
attrs = """
id name status user_id tenant_id created OS-SRV-USG:launched_at hostId
OS-EXT-SRV-ATTR:hypervisor_hostname OS-EXT-STS:power_state
OS-EXT-STS:power_state flavor networks os-extended-volumes:volumes_attached
"""
attrs = attrs.split()
for server in nova_cli.servers.list(search_opts=search_opts):
    print " ".join(map(lambda x: str(getattr(server, x)), attrs))
