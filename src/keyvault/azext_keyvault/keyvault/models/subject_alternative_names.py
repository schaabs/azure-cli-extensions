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


class SubjectAlternativeNames(Model):
    """The subject alternate names of a X509 object.

    :param emails: Email addresses.
    :type emails: list[str]
    :param dns_names: Domain names.
    :type dns_names: list[str]
    :param upns: User principal names.
    :type upns: list[str]
    """

    _attribute_map = {
        'emails': {'key': 'emails', 'type': '[str]'},
        'dns_names': {'key': 'dns_names', 'type': '[str]'},
        'upns': {'key': 'upns', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(SubjectAlternativeNames, self).__init__(**kwargs)
        self.emails = kwargs.get('emails', None)
        self.dns_names = kwargs.get('dns_names', None)
        self.upns = kwargs.get('upns', None)
