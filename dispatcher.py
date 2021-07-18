from aiogram import Dispatcher, Bot
import config

bot = Bot(token=config.API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
