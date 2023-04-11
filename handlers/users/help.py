from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Commands: ",
            "/start - Starts the bot",
            "/help - Explains how does this bot work")
    
    await message.answer("\n".join(text))
