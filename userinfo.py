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

from telethon import functions

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class UserInfoMod(loader.Module):
    """Информация о пользователе."""
    strings = {
        "name": "userinfo",
    }
    async def client_ready(self, client, db):
        self.client = client
    @loader.unrestricted
    async def infocmd(self, message):
        """.info [reply]"""
        n = await message.get_reply_message()
        if not n:
            n = message
        u = await self.client(functions.users.GetFullUserRequest(n.from_id))
        user = u.user
        await message.edit(f"""

ID: {user.id}
Юзернейм: {user.username}

Имя: {user.first_name}
Фамилия: {user.last_name}
Био: {u.about}

Скамер: {user.scam}
Удален: {user.deleted}
Бот: {user.bot}

DC ID: {user.photo.dc_id}

Общих чатов: {u.common_chats_count}
Перманентная ссылка: <a href="tg://user?id={n.from_id}">тык</a>

""")
    