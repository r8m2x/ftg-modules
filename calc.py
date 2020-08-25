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
class CalcMod(loader.Module):
    """Калькулятор."""
    strings = {"name": "calc", "bad": "<code>Я не могу решить этот пример.</code>"}

    @loader.unrestricted
    async def calccmd(self, message):
        """.calc [пример] - калькулятор."""
        text = utils.get_args_raw(message)
        if not text:
            return await utils.answer(message, self.strings("bad", message))
        isCorrect = text.replace(" ", "").replace("/", "").replace("*", "").replace("**", "").replace("+", "").replace("-", "").replace("(", "").replace(")", "").replace(".", "").isdigit()
        if not isCorrect:
            return await utils.answer(message, self.strings("bad", message))
        try:
            await message.edit(f"<code>{text}</code>=<code>{eval(text)}</code>")
        except:
            return await utils.answer(message, self.strings("bad", message))