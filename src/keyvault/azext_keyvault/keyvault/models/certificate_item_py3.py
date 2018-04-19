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


class CertificateItem(Model):
    """The certificate item containing certificate metadata.

    :param id: Certificate identifier.
    :type id: str
    :param attributes: The certificate management attributes.
    :type attributes: ~azure.keyvault.models.CertificateAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    :param x509_thumbprint: Thumbprint of the certificate.
    :type x509_thumbprint: bytes
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'CertificateAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'x509_thumbprint': {'key': 'x5t', 'type': 'base64'},
    }

    def __init__(self, *, id: str=None, attributes=None, tags=None, x509_thumbprint: bytes=None, **kwargs) -> None:
        super(CertificateItem, self).__init__(**kwargs)
        self.id = id
        self.attributes = attributes
        self.tags = tags
        self.x509_thumbprint = x509_thumbprint