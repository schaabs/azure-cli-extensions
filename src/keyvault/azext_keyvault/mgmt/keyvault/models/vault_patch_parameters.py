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


class VaultPatchParameters(Model):
    """Parameters for creating or updating a vault.

    :param tags: The tags that will be assigned to the key vault.
    :type tags: dict[str, str]
    :param properties: Properties of the vault
    :type properties: ~azure.mgmt.keyvault.models.VaultPatchProperties
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'VaultPatchProperties'},
    }

    def __init__(self, **kwargs):
        super(VaultPatchParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.properties = kwargs.get('properties', None)
