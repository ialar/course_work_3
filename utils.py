import json
from datetime import datetime


def get_data():
    """Возвращает исходный список операций"""
    with open('operations.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_filtered_data(data):
    """Возвращает отфильтрованный список по исполненным операциям,
    проверив наличие соответствующего ключа в словаре"""
    data = [i for i in data if 'state' in i and i['state'] == 'EXECUTED']
    return data


def get_last_values(data, last_values_quantity):
    """Возвращает определенное количество последних операций"""
    data = sorted(data, key=lambda operation: operation['date'], reverse=True)
    data = data[:last_values_quantity]
    return data


def format_bill_output(name_number):
    """Форматирует вывод счета / номера карты"""
    name_number = name_number.split()
    name, number = ' '.join(name_number[:-1]), name_number[-1]

    if len(number) == 16:
        number = f'{number[:4]} {number[4:6]}** **** {number[-4:]}'
    else:
        number = f'**{number[-4:]}'

    bill_output = f'{name} {number}'
    return bill_output


def get_formatted_data(data):
    """Возвращает список отформатированных операций"""
    formatted_data = []

    for operation in data:
        date = datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f")\
                       .strftime("%d.%m.%Y")
        description = operation['description']
        if 'from' in operation:
            sender = f"{format_bill_output(operation['from'])} -> "
        else:
            sender = ''
        recipient = format_bill_output(operation['to'])
        operation_amount = f"{operation['operationAmount']['amount']} " \
                           f"{operation['operationAmount']['currency']['name']}"

        formatted_data.append(f'{date} {description}\n'
                              f'{sender}{recipient}\n'
                              f'{operation_amount}\n')
    return formatted_data
