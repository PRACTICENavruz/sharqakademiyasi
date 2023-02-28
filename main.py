from flask import Flask ,request,jsonify
import requests
from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os

TOKEN = os.environ['TOKEN']


def start(update:Update,context:CallbackContext):

    chat_id=update.message.chat_id

    keyboar = ReplyKeyboardMarkup([
        ["Biz Bilan Bog'lanish"],
        ['ijtimoiy tarmoqlar']
    ]
    )
    bot=context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum  ',
    reply_markup=keyboar
    )
def biz(update:Update,context:CallbackContext):
    chat_id = update.message.chat.id

    keyboar = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='📞 Phone number',callback_data='number'),InlineKeyboardButton(text='📧 Email',callback_data='email')],
        [InlineKeyboardButton(text='📍 Location',callback_data='location'),InlineKeyboardButton(text='📌 Address',callback_data='address')],
        # [InlineKeyboardButton(text='📞 Phone number',url='txt')]

    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
def tarmoqlar(update:Update,context:CallbackContext):
    chat_id=update.message.chat_id
    Kanal3=InlineKeyboardButton(text="Guruhga Qo'shish",url='https://telegram.me/Sharq_Akademiyasi_bot?startgroup=start',callback_data='1')

    Kanal=InlineKeyboardButton(text='Telegram',url='https://t.me/sharq_Academy',callback_data='1')
    Kanal1=InlineKeyboardButton(text='Instagram',url='https://instagram.com/sharq.akademiyasi?igshid=YmMyMTA2M2Y=',callback_data='2')
    Kanal2=InlineKeyboardButton(text='Telegram chat',url='https://t.me/sharqakademiyasi',callback_data='3')
    keyboar=InlineKeyboardMarkup([
        [Kanal],
        [Kanal2],
        [Kanal1],
        [Kanal3]
    ])
    bot=context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text="Sharq Akademiyasining\nIjtimoiy Tarmoqlar ",
    reply_markup=keyboar)
def query(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    data = query.data
    bot = context.bot
    if data=='number':
        phone_1 ='Tel: +99883981918'
        phone_2 ='Tel: +99883981918'
        text = f'Our phone numbers:\n{phone_1}\n{phone_2}'
        bot.sendMessage(text=text,chat_id=chat_id)
    elif data=='email':
        email = 'Bizning elektron pochtamiz: sharqakademiyasi@gmail.com'
        bot.sendMessage(text=email,chat_id=chat_id)

    elif data=='address':
        address = "📍Manzil:  Samarqand Sagdiana massivi \n📍Mo'ljal: 4-son to'g'riqxona ro'parasida"
        bot.sendMessage(text=address,chat_id=chat_id)

    elif data=='location':
        # 39.644053, 66.973233

        lat = 39.65555
        lon = 66.91228
        bot.sendLocation(chat_id=chat_id,latitude=lat,longitude=lon)

    query.answer(" ")
    print(data)

"""
updater = Updater(token=TOKEN)
updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text("ijtimoiy tarmoqlar"),tarmoqlar))

updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text("Biz Bilan Bog'lanish"),biz))
#updater.dispatcher.add_handler(CallbackQueryHandler(phone_list,pattern='phone_list'))
#updater.dispatcher.add_handler(CallbackQueryHandler(phone,pattern='phone'))
#updater.dispatcher.add_handler(CallbackQueryHandler(add_cart,pattern='add_cart'))
updater.dispatcher.add_handler(CallbackQueryHandler(query))
# Add handler for photo message


updater.start_polling()
updater.idle()

"""
