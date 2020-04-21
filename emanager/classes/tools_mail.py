#! -*- coding: utf-8 -*-


# IMPORT
from smtplib import SMTP
from imapclient import IMAPClient
from .decors import validate_email, validate_func

# VARS
_PROVEDORES_SMTP = {
    'gmail': 'smtp.gmail.com',
    'outlook': 'smtp-mail.outlook.com',
    'hotmail': 'smtp-mail.outlook.com'}

_PROVEDORES_IMAP = {
    'gmail': 'imap.gmail.com',
    'outlook': 'imap-mail.outlook.com',
    'hotmail': 'imap-mail.outlook.com'}

PROVEDORES = ['Gmail', 'Hotmail', 'Outlook']
PROVEDOR = ''


def connect_smtp(host):
    '''
    Funcao responsável por conectar com o servidor via protocolo SMTP/IMAP
    '''

    global PROVEDOR

    PROVEDOR = host

    while True:
        try:
            _provedor = _PROVEDORES_SMTP[host]
            # Conectando no servidor
            smtp_obj = SMTP(_provedor, 587)
            # Iniciando a Criptografia
            smtp_obj.starttls()
            break
        except Exception as er:
            return er
    return smtp_obj


def connect_imap(host):
    '''
    Funcao responsavel por conectar com o servidor via protocolo IMAP
    '''

    while True:
        try:
            # Conectando no servidor
            _provedor = _PROVEDORES_IMAP[host]
            imap_obj = IMAPClient(_provedor, ssl=True)
            break
        except Exception as er:
            return er

    return imap_obj
