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

from requests import get

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class BssidMod(loader.Module):
    """Получение местоположения по mac-адресу."""
    strings = {"name": "bssid", "bad_mac": "<code>MAC адрес не верный.</code>"}

    @loader.unrestricted
    async def bssidcmd(self, message):
        """.bssid [МАК-адрес] - найти местоположение по мак адресу.."""
        addr = utils.get_args_raw(message)
        if not addr:
            return await utils.answer(message, self.strings("bad_mac", message))
        if len(list(addr)) < 16:
            return await utils.answer(message, self.strings("bad_mac", message))
        
        await message.edit("<code>Обработка...</code>")
        
        response = get(f"https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid={addr}")
        r = response.json()
        
        if r["result"] == 200:
            await message.edit(f"""
    
<strong>BSSID</strong>: <code>{addr}</code>
    
======================
                          
<strong>Latitude</strong>: <code>{r["data"]["lat"]}</code>
<strong>Longitude</strong>: <code>{r["data"]["lon"]}</code>
                          
    """)
        elif r["result"] == 404:
            await utils.answer(message, self.strings("bad_mac", message))
        else:
            await message.edit("<code>Произошла ошибка на сервере. Попробуйте позднее.</code>")
            #await message.reply(str(r))