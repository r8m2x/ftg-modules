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

# requires: pydub

import asyncio
import logging
import io
from pydub import AudioSegment as AS
from telethon import types

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class ConvertMod(loader.Module):
    """Конвертирование аудио в: mp3, войс; конвертирование стикера, jpg, и др. в png"""
    strings = {
        "name": "convert"
    }
    
    async def client_ready(self, client, db):
        self.client = client
    
    @loader.unrestricted
    async def mp3cmd(self, message):
        """Конвертация в mp3."""
        try:
            await message.edit("<code>Обработка..</code>")
            reply = await message.get_reply_message()
            rf = io.BytesIO(await self.client.download_file(reply, bytes))
            rf.seek(0)
            m = io.BytesIO()
            m.name="out.mp3"
            audio = AS.from_file(rf)
            audio.split_to_mono()
            audio.export(m, format="mp3")
            m.seek(0)
            await self.client.send_file(message.to_id, m, attributes=[types.DocumentAttributeAudio(duration=reply.media.document.attributes[0].duration, voice=False, title="Converted", performer="@r8m2x_modules", waveform=None),types.DocumentAttributeFilename(file_name="output.mp3")], reply_to=reply)
            await message.delete()
        except:
            await utils.answer(message, "<code>Произошла ошибка. Верятно то что вы хотели конвертировать - не аудиофайл.</code>")
   
    @loader.unrestricted
    async def voicecmd(self, message):
        """Конвертация в войс."""
        try:
            reply = await message.get_reply_message()
            await message.edit("<code>Обработка...</code>")
            rf = io.BytesIO(await self.client.download_file(reply, bytes))
            rf.seek(0)
            m = io.BytesIO()
            m.name="out.ogg"
            audio = AS.from_file(rf)
            audio.split_to_mono()
            audio.export(m, format="ogg", bitrate="64k", codec="libopus")
            m.seek(0)
            await self.client.send_file(message.to_id, m, voice_note=True, reply_to=reply)
            await message.delete()
        except:
            await utils.answer(message, "<code>Произошла ошибка. Верятно то что вы хотели конвертировать - не аудиофайл.</code>")