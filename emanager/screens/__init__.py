from enum import Enum

from .initial import InitialScreen as Initial
from .sendmesage import SendMessageScreen as Send
from .screenlogin import LoginScreen as Login
from .settings import SettingsScreen as Settings


class ChangeScreen(Enum):
    INITIAL = Initial
    SENDMESAGE = Send
    SCREENLOGIN = Login
    SETTINGS = Settings

    def getscreen(self, app, **kw):
        return self.value(app, **kw)
