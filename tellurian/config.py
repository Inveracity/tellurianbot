from os import environ

class Error(Exception):
    pass


class MissingToken(Error):
    pass

class Config:

    @property
    def token(self):
        self.sketchbook = 649897278374412289

        discord_token = environ.get("TELLURIAN_DISCORD_TOKEN", None)
        if discord_token:
            return discord_token

        else:
            raise MissingToken

