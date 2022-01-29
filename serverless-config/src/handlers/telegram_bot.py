import json
import os

import requests

from bot_command_handler import BotCommandHandler

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
USER_ID = os.environ['PERMITTED_USER_ID']
BASE_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)

handler = BotCommandHandler()


def handle(event, context):
    try:
        data = json.loads(event['body'])
        chat_id = str(data['message']['chat']['id'])

        print('UserID: ' + chat_id)
        if chat_id != USER_ID:
            print('Unauthorized user ID: ' + chat_id)
            return {'statusCode': 200}

        message = str(data['message']['text'])

        response = handler.handle(message)

        data = {'text': response, 'chat_id': chat_id}
        url = BASE_URL + '/sendMessage'
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {'statusCode': 200}
