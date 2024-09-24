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
    await message.answer("Привет! 👋\n\n"
        "Я бот, который поможет тебе купить кроссовки! 🏀👟\n\n"
        "Вот список команд, которые ты можешь использовать:\n"
        "👉 /show — Показать доступные кроссовки\n"
        "👉 /info — Узнать больше о нас\n"
        "👉 /info_bot — Информация о боте\n\n"
        "👉 /help — Связаться с продавцом\n\n"
        "Начни с команды /show, чтобы увидеть наши предложения!")

#Обработчик команды /info
@dp.message(Command("info"))
async def info_command_handler(message:Message):
    await message.answer("Ищешь выгодное предложение по поводу обуви? 👟\n\n"
        "✅Мы предлагаем **50% скидку** на любую пару обуви из магазина NewYorker! 🔥\n\n"
        "✅В наличии все размеры, и цены не превышают **100 zł**! 💸\n\n"
        "✅Кроме того, ты можешь получить **50 zł бонуса** от цены любой пары, если приведёшь друга!\n\n"
        "✅Работает доставка по Труймясту!🚘\n\n "
        "✅Не упусти возможность обновить свою коллекцию кроссовок по лучшим ценам!\n\n"
        "Если у тебя есть вопросы, всегда можно воспользоваться командой /help, чтобы связаться с продавцом.")

#Обработчик команды /help
@dp.message(Command("help"))
async def help_command_handler(message:Message):
    await message.answer("По всем интересующим вопросам писать:\n\n"
                        "🙋🏻‍♀️@tanyha_m_25\n"
                        "🙋🏼@boris_serheevich")


#Обработчик команды /info_bot
@dp.message(Command("info_bot"))
async def info_bot_command_handler(message:Message):
    await message.answer( "👋Я бот, который поможет тебе выгодно купить кроссовки! 👟\n\n"
        "💸 **Скидки, акции и отличные предложения** — всё, чтобы ты нашёл идеальную пару обуви.\n\n"
        "🔒 **Конфиденциальность**: я не собираю и не храню никаких данных о пользователях. Всё, что ты делаешь, остаётся между нами!\n\n"
        "❓ Если у тебя возникнут вопросы, просто используй команду /help, чтобы связаться с продавцом. Я всегда готов помочь!")


#Обработчик команды /show
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


