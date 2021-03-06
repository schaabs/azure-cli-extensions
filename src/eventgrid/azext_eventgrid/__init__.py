# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

import azext_eventgrid._help  # pylint: disable=unused-import


class EventGridCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        eventgrid_custom = CliCommandType(operations_tmpl='azext_eventgrid.custom#{}')
        super(EventGridCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                      custom_command_type=eventgrid_custom,
                                                      min_profile='2017-03-10-profile')

    def load_command_table(self, args):
        from .commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from ._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = EventGridCommandsLoader
