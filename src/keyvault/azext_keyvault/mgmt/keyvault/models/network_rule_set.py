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


class NetworkRuleSet(Model):
    """A set of rules governing the network accessibility of a vault.

    :param bypass: Tells what traffic can bypass network rules. This can be
     'AzureServices' or 'None'.  If not specified the default is
     'AzureServices'. Possible values include: 'AzureServices', 'None'
    :type bypass: str or ~azure.mgmt.keyvault.models.NetworkRuleBypassOptions
    :param default_action: The default action when no rule from ipRules and
     from virtualNetworkRules match. This is only used after the bypass
     property has been evaluated. Possible values include: 'Allow', 'Deny'
    :type default_action: str or ~azure.mgmt.keyvault.models.NetworkRuleAction
    :param ip_rules: The list of IP address rules.
    :type ip_rules: list[~azure.mgmt.keyvault.models.IPRule]
    :param virtual_network_rules: The list of virtual network rules.
    :type virtual_network_rules:
     list[~azure.mgmt.keyvault.models.VirtualNetworkRule]
    """

    _attribute_map = {
        'bypass': {'key': 'bypass', 'type': 'str'},
        'default_action': {'key': 'defaultAction', 'type': 'str'},
        'ip_rules': {'key': 'ipRules', 'type': '[IPRule]'},
        'virtual_network_rules': {'key': 'virtualNetworkRules', 'type': '[VirtualNetworkRule]'},
    }

    def __init__(self, **kwargs):
        super(NetworkRuleSet, self).__init__(**kwargs)
        self.bypass = kwargs.get('bypass', None)
        self.default_action = kwargs.get('default_action', None)
        self.ip_rules = kwargs.get('ip_rules', None)
        self.virtual_network_rules = kwargs.get('virtual_network_rules', None)
