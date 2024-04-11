def mask_card_number(user_card_number: str) -> str:
    """
    Функция принимает номер банковской карты и возвращает ее маску.
    """
    user_card = user_card_number.split()
    number = user_card[-1]
    card_name = user_card[:-1]
    masked_number = " " + number[:4] + " " + number[4:6] + "** **** " + number[12:]
    return " ".join(card_name) + masked_number


def mask_account_number(user_account_number: str) -> str:
    """
    Функция принимает номер счета и возвращает маску счета.
    """
    masked_number = "**" + user_account_number[-4:]
    return f"Счет {masked_number}"
