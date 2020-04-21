#! -*- coding: utf-8 -*-


def validate_email(email, provedor):
    '''
    Valida o email
    '''
    if not all(str.isalpha(item) for item in [email, provedor]):
        raise TypeError("Somente Strings(str)")

    if not email.endswith(f'@{provedor}.com'):
            return f"Favor, digite um email do provedor que você escolheu:\
 {provedor.title()}"
