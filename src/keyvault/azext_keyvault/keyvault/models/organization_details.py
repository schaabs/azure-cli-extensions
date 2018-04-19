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


class OrganizationDetails(Model):
    """Details of the organization of the certificate issuer.

    :param id: Id of the organization.
    :type id: str
    :param admin_details: Details of the organization administrator.
    :type admin_details: list[~azure.keyvault.models.AdministratorDetails]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'admin_details': {'key': 'admin_details', 'type': '[AdministratorDetails]'},
    }

    def __init__(self, **kwargs):
        super(OrganizationDetails, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.admin_details = kwargs.get('admin_details', None)
