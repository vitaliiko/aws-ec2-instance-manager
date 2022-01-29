import json
import os

import requests

from bot_command_handler import BotCommandHandler

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
BASE_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)

handler = BotCommandHandler()


def handle(event, context):
    try:
        data = json.loads(event['body'])
        message = str(data['message']['text'])
        chat_id = data['message']['chat']['id']

        response = handler.handle(message)

        data = {'text': response, 'chat_id': chat_id}
        url = BASE_URL + '/sendMessage'
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {'statusCode': 200}
