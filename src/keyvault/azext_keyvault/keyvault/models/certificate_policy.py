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


class CertificatePolicy(Model):
    """Management policy for a certificate.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The certificate id.
    :vartype id: str
    :param key_properties: Properties of the key backing a certificate.
    :type key_properties: ~azure.keyvault.models.KeyProperties
    :param secret_properties: Properties of the secret backing a certificate.
    :type secret_properties: ~azure.keyvault.models.SecretProperties
    :param x509_certificate_properties: Properties of the X509 component of a
     certificate.
    :type x509_certificate_properties:
     ~azure.keyvault.models.X509CertificateProperties
    :param lifetime_actions: Actions that will be performed by Key Vault over
     the lifetime of a certificate.
    :type lifetime_actions: list[~azure.keyvault.models.LifetimeAction]
    :param issuer_parameters: Parameters for the issuer of the X509 component
     of a certificate.
    :type issuer_parameters: ~azure.keyvault.models.IssuerParameters
    :param attributes: The certificate attributes.
    :type attributes: ~azure.keyvault.models.CertificateAttributes
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'key_properties': {'key': 'key_props', 'type': 'KeyProperties'},
        'secret_properties': {'key': 'secret_props', 'type': 'SecretProperties'},
        'x509_certificate_properties': {'key': 'x509_props', 'type': 'X509CertificateProperties'},
        'lifetime_actions': {'key': 'lifetime_actions', 'type': '[LifetimeAction]'},
        'issuer_parameters': {'key': 'issuer', 'type': 'IssuerParameters'},
        'attributes': {'key': 'attributes', 'type': 'CertificateAttributes'},
    }

    def __init__(self, **kwargs):
        super(CertificatePolicy, self).__init__(**kwargs)
        self.id = None
        self.key_properties = kwargs.get('key_properties', None)
        self.secret_properties = kwargs.get('secret_properties', None)
        self.x509_certificate_properties = kwargs.get('x509_certificate_properties', None)
        self.lifetime_actions = kwargs.get('lifetime_actions', None)
        self.issuer_parameters = kwargs.get('issuer_parameters', None)
        self.attributes = kwargs.get('attributes', None)
