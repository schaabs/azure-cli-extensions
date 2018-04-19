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
from msrest.exceptions import HttpOperationError


class KeyVaultError(Model):
    """The key vault error exception.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar error:
    :vartype error: ~azure.keyvault.models.Error
    """

    _validation = {
        'error': {'readonly': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(self, **kwargs) -> None:
        super(KeyVaultError, self).__init__(**kwargs)
        self.error = None


class KeyVaultErrorException(HttpOperationError):
    """Server responsed with exception of type: 'KeyVaultError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(KeyVaultErrorException, self).__init__(deserialize, response, 'KeyVaultError', *args)
