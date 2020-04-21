#! -*- coding: utf-8 -*-

__author__ = 'Desnown'
__date__ = '03/2019'

#IMPORT
# from imapclient import IMAPClient
from tools_mail import connect_smtp, PROVEDOR



class READMail(object):
    def __init__(self, host):
        #Connect
        self._imap_obj = connect_imap(host):
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
            #Logando no servidor
            self._imap_obj.login(self.name, self._password)
            return "Logado."

        except Exception as er:
            return er


    def Log_Out(self, ):
        '''
        Terminar a seção.
        '''

        try:
            self._imap_obj.logout()
            return "Deslogado."
        except Exception as er:
            return er


    # TERMINAR
    def Search_Email(self, folder=''):
        '''
        Metodo para "pesquisar" as pastas que estão desponível no servidor de
        email do usuário
        '''

        try:
            folder = self._imap_obj.list_folders(folder)
            # Irei implementar depois com 'Chaves de pesquisa'
            print(folder) # DEBUG

        except Exception as er:
            return er    