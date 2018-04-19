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


class KeyVerifyParameters(Model):
    """The key verify parameters.

    All required parameters must be populated in order to send to Azure.

    :param algorithm: Required. The signing/verification algorithm. For more
     information on possible algorithm types, see JsonWebKeySignatureAlgorithm.
     Possible values include: 'PS256', 'PS384', 'PS512', 'RS256', 'RS384',
     'RS512', 'RSNULL', 'ES256', 'ES384', 'ES512', 'ECDSA256'
    :type algorithm: str or
     ~azure.keyvault.models.JsonWebKeySignatureAlgorithm
    :param digest: Required. The digest used for signing.
    :type digest: bytes
    :param signature: Required. The signature to be verified.
    :type signature: bytes
    """

    _validation = {
        'algorithm': {'required': True, 'min_length': 1},
        'digest': {'required': True},
        'signature': {'required': True},
    }

    _attribute_map = {
        'algorithm': {'key': 'alg', 'type': 'str'},
        'digest': {'key': 'digest', 'type': 'base64'},
        'signature': {'key': 'value', 'type': 'base64'},
    }

    def __init__(self, **kwargs):
        super(KeyVerifyParameters, self).__init__(**kwargs)
        self.algorithm = kwargs.get('algorithm', None)
        self.digest = kwargs.get('digest', None)
        self.signature = kwargs.get('signature', None)
