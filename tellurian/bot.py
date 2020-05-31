import logging
import discord
from config import Config

logging.basicConfig(level=logging.ERROR, format='%(asctime)s [%(levelname)-7s] %(message)s')
log = logging.getLogger(__name__)

config = Config()
log.info(config.token)

def bad_sketch(msg) -> bool:
    """ If True then delete message """

    if msg.channel.id == config.sketchbook:
        if "https://www.dropbox.com/" in msg.content:
            return False

        if "https://drive.google.com/" in msg.content:
            return False

        if not msg.attachments:
            return True

        for attachment in msg.attachments:
            if ".mp3" not in attachment.filename:
                return True

    return False


class Tellurian(discord.Client):

    async def on_ready(self):
        log.info(f'Logged on as {self.user}')

    async def on_message(self, message):
        if bad_sketch(message):
            await message.delete()

if __name__ == "__main__":
    client = Tellurian()
    client.run(config.token)
