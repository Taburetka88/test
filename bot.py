from aiogram import Bot, Dispatcher , types
from aiogram.filters import CommandStart
from aiogram.types import Message

API_TOKEN = '7218056575:AAFfQg3l9GLvA1peScMtnjuwTkjTJpsciYY'

bot = Bot(token = API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    kb = [
        [types.KeyboardButton(text='кнопка 1')],
        [types.KeyboardButton(text='кнопка 2')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Привет',reply_markup=keyboard)

