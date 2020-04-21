from kivy.lang import Builder
from .basic import BasicScreen


Builder.load_string('''
<SendMessageScreen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: [1,1,1,1]
            Rectangle:
                size: self.size
                source: 'Imagens/obra_prima.png'

        Label:
            text: app.root.get_screen('tela_login').ids.text_email.text

''')


class SendMessageScreen(BasicScreen):
    '''
    Classe responsavel por enviar uma mensagem para
    um determinado usuario.
    '''
    pass

