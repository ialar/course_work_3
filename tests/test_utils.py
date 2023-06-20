import pytest
from utils import get_data, get_filtered_data, get_last_values, format_bill_output, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert len(data) == 7


def test_get_last_values(test_data):
    data = get_last_values(test_data, 3)
    assert [i['date'] for i in data] == \
           ["2020-12-28T23:10:35.459698", "2019-07-13T18:51:29.313309", "2019-04-11T23:10:21.514616"]


@pytest.mark.parametrize('test_input, expected', [
    ('Счет 46363668439560358409', 'Счет **8409'),
    ('Visa Platinum 1246377376343588', 'Visa Platinum 1246 37** **** 3588')
])
def test_format_bill_output(test_input, expected):
    assert format_bill_output(test_input) == expected


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == \
           ['05.01.2019 Перевод со счета на счет\nСчет **8409 -> Счет **8266\n87941.37 руб.\n',
            '13.07.2019 Перевод с карты на счет\nMaestro 1308 79** **** 7170 -> Счет **8612\n97853.86 руб.\n',
            '12.09.2018 Перевод организации\nVisa Platinum 1246 37** **** 3588 -> Счет **1657\n67314.70 руб.\n',
            '14.10.2018 Перевод с карты на счет\nMaestro 3928 54** **** 4026 -> Счет **3493\n77751.04 руб.\n',
            '08.10.2018 Перевод с карты на счет\nVisa Gold 6527 18** **** 7720 -> Счет **9611\n77302.31 USD\n',
            '11.04.2019 Перевод с карты на карту\nМИР 8193 81** **** 8899 -> МИР 9425 59** **** 4146\n62621.51 руб.\n',
            '13.01.2018 Перевод с карты на карту\n'
            'Visa Classic 8906 17** **** 3215 -> '
            'Visa Platinum 6086 99** **** 8217\n55985.82 USD\n',
            '18.12.2018 Перевод со счета на счет\nСчет **1969 -> Счет **7994\n19683.25 USD\n',
            '28.12.2020 Открытие вклада\nСчет **2391\n49192.52 USD\n']
