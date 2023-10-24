import telebot
from telebot import types
from telebot.types import WebAppInfo

bot = telebot.TeleBot("5175169529:AAFWRSHZGblFf5GNWdN3rMRDQF3iqRS11EE")
PAYMENTS_TOKEN = "401643678:TEST:0363ce47-d7c7-47d4-8491-170838062f73"

PRICE = {
    '1': [types.LabeledPrice(label='Item1', amount=80)],
    '2': [types.LabeledPrice(label='Item2', amount=100)],
    '3': [types.LabeledPrice(label='Item3', amount=100)],
    '4': [types.LabeledPrice(label='Item4', amount=100)],
    '5': [types.LabeledPrice(label='Item5', amount=80)],
    '6': [types.LabeledPrice(label='Item6', amount=100)]
}

@bot.message_handler(commands=['start'])
def start(message):
        mess = f"Привет, <b>{message.from_user.first_name}</b>👋 \n\nСамые вкусные сладости можно заказать по кнопке ниже😋👇"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Заказать', web_app=WebAppInfo(url='https://heyartemno.github.io/testtelegramwebapp/')))
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types='web_app_data')
def buy_process(web_app_message):
    bot.send_invoice(web_app_message.chat.id,
                           title='Laptop',
                           description='Description',
                           provider_token=PAYMENTS_TOKEN,
                           currency='rub',
                           need_email=True,
                           prices=PRICE[f'{web_app_message.web_app_data.data}'],
                           start_parameter='example',
                           payload='some_invoice')

@bot.pre_checkout_query_handler(lambda query: True)
def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
    bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message: types.Message):
    bot.send_message(message.chat.id, 'Заказ оформлен')

bot.polling()