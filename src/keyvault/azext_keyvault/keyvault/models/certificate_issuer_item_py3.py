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


class CertificateIssuerItem(Model):
    """The certificate issuer item containing certificate issuer metadata.

    :param id: Certificate Identifier.
    :type id: str
    :param provider: The issuer provider.
    :type provider: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'provider': {'key': 'provider', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, provider: str=None, **kwargs) -> None:
        super(CertificateIssuerItem, self).__init__(**kwargs)
        self.id = id
        self.provider = provider
