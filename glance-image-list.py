#!/usr/bin/python
# openstack example python-let: glance-image-list.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: http://www.apache.org/licenses/LICENSE-2.0
# vim: si et sw=4 ts=4

import os
import sys
from keystoneclient.v2_0 import client as keystone_client
from glanceclient import Client as glance_client


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
ks_token = keystone_cli.auth_token
ep_glance = keystone_cli.service_catalog.url_for(service_type='image')

glance_cli = glance_client(1, endpoint=ep_glance, token=ks_token)
# For each image, print its id and name
for image in glance_cli.images.list():
    # print image.id, image.name, ...
    print ("{0.id} {0.name} {0.disk_format} {0.container_format} "
           "{0.size} {0.status}".format(image))
