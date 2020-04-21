from kivy.lang import Builder
from .basic import BasicScreen
from ..classes.tools_mail import PROVEDORES


Builder.load_string('''
<InitialScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: 10
        pos_hint: {'top': 1.375}

        canvas.before:
            Color:
                rgba: [1,1,1,1]
            Rectangle:
                size: self.size
                source: 'Imagens/obra_prima.png'

        MYFillRoundFlatIconButton:
            text: 'Gmail'
            icon: 'gmail'

        MYFillRoundFlatIconButton:
            text: 'Hotmail'
            icon: 'microsoft'

        MYFillRoundFlatIconButton:
            text: 'Outlook'
            icon: 'outlook'
''')


class InitialScreen(BasicScreen):
    '''
    Tela inicial.
    '''
    provedores = PROVEDORES
