import logging
from typing import Optional

import discord
from discord import Message
from discord.ext.commands import Bot, Cog

from tellurian import constants

log = logging.getLogger(__name__)


class Sketchbook(Cog):
    """Keep the #sketchbook channel clean, and relay non-sketches to #sketchbook-comments."""

    def __init__(self, bot: Bot):
        """Initialize this cog with the Bot instance."""
        self.bot = bot
        self.webhook = None

    async def _send_webhook(self, content: str, username: str, avatar_url: str) -> None:
        """Send a webhook to the #sketchbook-comments channel."""
        if self.webhook is None:
            self.webhook = await self.bot.fetch_webhook(constants.Webhooks.sketchbook_comments)

        try:
            await self.webhook.send(
                content=content,
                username=username,
                avatar_url=avatar_url
            )
        except discord.HTTPException:
            log.exception("Failed to send a message to the #sketchbook-comments webhook.")

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
    async def on_message(self, message: Message) -> None:
        """
        Does this message belong in the #sketchbook channel?

        If not, we should relay that message to #sketchbook-comments and then delete it from #sketchbook.
        """
        ctx = await self.bot.get_context(message)

        # If this is an actual sketch or the message came from a bot, no action required.
        if not self._bad_sketch(message) or ctx.author.bot:
            return

        # We're still here? Okay, we need to relay this message to #sketchbook-comments and then delete it.
        await self._send_webhook(
            content=message.content,
            username=message.author.display_name,
            avatar_url=message.author.avatar_url
        )
        await message.delete()


def setup(bot: Bot) -> None:
    """
    This function is called automatically when this cog is loaded by the bot.

    It's only purpose is to load the cog above, and to pass the Bot instance into it.
    """
    bot.add_cog(Sketchbook(bot))
    log.info("Cog loaded: Sketchbook")
