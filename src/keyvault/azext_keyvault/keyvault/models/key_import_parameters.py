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


class KeyImportParameters(Model):
    """The key import parameters.

    All required parameters must be populated in order to send to Azure.

    :param hsm: Whether to import as a hardware key (HSM) or software key.
    :type hsm: bool
    :param key: Required. The Json web key
    :type key: ~azure.keyvault.models.JsonWebKey
    :param key_attributes: The key management attributes.
    :type key_attributes: ~azure.keyvault.models.KeyAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    """

    _validation = {
        'key': {'required': True},
    }

    _attribute_map = {
        'hsm': {'key': 'Hsm', 'type': 'bool'},
        'key': {'key': 'key', 'type': 'JsonWebKey'},
        'key_attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(KeyImportParameters, self).__init__(**kwargs)
        self.hsm = kwargs.get('hsm', None)
        self.key = kwargs.get('key', None)
        self.key_attributes = kwargs.get('key_attributes', None)
        self.tags = kwargs.get('tags', None)
