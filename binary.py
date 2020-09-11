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
class BinaryMod(loader.Module):
    """Конвертация текста в 1, 0 и наоборот"""
    strings = {
        "name": "binary"
    }

    

    @loader.unrestricted
    async def stbcmd(self, message):
        """.stb [реплай или текст]"""
        reply = await message.get_reply_message()
        text = utils.get_args_raw(message)
        
        if reply and not text:
            text = reply.raw_text
        if not text:
            return await utils.answer(message, "<code>Вы не ввели текст.</code>")
        
        await utils.answer(message, ''.join([bin(ord(char))[2:].zfill(8) + " " for char in text]))
        
    @loader.unrestricted
    async def btscmd(self, message):
        """.bts [реплай или текст]"""
        reply = await message.get_reply_message()
        text = utils.get_args_raw(message)
        
        if reply and not text:
            text = reply.raw_text
        if not text:
            return await utils.answer(message, "<code>Вы не ввели текст.</code>")
        
        await utils.answer(message, ''.join([chr(int(x, 2)) for x in text.split(" ")]))