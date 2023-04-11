from aiogram import executor

from loader import dp, db
# Don't delete this unused import, without them nothing will work
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Creating Database:
    await db.create()
    # await db.drop_users()
    await db.create_table_users()

    # Default commands (/start va /help)
    await set_default_commands(dispatcher)

    # inform the administration that the bot has started
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
