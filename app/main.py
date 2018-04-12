from functools import partial

import telepot

from app import constants

from app.modules.modules import textmodules
from app.modules.modules import photomodules
from app.modules.modules import gifmodules


def processor(text, modules):
    for module in modules:
        response = module.resolver(
            module.processor(text)
        )

        if response:
            return response


def on_chat_message(msg, bot):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']

        response = processor(txt, textmodules)
        if response:
            bot.sendMessage(chat_id, response)

        response = processor(txt, photomodules)
        if response:
            bot.sendPhoto(chat_id, response)

        response = processor(txt, gifmodules)
        if response:
            bot.sendDocument(chat_id, response)


def listen():
    bot = telepot.Bot(constants.bot_token)
    bot.message_loop(partial(on_chat_message, bot=bot))

    print('Listening ...')
    import time

    while 1:
        time.sleep(10)


if __name__ == "__main__":
    listen()
