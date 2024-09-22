import asyncio
from aiogram import Bot,Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from config import API_TOKEN

#Вставьте сюда свой токен
TOKEN = API_TOKEN

#Создание обьекта бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

#Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message:Message):
    await message.answer("Привет")

#Функция для запуска бота
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

#Запуск бота
if __name__ == "__main__":
    asyncio.run(main())


