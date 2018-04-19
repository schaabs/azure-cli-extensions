# coding=utf-8
# pylint: disable-all

# ---------------------------------------------------------------------------------
# The code for this extension file is pulled from the azure-sdk-for-python repo and
# modified to run inside a cli extension.  Changes may cause incorrect behavior and
# will be lost if the code is regenerated. Please see the readme.md at the base of
# the keyvault extension for details.
# ---------------------------------------------------------------------------------

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


class VaultAccessPolicyProperties(Model):
    """Properties of the vault access policy.

    All required parameters must be populated in order to send to Azure.

    :param access_policies: Required. An array of 0 to 16 identities that have
     access to the key vault. All identities in the array must use the same
     tenant ID as the key vault's tenant ID.
    :type access_policies: list[~azure.mgmt.keyvault.models.AccessPolicyEntry]
    """

    _validation = {
        'access_policies': {'required': True},
    }

    _attribute_map = {
        'access_policies': {'key': 'accessPolicies', 'type': '[AccessPolicyEntry]'},
    }

    def __init__(self, **kwargs):
        super(VaultAccessPolicyProperties, self).__init__(**kwargs)
        self.access_policies = kwargs.get('access_policies', None)
