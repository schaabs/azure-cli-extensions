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


class LifetimeAction(Model):
    """Action and its trigger that will be performed by Key Vault over the
    lifetime of a certificate.

    :param trigger: The condition that will execute the action.
    :type trigger: ~azure.keyvault.models.Trigger
    :param action: The action that will be executed.
    :type action: ~azure.keyvault.models.Action
    """

    _attribute_map = {
        'trigger': {'key': 'trigger', 'type': 'Trigger'},
        'action': {'key': 'action', 'type': 'Action'},
    }

    def __init__(self, **kwargs):
        super(LifetimeAction, self).__init__(**kwargs)
        self.trigger = kwargs.get('trigger', None)
        self.action = kwargs.get('action', None)
