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


class Trigger(Model):
    """A condition to be satisfied for an action to be executed.

    :param lifetime_percentage: Percentage of lifetime at which to trigger.
     Value should be between 1 and 99.
    :type lifetime_percentage: int
    :param days_before_expiry: Days before expiry to attempt renewal. Value
     should be between 1 and validity_in_months multiplied by 27. If
     validity_in_months is 36, then value should be between 1 and 972 (36 *
     27).
    :type days_before_expiry: int
    """

    _validation = {
        'lifetime_percentage': {'maximum': 99, 'minimum': 1},
    }

    _attribute_map = {
        'lifetime_percentage': {'key': 'lifetime_percentage', 'type': 'int'},
        'days_before_expiry': {'key': 'days_before_expiry', 'type': 'int'},
    }

    def __init__(self, *, lifetime_percentage: int=None, days_before_expiry: int=None, **kwargs) -> None:
        super(Trigger, self).__init__(**kwargs)
        self.lifetime_percentage = lifetime_percentage
        self.days_before_expiry = days_before_expiry
