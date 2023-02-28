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

@app.post("/")
def index():
    

    return" <tr><td><a webhook='https://sharqakademiyasi.pythonanywhere.com/webhook'>Watermelon</a></td></tr>"
@app.route('/webhook', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return {'GET': 200}

    elif request.method == 'POST':
        # get data from request
      

        # convert data to Update obj
     

        # Dispatcher
        dp: Dispatcher = Dispatcher(bot, None, workers=0)

        # handlers
        dp.add_handler(CommandHandler('start',start))
        # Add handler for photo message
        
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
    

#   dp.add_handler(CallbackQueryHandler(query))
        return {'POST': 200}

if __name__ == '__main__':
    
    app.run()
