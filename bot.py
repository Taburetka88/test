import asyncio

from aiogram import Bot, Dispatcher , types, F
from aiogram.filters import CommandStart
from aiogram.types import Message



bot = Bot(token = '7218056575:AAFfQg3l9GLvA1peScMtnjuwTkjTJpsciYY')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    kb = [
        [types.KeyboardButton(text='tg id')],
        [types.KeyboardButton(text='ничего')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Привет',reply_markup=keyboard)
@dp.message(F.text == 'tg id')
async def get_id(message: Message):
     await message.answer(f"Ваш ID: {message.from_user.id}")
async def start_bot():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(start_bot())