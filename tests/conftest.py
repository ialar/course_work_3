import pytest


@pytest.fixture
def test_data():
    return [{
        "id": 957763565,
        "state": "EXECUTED",
        "date": "2019-01-05T00:52:30.108534",
        "operationAmount": {
            "amount": "87941.37",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 46363668439560358409",
        "to": "Счет 18889008294666828266"
    },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        },
        {
            "id": 615064591,
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {
                "amount": "77751.04",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "to": "Счет 84163357546688983493"
        },
        {
            "id": 608117766,
            "state": "EXECUTED",
            "date": "2018-10-08T09:05:05.282282",
            "operationAmount": {
                "amount": "77302.31",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 6527183396477720",
            "to": "Счет 38573816654581789611"
        },
        {
            "id": 484201274,
            "state": "EXECUTED",
            "date": "2019-04-11T23:10:21.514616",
            "operationAmount": {
                "amount": "62621.51",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "МИР 8193813157568899",
            "to": "МИР 9425591958944146"
        },
        {
            "id": 317987878,
            "state": "EXECUTED",
            "date": "2018-01-13T13:00:58.458625",
            "operationAmount": {
                "amount": "55985.82",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 8906171742833215",
            "to": "Visa Platinum 6086997013848217"
        },
        {
            "id": 72122709,
            "state": "EXECUTED",
            "date": "2018-12-18T17:07:09.800800",
            "operationAmount": {
                "amount": "19683.25",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 86675623828180311969",
            "to": "Счет 15351391408911677994"
        },
        {
            "id": 172864002,
            "state": "EXECUTED",
            "date": "2020-12-28T23:10:35.459698",
            "operationAmount": {
                "amount": "49192.52",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 96231448929365202391"
        }]
