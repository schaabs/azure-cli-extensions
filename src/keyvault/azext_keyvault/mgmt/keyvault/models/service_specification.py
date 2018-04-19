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


class ServiceSpecification(Model):
    """One property of operation, include log specifications.

    :param log_specifications: Log specifications of operation.
    :type log_specifications:
     list[~azure.mgmt.keyvault.models.LogSpecification]
    """

    _attribute_map = {
        'log_specifications': {'key': 'logSpecifications', 'type': '[LogSpecification]'},
    }

    def __init__(self, **kwargs):
        super(ServiceSpecification, self).__init__(**kwargs)
        self.log_specifications = kwargs.get('log_specifications', None)
