import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f'Привет, {html.bold(message.from_user.full_name)} моя любовь!', reply_markup = ease_link_kb())

def ease_link_kb():
        inline_kb_list = [
            [InlineKeyboardButton(text="Нажми на меня", web_app = WebAppInfo (url='https://www.jetbrains.com/ru-ru/code-with-me/buy/?section=personal&billing=monthly'))],
            [InlineKeyboardButton(text="Не нажимай", url='tg://resolve?domain=yakvenalexx')]
        ]
        return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


async def main() -> None:
    bot = Bot(token='7727541355:AAH-Wx8ab4RniGhnaG5HovsH9xMivhuuEvs', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())