# pylint: disable-all

# ---------------------------------------------------------------------------------
# The code for this extension file is pulled from the azure-sdk-for-python repo
# and modified to run inside a cli extension.  Changes may cause incorrect behavior
# and will be lost if the code is regenerated. Please see the readme.md at the base
# of the keyvault extension for details.
# ---------------------------------------------------------------------------------

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


class KeyUpdateParameters(Model):
    """The key update parameters.

    :param key_ops: Json web key operations. For more information on possible
     key operations, see JsonWebKeyOperation.
    :type key_ops: list[str or ~azure.keyvault.models.JsonWebKeyOperation]
    :param key_attributes:
    :type key_attributes: ~azure.keyvault.models.KeyAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'key_ops': {'key': 'key_ops', 'type': '[str]'},
        'key_attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(KeyUpdateParameters, self).__init__(**kwargs)
        self.key_ops = kwargs.get('key_ops', None)
        self.key_attributes = kwargs.get('key_attributes', None)
        self.tags = kwargs.get('tags', None)