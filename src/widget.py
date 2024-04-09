from src.masks import mask_account_number, mask_card_number


def convert_date(input_date: str) -> str:
    """
    Функция выдает нам дату.
    """
    date_parts = input_date.split("T")[0].split("-")
    return f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"


def number_or_account(user_input: str) -> str:
    """
    Функция определяет работаем мы с счетом или картой.
    """
    if "Счет" in user_input:
        return mask_account_number(user_input)
    else:
        return mask_card_number(user_input)
