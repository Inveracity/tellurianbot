import logging
import discord

from config import Config

logging.basicConfig(level=logging.ERROR, format='%(asctime)s [%(levelname)-7s] %(message)s')
log = logging.getLogger(__name__)

config = Config()
log.info(config.token)

class Tellurian(discord.Client):

    async def on_ready(self):
        log.info(f'Logged on as {self.user}')

    async def on_message(self, message):
        """ Delete messages that are not mp3 files from #sketchbook """
        if message.channel.id == config.sketchbook:
            if not message.attachments:
                await message.delete()

            for attachment in message.attachments:
                if ".mp3" not in attachment.filename:
                    await message.delete()


client = Tellurian()

client.run(config.token)
