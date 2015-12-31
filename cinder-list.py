#!/usr/bin/python
# openstack example python-let: cinder-list.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: http://www.apache.org/licenses/LICENSE-2.0
# vim: si et sw=4 ts=4

import os
import sys
from cinderclient import client as cinder_client


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
cinder_cli = cinder_client.Client(1,
                                  auth_url=creds['auth_url'],
                                  username=creds['username'],
                                  api_key=creds['password'],
                                  project_id=creds['tenant_name'],
                                  region_name=creds['region_name'])
# For each cinder volume, print its id, size and display_name
for vol in cinder_cli.volumes.list():
    # print vol.id, vol.status, ...
    print ("{0.id} {0.status} {0.display_name} {0.size} {0.volume_type} "
           "{0.attachments}".format(vol))
