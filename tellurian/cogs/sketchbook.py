import logging

from discord import Message
from discord.ext.commands import Bot, Cog

from tellurian import constants

log = logging.getLogger(__name__)


class Sketchbook(Cog):
    """Super helpful automated help-channel responses."""

    def __init__(self, bot: Bot):
        """Initialize this cog with the Bot instance. Always do this."""
        self.bot = bot

    @staticmethod
    def _bad_sketch(msg: Message) -> bool:
        """Does this message belong in the #sketchbook channel?"""
        if msg.channel.id == constants.Channels.sketchbook:
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

    @Cog.listener()
    async def on_message(self, msg: Message) -> None:
        """
        Does this message belong in the #sketchbook channel?

        If not, we should relay that message to another channel and then delete it from #sketchbook.
        """
        ctx = await self.bot.get_context(msg)

        # Check if we need to take any action
        if not self._bad_sketch(msg) or ctx.author.bot:
            return

        # Okay, we need to relay this message to another channel.
        await ctx.send("ding dong!")


def setup(bot: Bot) -> None:
    """
    This function is called automatically when this cog is loaded by the bot.

    It's only purpose is to load the cog above, and to pass the Bot instance into it.
    """
    bot.add_cog(Sketchbook(bot))
    log.info("Cog loaded: SocialDistancing")
