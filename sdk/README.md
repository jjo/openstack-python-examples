Openstack API python-lets examples using SDK
============================================

Openstack python examples using SDK (instead of services' own APIs),
see http://docs.openstack.org/user-guide/sdk.html .

Openstack SDK is quite a moving target, you may want to:

    virtualenv ~/.venv/openstacksdk
    . ~/.venv/openstacksdk/bin/activate
    pip install openstacksdk

All these assume you've already loaded your openstack credentials
from your ``openrc.sh`` file, namely ``OS_USERNAME``,
``OS_TENANT_NAME``, ``OS_PASSWORD``, ``OS_AUTH_URL``,
``OS_REGION_NAME``.

