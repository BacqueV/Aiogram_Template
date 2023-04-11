from environs import Env

# environs library utilization
env = Env()
env.read_env()

# config data from .env file
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")


DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
