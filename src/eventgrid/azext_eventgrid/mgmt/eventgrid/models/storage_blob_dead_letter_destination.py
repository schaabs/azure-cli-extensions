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

from .dead_letter_destination import DeadLetterDestination


class StorageBlobDeadLetterDestination(DeadLetterDestination):
    """Information about the storage blob based dead letter destination.

    :param endpoint_type: Constant filled by server.
    :type endpoint_type: str
    :param resource_id: The Azure Resource ID of the storage account that is
     the destination of the deadletter events
    :type resource_id: str
    :param blob_container_name: The name of the Storage blob container that is
     the destination of the deadletter events
    :type blob_container_name: str
    """

    _validation = {
        'endpoint_type': {'required': True},
    }

    _attribute_map = {
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
        'blob_container_name': {'key': 'properties.blobContainerName', 'type': 'str'},
    }

    def __init__(self, resource_id=None, blob_container_name=None):
        super(StorageBlobDeadLetterDestination, self).__init__()
        self.resource_id = resource_id
        self.blob_container_name = blob_container_name
        self.endpoint_type = 'StorageBlob'
