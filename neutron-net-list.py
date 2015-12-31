#!/usr/bin/python
# openstack example python-let: neutron-net-list.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: http://www.apache.org/licenses/LICENSE-2.0
# vim: si et sw=4 ts=4

import os
import sys
from neutronclient.v2_0 import client as neutron_client


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
neutron_cli = neutron_client.Client(**creds)

# Index subnets by id (will avoid one rpc per net call at the last line)
subnets_by_id = {s['id']: s for s in neutron_cli.list_subnets()["subnets"]}

# For each neutron network, print its id and value
for net in neutron_cli.list_networks().get('networks'):
    net['subnets_info'] = [(subnet['id'], subnet['cidr']) for subnet in
                           [subnets_by_id[s_id] for s_id in net['subnets']]]
    # print net['id'], ...
    print "{id} {name} {subnets_info}".format(**net)
