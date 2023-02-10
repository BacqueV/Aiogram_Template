from aiogram import executor

from loader import dp, db
# don't delete this unused imports, without them nothing will work
import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # simple commands (/start & /help)
    await set_default_commands(dispatcher)

    # creating db:
    try:
        db.create_table_users()
    except Exception as err:
        print(err)

    # notify the admin that the bot has started
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
