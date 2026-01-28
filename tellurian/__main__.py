import logging

import discord
from discord.ext.commands import Bot, when_mentioned_or

from tellurian import constants
from tellurian.utils.exceptions import MissingToken

log = logging.getLogger(__name__)

# Initialize the bot
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = Bot(
    command_prefix=when_mentioned_or(
        constants.Bot.prefix
    ),  # Invoked commands must have this prefix
    activity=discord.Game(name="blast beats at 240 BPM"),
    case_insensitive=True,
    max_messages=10_000,
    intents=intents,
)


# Load extensions during bot setup
async def setup_hook():
    await bot.load_extension("tellurian.cogs.sketchbook")


bot.setup_hook = setup_hook

# Validate the token
token = constants.Bot.token

if token is None:
    raise MissingToken(
        "No token found in the TELLURIAN_DISCORD_TOKEN environment variable!"
    )

# Start the bot
log.info(f"== All systems nominal. Bot is go for launch. ==")
bot.run(token)
