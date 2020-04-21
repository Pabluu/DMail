from kivy.lang import Builder
from kivy.properties import StringProperty
from .basic import BasicScreen


Builder.load_string('''
<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: [1,1,1,1]
            Rectangle:
                size: self.size
                source: 'Imagens/obra_prima.png'

        spacing: 5

        BarStatus:
            titulo: 'Tela Login'

        BoxLayout:
            orientation: 'vertical'
            spacing: 10
            pos_hint: {'top':1}

            Image:
                source: 'Imagens/log.png'

            MYTextFieldRound:
                id: text_email
                icon_right: 'face-outline'
                hint_text: 'exemplo@{}.com'.format(root.provedor)

            MYTextFieldRound:
                id: text_pwd
                icon_right: 'eye-off'
                password: True
                password_mask: '.'
                hint_text: 'Digite sua senha'
                icon_callback: root.show_password

            MDFillRoundFlatButton:
                text: 'Login'
                size_hint: [.50, None]
                height: dp(45)
                pos_hint: {'center_x': .5}
                on_release: root.login(root.ids.text_email, root.ids.text_pwd)

            Widget:
''')


class LoginScreen(BasicScreen):
    '''
    Classe responsavel por receber um email e uma senha
    e logar no servidor.
    '''
    provedor = StringProperty('')

    def show_password(self, field, button):
        field.password = not field.password
        field.focus = True
        button.icon = 'eye' if button.icon == 'eye-off' else 'eye-off'

    def login(self, user, pwd):
        if user and pwd == '':
            pass

        else:
            try:
                self.connect = Thread(
                    target=SENDMail,
                    args=[self.provedor]).start()

                self.connect.Log_In(user, pwd)
                App.get_running_app().root.current = 'send_mail'
            except Exception as error:
                return error
