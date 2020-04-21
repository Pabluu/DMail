from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


class BasicScreen(Screen):
    app = ObjectProperty(None)

    def __init__(self, app, **kw):
        super(BasicScreen, self).__init__(**kw)
        self.app = app
