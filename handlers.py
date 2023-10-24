from main import bot, dp
from aiogram import types
from aiogram.types import WebAppInfo
from aiogram.dispatcher.filters import Command

PRICE = {
    '1': [types.LabeledPrice(label='Item1', amount=80)],
    '2': [types.LabeledPrice(label='Item2', amount=100)],
    '3': [types.LabeledPrice(label='Item3', amount=100)],
    '4': [types.LabeledPrice(label='Item4', amount=100)],
    '5': [types.LabeledPrice(label='Item5', amount=80)],
    '6': [types.LabeledPrice(label='Item6', amount=100)]
}

@dp.message_handler(Command("start"))
async def start(message: types.Message):
        markup = types.InlineKeyboardMarkup()
        mess = f"Привет, <b>{message.from_user.first_name}</b>👋 \n\nСамые вкусные сладости можно заказать по кнопке ниже😋👇"
        markup.add(types.InlineKeyboardButton('Заказать', web_app=WebAppInfo(url='https://heyartemno.github.io/testtelegramwebapp/')))
        await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    await bot.send_invoice(web_app_message.chat.id,
                           title='Laptop',
                           description='Description',
                           provider_token='pay_token',
                           currency='rub',
                           need_email=True,
                           prices=PRICE[f'{web_app_message.web_app_data.data}'],
                           start_parameter='example',
                           payload='some_invoice')

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id, 'Заказ оформлен!')

