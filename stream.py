# python
import os
import twitter
import requests


""" endpoint declaration """
BASE_ENDPOINT = 'https://api.telegram.org/bot'
SEND_MESSAGE_ENDPOINT = '/sendMessage'
BOT_ACCESS_TOKEN = os.environ.get('BOT_ACCESS_TOKEN')

api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                  consumer_secret=os.environ.get('CONSUMER_SECRET'),
                  access_token_key=os.environ.get('ACCESS_TOKEN_KEY'),
                  access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET'))

# Change chat_id to '@YourBotName' or your_id
def stream_fun():
    for item in api.GetUserStream():
        if item.has_key('id'):
            text =  item['text']
            print text
            payload = {
                'chat_id': '@YourBotName',
                'text': text,
            }
            resp = requests.post('{}{}{}'.format(
                BASE_ENDPOINT,
                BOT_ACCESS_TOKEN,
                SEND_MESSAGE_ENDPOINT), data=payload)


if __name__=='__main__':
    stream_fun()
