from typing import Union


def mask_account_card(account_card: Union[str]) -> str:
    """Фуникция, которая умеет обрабатывать информацию как о картах, так и о счетах."""

    if account_card[0:4] == "Счет":
        return "Cчет" + " " + "**" + account_card[21:]
    else:
        return (
            account_card[:-16]
            + " "
            + account_card[-16:-12]
            + " "
            + account_card[-12:-10]
            + "**"
            + " "
            + "****"
            + " "
            + account_card[-4:]
        )


def get_date(date: Union[str]) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    return date[8:10] + "." + date[5:7] + "." + date[0:4]
