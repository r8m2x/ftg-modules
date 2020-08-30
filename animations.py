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

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class AnimationMod(loader.Module):
    """Анимация при помощи смайлов."""
    strings = {
               "name": "animations"
    }

    @loader.unrestricted
    async def moonscmd(self, message):
        """.moons [сколько раз повторять - дефолт 5 раз]"""
        text = utils.get_args_raw(message)
        if not text.isdigit():
            text = 5

        for _ in range(int(text)):
            for item in list("🌑🌘🌗🌖🌕🌔🌓🌒"):
                await message.edit(item)
                await asyncio.sleep(5)
    
    @loader.unrestricted
    async def clockscmd(self, message):
        """.clocks [сколько раз повторять - дефолт 5 раз]"""
        text = utils.get_args_raw(message)
        if not text.isdigit():
            text = 5

        for _ in range(int(text)):
            for item in list("🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛"):
                await message.edit(item)
                await asyncio.sleep(5)