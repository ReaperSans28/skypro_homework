def filter_state(data, state='EXECUTED'):
    """
    Функция принимает список словарей и значение для ключа state (по умолчанию EXECUTED)
    возвращает список, содержащий только словари, у которых значение ключа state совпадает с переданным в функцию.
    """
    filtered_data = []
    for d in data:
        if d.get('state') == state:
            filtered_data.append(d)
    return filtered_data


def convert_date(date):
    """
    Функция раскидывает каждое значение даты в отдельную переменную.
    """
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])
    hour = int(date[11:13])
    minute = int(date[14:16])
    second = int(date[17:19])
    return year, month, day, hour, minute, second


def key_for_sort(x):
    """Функция выдает ключ для работы функции sort_by_date."""
    return convert_date(x['date'])


def sort_by_date(data, order='desc'):
    """
    Сортирует по времени
    """
    reverse = order.lower() == 'desc'
    return sorted(data, key=key_for_sort, reverse=reverse)
