import asyncio
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
from aiogram.types import Message,InputMediaPhoto
from config import API_TOKEN
import os

#Вставьте сюда свой токен
TOKEN = API_TOKEN

#Создание обьекта бота
bot = Bot(token=TOKEN)
dp = Dispatcher()


#Обработчик команды /start
@dp.message(Command("start"))
async def start_command_handler(message:Message):
    await message.answer("Привет")


@dp.message(Command("show"))
async def show_command_handler(message:Message):
    folder_path = "img/shoes"  # Папка с фотографиями

    # Получаем список всех файлов в папке
    image_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(('.jpg', '.jpeg', '.png'))]

    if image_paths:
        media_group = []  # Список для хранения фотографий как InputMediaPhoto

        for image_path in image_paths:
            if os.path.isfile(image_path):
                media_group.append(InputMediaPhoto(media=types.FSInputFile(image_path)))

            # Если есть фото, отправляем их все в одном сообщении
        if media_group:
            await message.answer_media_group(media_group)
        else:
            await message.answer("Не удалось загрузить фотографии.")
    else:
        await message.answer("Фотографии не найдены")



#Функция для запуска бота
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

#Запуск бота
if __name__ == "__main__":
    asyncio.run(main())


