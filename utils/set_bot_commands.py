from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "brings the bot to the state quo"),
            types.BotCommand("help", "explains how does bot work"),
        ]
    )
