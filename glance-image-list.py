#!/usr/bin/python
# openstack example python-let: glance-image-list.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: http://www.apache.org/licenses/LICENSE-2.0
# vim: si et sw=4 ts=4

import os
from keystoneclient.v2_0 import client as keystone_client
from glanceclient import Client as glance_client


def get_creds():
    # create a dictionary as e.g.: {'username': env['OS_USERNAME'], ...
    return {key: os.environ.get('OS_{}'.format(key.upper())) for key in
            ('auth_url', 'username', 'password', 'tenant_name', 'region_name')}
    return creds

creds = get_creds()
keystone_cli = keystone_client.Client(**creds)
ks_token = keystone_cli.auth_token
ep_glance = keystone_cli.service_catalog.url_for(service_type='image')

glance_cli = glance_client(1, endpoint=ep_glance, token=ks_token)
# For each image, print its id and name
for image in glance_cli.images.list():
    print image.id, image.name
