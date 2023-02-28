import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from main import (
    start,
    biz,
    tarmoqlar,
    query
)


app = Flask(__name__)

# bot
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)


@app.route('/webhook', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return {'GET': 200}

    elif request.method == 'POST':
        # get data from request
      

        # convert data to Update obj
     

        # Dispatcher
 

        # handlers
        dp.add_handler(CommandHandler('start',start))
        # Add handler for photo message
        #dp.add_handler(MessageHandler(Filters.photo,photo))
        dp.add_handler(MessageHandler(Filters.text("ijtimoiy tarmoqlar"),tarmoqlar))
        dp.add_handler(MessageHandler(Filters.text('Main menu'),start))
        dp.add_handler(MessageHandler(Filters.text("Biz Bilan Bog'lanish"),biz))
        #dp.add_handler(MessageHandler(Filters.text('📞 Contact'),contact))
        #dp.add_handler(MessageHandler(Filters.text('Main menu'),start))
        #dp.add_handler(CallbackQueryHandler(phone_list,pattern='phone_list'))
        #dp.add_handler(CallbackQueryHandler(phone,pattern='phone'))
        #dp.add_handler(CallbackQueryHandler(add_cart,pattern='add_cart'))

        dp.add_handler(CallbackQueryHandler(query))

        # process update
        dp.process_update(update=update)

#   dp.add_handler(CallbackQueryHandler(query))
        return {'POST': 200}

bot=Bot(TOKEN)


#print(bot.set_webhook('https://sharqakademiyasi.pythonanywhere.com/webhook'))
#print(bot.delete_webhook())

print(bot.get_webhook_info())

