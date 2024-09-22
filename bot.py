import asyncio
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
from aiogram.types import Message
from config import API_TOKEN
import os

#Вставьте сюда свой токен
TOKEN = API_TOKEN

#Создание обьекта бота
bot = Bot(token=TOKEN)
dp = Dispatcher()


# Список путей к картинкам
# image_paths = [
#     'img/shoes/photo_1.jpg',
#     'img/shoes/photo_2.jpg',
#     'img/shoes/photo_3.jpg',
#     'img/shoes/photo_4.jpg',
#     'img/shoes/photo_5.jpg',
#     'img/shoes/photo_6.jpg',
#     'img/shoes/photo_7.jpg',
#     'img/shoes/photo_8.jpg'
# ]


#Обработчик команды /start
@dp.message(Command("start"))
async def start_command_handler(message:Message):
    await message.answer("Привет")


@dp.message(Command("show"))
async def show_command_handler(message:Message):
    photo_path = "img/shoes/photo_1.jpg"

    #Проверка на существование файла
    if os.path.isfile(photo_path):
        photo = types.FSInputFile(photo_path)
        await message.answer_photo(photo,caption="Фото кроссовок")
    else:
        await message.answer("Что-то пошло не так,на данный момент фотографии не доступны")  


#Функция для запуска бота
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

#Запуск бота
if __name__ == "__main__":
    asyncio.run(main())


