# pylint: skip-file
# ---------------------------------------------------------------------------
# The code for this extension file is pulled from the azure-sdk-for-python repo. Changes may 
# cause incorrect behavior and will be lost if the code is regenerated.
# Please see the readme.md at the base of the keyvault extension for details.
# ---------------------------------------------------------------------------
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Permissions(Model):
    """Permissions the identity has for keys, secrets, certificates and storage.

    :param keys: Permissions to keys
    :type keys: list[str or ~azure.mgmt.keyvault.models.KeyPermissions]
    :param secrets: Permissions to secrets
    :type secrets: list[str or ~azure.mgmt.keyvault.models.SecretPermissions]
    :param certificates: Permissions to certificates
    :type certificates: list[str or
     ~azure.mgmt.keyvault.models.CertificatePermissions]
    :param storage: Permissions to storage accounts
    :type storage: list[str or ~azure.mgmt.keyvault.models.StoragePermissions]
    """

    _attribute_map = {
        'keys': {'key': 'keys', 'type': '[str]'},
        'secrets': {'key': 'secrets', 'type': '[str]'},
        'certificates': {'key': 'certificates', 'type': '[str]'},
        'storage': {'key': 'storage', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(Permissions, self).__init__(**kwargs)
        self.keys = kwargs.get('keys', None)
        self.secrets = kwargs.get('secrets', None)
        self.certificates = kwargs.get('certificates', None)
        self.storage = kwargs.get('storage', None)
