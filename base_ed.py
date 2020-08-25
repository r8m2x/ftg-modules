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
        "no_text_e": "<code>Provide text to encode.</code>",
        "no_text_d": "<code>Provide text to decode.</code>"
    }
    
    
    @loader.owner
    
    async def b85dcmd(self, message):
        """.b85d {encoded text} - decode base85"""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and reply:
        	text = reply.raw_text
        if not text and not reply:
        	return await utils.answer(message, self.strings("no_text_d", message))
        try:
            enc_bytes = bytes(text, "utf-8")
            dec_bytes = base64.b85decode(enc_bytes)
            decoded = bytes.decode(dec_bytes)
            await message.edit(decoded)
        except:
            await message.edit("<code>Invalid encoded text</code>")
    
    @loader.owner
    async def b85ecmd(self, message):
        """.b85e {text} - encode to base85"""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and reply:
        	text = reply.raw_text
        if not text and not reply:
        	return await utils.answer(message, self.strings("no_text_e", message))
        try:
            dec_bytes = bytes(text, "utf-8")
            enc_bytes = base64.b85encode(dec_bytes)
            encoded = bytes.decode(enc_bytes)
            await message.edit(encoded)
        except:
            await message.edit("<code>Error</code>")
    
    @loader.owner
    async def b64dcmd(self, message):
        """.b64d {encoded text} - decode base64"""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and reply:
            text = reply.raw_text
        if not text and not reply:
            return await utils.answer(message, self.strings("no_text_d", message))
        try:
            enc_bytes = bytes(text, "utf-8")
            dec_bytes = base64.b64decode(enc_bytes)
            decoded = bytes.decode(dec_bytes)
            await message.edit(decoded)
        except:
            await message.edit("<code>Invalid encoded text</code>")

    @loader.owner
    async def b64ecmd(self, message):
        """.b64e {text} - encode to base64"""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and reply:
            text = reply.raw_text
        if not text and not reply:
            return await utils.answer(message, self.strings("no_text_e", message))
        try:
            dec_bytes = bytes(text, "utf-8")
            enc_bytes = base64.b64encode(dec_bytes)
            encoded = bytes.decode(enc_bytes)
            await message.edit(encoded)
        except:
            await message.edit("<code>Error</code>")
        
    @loader.owner
    async def b32dcmd(self, message):
        """.b32d {encoded text} - decode base32"""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and reply:
            text = reply.raw_text
        if not text and not reply:
            return await utils.answer(message, self.strings("no_text_d", message))
        try:
            enc_bytes = bytes(text, "utf-8")
            dec_bytes = base64.b32decode(enc_bytes)
            decoded = bytes.decode(dec_bytes)
            await message.edit(decoded)
        except:
            await message.edit("<code>Invalid encoded text</code>")

    @loader.owner
    async def b32ecmd(self, message):
        """.b32e {text} - encode to base32"""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and reply:
            text = reply.raw_text
        if not text and not reply:
            return await utils.answer(message, self.strings("no_text_e", message))
        try:
            dec_bytes = bytes(text, "utf-8")
            enc_bytes = base64.b32encode(dec_bytes)
            encoded = bytes.decode(enc_bytes)
            await message.edit(encoded)
        except:
            await message.edit("<code>Error</code>")
        
    @loader.owner
    async def b16dcmd(self, message):

        """.b16d {encoded text} - decode base16"""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and reply:
            text = reply.raw_text
        if not text and not reply:
        	return await utils.answer(message, self.strings("no_text_d", message))
        try:
            enc_bytes = bytes(text, "utf-8")
            dec_bytes = base64.b16decode(enc_bytes)
            decoded = bytes.decode(dec_bytes)
            await message.edit(decoded)
        except:
            await message.edit("<code>Invalid encoded text</code>")
    
    @loader.owner
    async def b16ecmd(self, message):
        """.b16e {text} - encode to base16"""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and reply:
        	text = reply.raw_text
        if not text and not reply:
        	return await utils.answer(message, self.strings("no_text_e", message))
        try:
            dec_bytes = bytes(text, "utf-8")
            enc_bytes = base64.b16encode(dec_bytes)
            encoded = bytes.decode(enc_bytes)
            await message.edit(encoded)
        except:
            await message.edit("<code>Error</code>")