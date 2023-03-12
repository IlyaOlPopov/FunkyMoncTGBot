import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://aws.random.cat/meow'
BOT_TOKEN: str = '6264084630:AAGWsw7_dxh8EA3BiwyJ1Y070YkE9u-FrhM'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('

# TEXT: str = 'Привет, касатик!'
MAX_COUNTER: int = 20

offset: int = -2
counter: int = 0
timeout: int = 60
updates: dict
chat_id: int
cat_response: requests.Response
cat_link: str

while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cmd: str = result['message']['text']
            if cmd == "/start":
                TEXT: str = "Привет, " + result['message']['from']['first_name']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['file']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
