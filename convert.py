
import io
import os

from moviepy.editor import VideoFileClip

from .. import loader, utils

@loader.tds
class ConvertMod(loader.Module):
    """Just convert to voice, mp3 and png."""
    strings = {
                "name": "convert",
                "no_reply": "<code>reply</code>",
                "not_media": "<code>media in reply</code>"
              }
    
    async def client_ready(self, client, db):
        self.client = client

    @loader.unrestricted
    async def mp3cmd(self, message):
        """.mp3 [reply] - convert to mp3"""
        
        reply = await message.get_reply_message()
        
        if not reply:
            return await utils.answer(message, self.strings("no_reply", message))
        if not reply.media:
            return await utils.answer(message, self.strings("not_media", message))
        
        await message.edit("<code>Processing...</code>")
        
        if reply.video:
            await self.client.download_file(reply, "in.mp4")
            video = VideoFileClip("in.mp4")
            video.audio.write_audiofile("out.mp3")
            await self.client.send_file(message.to_id, "out.mp3")
            os.remove("out.mp3")
            os.remove("in.mp4")
        else:
            m = io.BytesIO(await self.client.download_file(reply));m.name = "out.mp3";m.seek(0)
            await self.client.send_file(message.to_id, m)
        await message.delete()
    
    @loader.unrestricted
    async def voicecmd(self, message):
        """.voice [reply] - convert to voice"""
        
        reply = await message.get_reply_message()
        
        if not reply:
            return await utils.answer(message, self.strings("no_reply", message))
        if not reply.media:
            return await utils.answer(message, self.strings("not_media", message))
        
        await message.edit("<code>Processing...</code>")
        
        if reply.video:
            await self.client.download_file(reply, "in.mp4")
            video = VideoFileClip("in.mp4")
            video.audio.write_audiofile("out.ogg")
            await self.client.send_file(message.to_id, "out.ogg", reply_to=reply,voice_note=True)
            os.remove("out.ogg")
            os.remove("in.mp4")
        else:
            m = io.BytesIO(await self.client.download_file(reply));m.name="out.ogg";m.seek(0)
            await self.client.send_file(message.to_id, m, reply_to=reply, voice_note=True)
        await message.delete()
    
    @loader.unrestricted
    async def pngcmd(self, message):
        """.png [reply] - convert to png"""
        
        reply = await message.get_reply_message()
        
        if not reply:
            return await utils.answer(message, self.strings("no_reply", message))
        if not reply.media:
            return await utils.answer(message, self.strings("not_media", message))
        
        m = io.BytesIO(await self.client.download_file(reply));m.name="out.png";m.seek(0)
        await self.client.send_file(message.to_id, m, reply_to=reply, force_document=True)
       
            
    