from kivy.app import App
from kivy.logger import Logger
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager
from .screens import ChangeScreen


class EManagerApp(App):
    title = 'Email Manager'
    theme_cls = ThemeManager()
    theme_cls.primary_pallete = 'Red'

    manager = ObjectProperty('')
    toolbar = ObjectProperty('')

    def build(self):
        # self.manager = self.root.ids.manager
        # self.toolbar = self.root.ids.toolbar
        return self.root

    def on_start(self):
        '''Ao abrir a app...'''
        self.goto(ChangeScreen.INITIAL)

    def goto(self, change_screen, **kw):
        '''
        Ir para uma nova tela.
        '''
        self.manager.switch_to(change_screen.screen(self, **kw))

    def on_stop(self):
        ''' Ao fechar a app...'''
        Logger.info('Fechando Aplicação')
