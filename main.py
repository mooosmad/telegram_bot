from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Que peut faire ce Bot ?

C’est un bot qui envoi de belle photos de chiens, si tu veux de jolies photos de chiens c’est ici.

Envoi /start pour commencer à utiliser le bot.
Parle au bot en envoyant /bop pour recevoir les images.
Pour arrêter le Bot envoi /stop.
Amuse toi bien 😌 """)

@run_async
def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('YOUR TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
