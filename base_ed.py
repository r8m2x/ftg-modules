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

import logging
import base64

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class Base64Mod(loader.Module):
    """Encode/decode base(16|32|64|85). NOT ENCRYPTING FILES!"""
    strings = {
        "name": "base64",
        "no_text_e": "<code>Вы не ввели текст для кодирования.</code>",
        "no_text_d": "<code>Вы не ввели текст для декодирования.</code>"
    }
    
    @loader.sudo
    async def b16ecmd(self,m):
        """.b16e [reply or text]"""
        try:
            text = utils.get_args_raw(m)
            reply = await m.get_reply_message()
            if not text:
                if reply:
                    text = reply.raw_text
                else:
                    return await utils.answer(m, self.strings(no_text_e, m))
            await m.edit(base64.b16encode(text.encode()).decode())
        except:
            await m.edit("<code>Я не могу закодировать это</code>")
    @loader.sudo
    async def b32ecmd(self,m):
        """.b32e [reply or text]"""
        try:
            text = utils.get_args_raw(m)
            reply = await m.get_reply_message()
            if not text:
                if reply:
                    text = reply.raw_text
                else:
                    return await utils.answer(m, self.strings(no_text_e, m))
            await m.edit(base64.b32encode(text.encode()).decode())
        except:
            await m.edit("<code>Я не могу закодировать это</code>")
    @loader.sudo
    async def b64ecmd(self,m):
        """.b64e [reply or text]"""
        try:
            text = utils.get_args_raw(m)
            reply = await m.get_reply_message()
            if not text:
                if reply:
                    text = reply.raw_text
                else:
                    return await utils.answer(m, self.strings(no_text_e, m))
            await m.edit(base64.b64encode(text.encode()).decode())
        except:
            await m.edit("<code>Я не могу закодировать это</code>")
    @loader.sudo
    async def b85ecmd(self,m):
        """.b85e [reply or text]"""
        try:
            text = utils.get_args_raw(m)
            reply = await m.get_reply_message()
            if not text:
                if reply:
                    text = reply.raw_text
                else:
                    return await utils.answer(m, self.strings(no_text_e, m))
            await m.edit(base64.b85encode(text.encode()).decode())
        except:
            await m.edit("<code>Я не могу закодировать это</code>")
    
    @loader.sudo
    async def b16dcmd(self,m):
        """.b16d [reply or text]"""
        try:
            text = utils.get_args_raw(m)
            reply = await m.get_reply_message()
            if not text:
                if reply:
                    text = reply.raw_text
                else:
                    return await utils.answer(m, self.strings(no_text_e, m))
            await m.edit(base64.b16decode(text.encode()).decode())
        except:
            await m.edit("<code>Я не могу декодировать это</code>")
    @loader.sudo
    async def b32dcmd(self,m):
        """.b32d [reply or text]"""
        try:
            text = utils.get_args_raw(m)
            reply = await m.get_reply_message()
            if not text:
                if reply:
                    text = reply.raw_text
                else:
                    return await utils.answer(m, self.strings(no_text_e, m))
            await m.edit(base64.b32decode(text.encode()).decode())
        except:
            await m.edit("<code>Я не могу декодировать это</code>")
    @loader.sudo
    async def b64dcmd(self,m):
        """.b64d [reply or text]"""
        try:
            text = utils.get_args_raw(m)
            reply = await m.get_reply_message()
            if not text:
                if reply:
                    text = reply.raw_text
                else:
                    return await utils.answer(m, self.strings(no_text_e, m))
            await m.edit(base64.b64decode(text.encode()).decode())
        except:
            await m.edit("<code>Я не могу декодировать это</code>")
    @loader.sudo
    async def b85dcmd(self,m):
        """.b85d [reply or text]"""
        try:
            text = utils.get_args_raw(m)
            reply = await m.get_reply_message()
            if not text:
                if reply:
                    text = reply.raw_text
                else:
                    return await utils.answer(m, self.strings(no_text_e, m))
            await m.edit(base64.b85decode(text.encode()).decode())
        except:
            await m.edit("<code>Я не могу декодировать это</code>")