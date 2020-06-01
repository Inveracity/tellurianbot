import os
from typing import Optional


class Bot:
    """Constants relating to the bot itself."""
    token: Optional[str] = os.environ.get("TELLURIAN_DISCORD_TOKEN")
    prefix: str = "!"


class Channels:
    """Channel IDs that are relevant for this community."""
    sketchbook: int = 649897278374412289
    sketchbook_comments: int = 716630834991333427


class Webhooks:
    """Webhook IDs that are relevant for this community."""
    sketchbook_comments: int = 717094632089190461
