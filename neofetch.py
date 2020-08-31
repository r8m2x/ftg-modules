#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import logging

import os

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class NeofetchMod(loader.Module):
    """Description for module"""
    strings = {
               "name": "neofetch"
    }

    @loader.unrestricted
    async def neofetchcmd(self, message):
        """Neofetch который работает на хероку"""

        await message.edit(os.popen("curl -Ls https://github.com/dylanaraps/neofetch/raw/master/neofetch | bash -s -- --stdout").read())
        
