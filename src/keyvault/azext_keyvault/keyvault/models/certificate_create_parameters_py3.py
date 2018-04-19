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


class CertificateCreateParameters(Model):
    """The certificate create parameters.

    :param certificate_policy: The management policy for the certificate.
    :type certificate_policy: ~azure.keyvault.models.CertificatePolicy
    :param certificate_attributes: The attributes of the certificate
     (optional).
    :type certificate_attributes: ~azure.keyvault.models.CertificateAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'certificate_policy': {'key': 'policy', 'type': 'CertificatePolicy'},
        'certificate_attributes': {'key': 'attributes', 'type': 'CertificateAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, certificate_policy=None, certificate_attributes=None, tags=None, **kwargs) -> None:
        super(CertificateCreateParameters, self).__init__(**kwargs)
        self.certificate_policy = certificate_policy
        self.certificate_attributes = certificate_attributes
        self.tags = tags
