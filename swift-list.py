#!/usr/bin/python
# openstack example python-let: swift-list.py
#
# Author: JuanJo Ciarlante <juanjosec@gmail.com>
# License: http://www.apache.org/licenses/LICENSE-2.0
# vim: si et sw=4 ts=4

import os
from swiftclient import client as swift_client


def get_creds():
    # create a dictionary as e.g.: {'username': env['OS_USERNAME'], ...
    return {key: os.environ.get('OS_{}'.format(key.upper())) for key in
            ('auth_url', 'username', 'password', 'tenant_name', 'region_name')}
    return creds

creds = get_creds()
swift_cli = swift_client.Connection(authurl=creds['auth_url'],
                                    user=creds['username'],
                                    key=creds['password'],
                                    auth_version='2.0',
                                    tenant_name=creds['tenant_name'],
                                    os_options={
                                        'region_name': creds['region_name']
                                    })
# For each swift container, print its name, objects count and bytes
for container in swift_cli.get_account()[1]:
    print "{name:32} {count:8} {bytes:16}".format(**container)
