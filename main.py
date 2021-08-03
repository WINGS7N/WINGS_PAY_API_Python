import requests

# Ссылка на API WINGS PAY
api_url = 'https://wings.host/wings_pay/api/'
HEADERS = {
    "email": "test@test.test",  # Электронная почта аккаунта личного кабинета
    "pass": "12345678"  # Пароль от туда же
}


# Выдаёт баланс WINGS PAY
def get_balance():
    return requests.post(api_url + 'balance', headers=HEADERS).text


# Выдаёт массив, в первом поле ссылка на оплату, а во вротом QWP ID. QWP ID надо куда-то временно записывать,
# по QWP ID выполняется проверка платежа.
def create_pay():
    headers_copy = dict(HEADERS)
    request_headers = {
        "donateuser": "test",  # ник донатера
        "sum": "1",  # сумма перевода
        "successurl": "https://wings.host/wings_pay/api"  # ссылка успешной оплаты. Должна вести на страницу, которая
        # вызовет check_pay(QWP_ID), проверит платёж и выдаст донат.
    }
    headers_copy.update(request_headers)
    return requests.post(api_url + 'pay/qwp', headers=headers_copy).text


# Для проверки платежей по QWP ID.
# Выдаёт:
# donate_user - имя пользователя донатера
# sum - сумма оплаты
# status - статус оплаты. Если PAID, то пользователь оплатил.
# external_status - внешний статус оплаты, если WP_NULL, то проверка платежа ещё не проводилась, если CHECKED, проверяли
# external_status нужен для предотвращения повторных операций, этот статус автоматически меняется с WP_NULL на CHECKED
# после проверки.
def check_pay(QWP_ID):
    headers_copy = dict(HEADERS)
    request_headers = {
        "QWPID": QWP_ID
    }
    headers_copy.update(request_headers)
    return requests.post(api_url + 'pay/qwp/check', headers=headers_copy).text


# Как вызывать функции:

# Эта покажет баланс
print("Ваш баланс WINGS PAY: " + str(get_balance()))

# А эта выдаст ссылку на оплату и QWP ID
# print(create_pay())

print(check_pay("da0022cc-b2d5-4f3f-9b7f-84e2fd4692f6"))

# Удачи в интеграции такого же, по примеру, в PHP. Всё строится на POST запросах.
