def get_mask_card_number(card_number):
    """Функция маскировки номера банковской карты"""
    x = str(card_number)
    return x[:6] + (len(x) - 10) * "*" + x[-4:]


def get_mask_account(account):
    """Функция маскировки номера банковского счета"""
    s = str(account)
    return "**" + s[-4:]
