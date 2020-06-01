"""Various Tellurian-specific exceptions, such as NotMetalEnoughError."""


class Error(Exception):
    pass


class MissingToken(Error):
    pass


class NotMetalEnoughError(Error):
    pass
