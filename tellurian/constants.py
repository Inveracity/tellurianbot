import os
from typing import Optional


class Bot:
    """Constants relating to the bot itself."""
    token: Optional[str] = os.environ.get("TELLURIAN_DISCORD_TOKEN")
    prefix: str = "!"


class Channels:
    """Channel IDs that are relevant for this community."""
    # sketchbook: int = 649897278374412289
    sketchbook: int = 705109372983836672
