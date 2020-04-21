#! -*- coding: utf-8 -*-

__author__ = 'Desnown'
__date__ = '03/2019'


#IMPORTS
#Lib para logar e deslogar do provedor e enviar e-mails.
from smtplib import (SMTPAuthenticationError,
                    SMTPSenderRefused, SMTPServerDisconnected)

from pdb import set_trace # DEBUG
from tools_mail import connect_smtp, PROVEDOR

#Descobrir o nome do arquivo
from os.path import basename

#Class for generating application/* MIME documents.
from email.mime.application import MIMEApplication

#Base class for MIME multipart/* type messages.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#COMMASPACE e usada para unir uma lista de muitos endereços de email
#em uma string para inserção na mensagem
from email.utils import COMMASPACE, formatdate
#from pdb import set_trace


#VARS
_upi = "Usuario e/ou senha incorreta"

_pams = """Você precisa habilitar a opcão
    "PERMITIR APLICATIVOS MENOS SEGUROS" em sua conta!!!
    Habilite pelo seguinte link:
    https://myaccount.google.com/lesssecureapps?pli=1"""


class SENDMail(object):
    def __init__(self, host):
        #Connect
        self._smtp_obj = connect_smtp(host)
        self.host_name = PROVEDOR
        #Log_In
        self.name = ''
        self._password = ''


    def Log_In(self, name, password):
            '''
            Metodo usado para logar usando o nome e a senha do usuario.
            '''

            self.name = name
            self._password = password

            try:
                #fazendo login com a metodo "login()"
                self._smtp_obj.login(self.name, self._password)
                return "Logado."

            except SMTPAuthenticationError:
                return _upi
            except SMTPSenderRefused:
                return  _pams


    def Send_Mail(self, send_to,title, assunto, files=None):
            '''
            Metodo responsavel por enviar o email para
            alguem(informado pelo usuario)
            '''

            #Instanciando um objeto para juntar varias partes de um email:
            #De quem, para quem, data e conteudo
            self.msg = MIMEMultipart()
            self.msg['From'] = self.name

            if type(send_to) is list  and len(send_to) > 1:
                #Juntando a sting(caso ela esteja separada por espaço)
                self.msg['To'] = COMMASPACE.join(send_to)
            #Hora '-'
            self.msg['Date'] = formatdate(localtime=True)
            self.msg['Subject'] = title
            #Texto do email
            #Inserir From, To, Date, Subject ao email.
            self.msg.attach(MIMEText(assunto))

            if files is not None:
                for file in files:
                    with open(file, "rb") as fl:
                        part = MIMEApplication(
                            fl.read(),
                            Name=basename(file))
                        #Apresentação do corpo de resposta c/
                            #um arquivo para baixar
                        part['Content-Disposition']='attachment;\
                            filename="%s"'% basename(file)
                        #Inserindo um anexo.
                        self.msg.attach(part)

            try:
                #Enviando email com sendmail
                self._smtp_obj.sendmail(self.name,
                                        send_to,
                                        self.msg.as_string())

                # email_send = True
                return "Email Enviado."

            except SMTPSenderRefused:
                return  _upi


    def Log_Out(self):
            '''
            Leave a section.
            '''
            try:
                self._smtp_obj.quit()
                return "Deslogado."
            except Exception as er:
                return er


    # def _Info(self):
    #     '''
    #     It will only be used by the terminal(for a while)

    #     Some Information about the last email sent:
    #     From, to, files sent, day and hour.
    #     '''

    #     if len(self.files) > 1:
    #         self.files = self.files.join(",")
    #     if not self.email_send:
    #         print("Você não enviou nenhum e-mail. ")
    #     else:
    #         print("""+----------------------------+
    # | Informações sobre o Email. |
    # +============================+
    # From: %s
    # To: %s
    # Files Sent: %s
#     Day: %d
#     Hour: %d""" %(self.name,self.send_to, self.files,
# self.msg["Date"][0:16],
# self.msg["Date"][17:25]"""
