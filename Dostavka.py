import asyncio
import logging
import sys
from os import getenv

import aiogram.types.reply_keyboard_markup
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
    await message.answer(f'Привет, {html.bold(message.from_user.full_name)}!', reply_markup = ease_link_kb())

def ease_link_kb():
        inline_kb_list = [
            [InlineKeyboardButton(text="Сделать заказ", url='https://github.com/abulfatasin/magazin/index.html')],
            [InlineKeyboardButton(text="Мой Telegram", url='tg://resolve?domain=yakvenalexx')],
            [InlineKeyboardButton(text="Веб приложение", web_app=WebAppInfo(url="https://tg-promo-bot.ru/questions"))]
        ]
        return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


async def main() -> None:
    bot = Bot(token='5873479362:AAFQYvnNSCe6APaoZg6XaRZduM85HXXRSsU', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())