import asyncio
import datetime
from aiogram import Bot, Dispatcher, executor, filters, types
from PIL import Image, ImageDraw, ImageFont

API_TOKEN = '1993748786:AAE2xZJQBjVIumiEZhub6zf6nSyKTfRv9RI'

bot = Bot(token=API_TOKEN,  parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


font = ImageFont.truetype("fonts/MontserratMd.ttf", 55)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    username = message.from_user.full_name
    salomlashuv = f"<b>Assalomu Alaykum {username}!😎</b>\n\nMen Mustaqillik tabrigi botiman!\n " \
                  f"Menga ismingizni yuboring, men ismingiz tushurilgan tabrik rasmni yuboraman!"

    await message.reply(salomlashuv)


@dp.message_handler()
async def tabrik(message: types.Message):
    x = datetime.datetime.now()
    ksdsms = (x.strftime("%d%H%M%S%f"))
    text = message.text
    id = message.from_user.id
    rasm = Image.open("Images/main.jpg")
    d = ImageDraw.Draw(rasm)
    d.text((521, 895), text, fill="white", anchor="mb", font=font)

    await message.reply("Biroz kuting, tez orada tayyor bo'ladi...")

    # Wait a little...
    await asyncio.sleep(1)
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    rasm.save(f"Exports/User_{id}_{ksdsms}.jpg")
    (media.attach_photo(types.InputFile(f"Exports/User_{id}_{ksdsms}.jpg"), 'Tayyor!'))

    await message.reply_media_group(media=media)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
