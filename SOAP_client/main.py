import requests
import xml.etree.ElementTree as Et

# Кодування кольорів для консолі
GREEN = '\033[92m'
BLUE = '\033[94m'
NORMAL = '\033[0m'
RED = '\033[91m'

if __name__ == '__main__':
    choice = None
    number = None
    while True:
        try:
            # Вибір типу запиту
            choice = input('Choose one from two options(Write number): [0]NumberToWords or [1]NumberToDollars: ')

            # Перевірка введених даних
            if choice not in ['0', '1']:
                raise ValueError("Input data must be number 0 or 1")

            # Якщо все добре, то виходимо з циклу
            break

        except ValueError as e:
            # Якщо ввід був некоректним, виводимо помилку з повідомленням та продовжуємо цикл
            print(str(e))
            continue

    while True:
        try:
            # Ввід числа для перетворення
            number = input('Enter number for conversion: ')

            # Перевірка введених даних
            if any(n.isalpha() for n in number):
                raise ValueError("Input data must be a number")

            # Якщо все добре, то виходимо з циклу
            break

        except ValueError as e:
            # Якщо ввід був некоректним, виводимо помилку з повідомленням та продовжуємо цикл
            print(str(e))
            continue

    # Масив для вибору опції в body та масив для виводу результатів
    s_body = ['ubiNum', 'dNum']
    s_result = ['NumberToWordsResult', 'NumberToDollarsResult', ' in words is ', ' in dollars is ']

    # Основне тіло запиту
    url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso"
    headers = {'content-type': 'text/xml'}
    body = f"""<?xml version="1.0" encoding="utf-8"?>
              <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                  <soap:Body>
                      <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
                          <{s_body[int(choice)]}>{number}</{s_body[int(choice)]}>
                      </NumberToWords>
                  </soap:Body>
              </soap:Envelope>"""

    try:
        # Відсилання запиту на сервер та отримання відповіді
        response = requests.post(url, data=body, headers=headers)

        # Парсинг та перевірка на fault
        root = Et.fromstring(response.content)
        faultstring = root.find('.//{http://schemas.xmlsoap.org/soap/envelope/}Fault/faultstring')

        # Якщо faultcode присутній, виводимо повідомлення про помилку. Інакше виводимо отримані дані
        if faultstring is not None:
            raise ValueError(f'{RED}{faultstring.text}')

        result = root.find('.//{http://www.dataaccess.com/webservicesserver/}' + s_result[int(choice)])
        print(f'{GREEN}{number}{NORMAL}{s_result[int(choice) + 2]}{BLUE}{result.text}')

    except ValueError as e:
        # Якщо faultcode присутній, виводимо помилку
        print(str(e))
