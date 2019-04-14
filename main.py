"""
the main script for running the telegram bot in python3.7
"""
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import random
import requests
#import json


TOKEN = "inserttokenhere"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
#OTLC telegram chat id
#CHATID = '-1001320128437'
PICS = ('https://dubsism.files.wordpress.com/2018/09/burt-reynolds-naked.jpg',
        'https://mfas3.s3.amazonaws.com/styles/grid-3_thumbnail_retina/s3/zardozsfw_0.jpg',
        'https://i.ebayimg.com/images/g/GzMAAOSwgkRVUSKD/s-l500.jpg')
KEVIN = ('https://goo.gl/maps/4nwWjyZi5Y82',
         'https://goo.gl/maps/8PAy8vgALgp',
         'https://goo.gl/maps/RhW3StqJWx72',
         'https://goo.gl/maps/8yiKtKEMGYR2')
HUMAN = 'CQADAQADrAADnXJhRNhVTrHIxfGZAg'


#def get_url(url):
#    contents = requests.get(url)
#    url = contents['url']
#    return url

#def get_json_from_url(url):
#    content = get_url(url)
#    js = json.loads(content)
#    return js


#def get_updates(offset=None):
#    url = URL + "getUpdates"
#    if offset:
#        url += "?offset={}".format(offset)
#    js = get_json_from_url(url)
#    return js


#def get_last_update_id(updates):
#    update_ids = []
#    for update in updates["result"]:
#        update_ids.append(int(update["update_id"]))
#    return max(update_ids)


#def send_message(text, chat_id):
#    text = urllib.parse.quote_plus(text)
#    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
#    get_url(url)


def cookie(bot, update):
    url = random.choice(PICS)
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url, caption="soft as a mouse's ear")


def areyoufriendly(bot, update):
    chat_id = update.message.chat_id
    bot.send_audio(chat_id=chat_id, audio=HUMAN)


def whereiskevin(bot, update):
    chat_id = update.message.chat_id
    text = random.choice(KEVIN)
    bot.sendMessage(chat_id=chat_id, text=text, caption="whew he's quick")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('givemeacookie', cookie))
    dp.add_handler(CommandHandler('areyoufriendly', areyoufriendly))
    dp.add_handler(CommandHandler('whereiskevin', whereiskevin))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
