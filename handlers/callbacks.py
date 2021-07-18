from aiogram.utils.markdown import fmt
from aiogram import types
from dispatcher import dp
import config
import db

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
	"""
		Команда /start с кнопками
	"""
	# --- Кнопки ---
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button = ["Авторизация 🔐"]
	markup.add(*button)
	
	text = fmt.text(fmt.hbold(fmt.hitalic(fmt.hlink(message.from_user.first_name, f"t.me/{message.from_user.username}"))), "чем могу помочь?")
	await message.bot.send_message(message.chat.id, text, reply_markup=markup)

@dp.message_handler(lambda message: message.text == "Авторизация 🔐")
@dp.message_handler(commands=["reg"])
async def auth_command(message: types.Message):
	"""
		Регистреция нового аккаунта
	"""
	data = message.text.split()

	if len(data) == 4:
		db.auth_user(first_name=data[1], last_name=data[2], password=data[3])
		await message.answer("Ваши данные успешно сохранены!")

	else:
		text = fmt.text(fmt.hbold("Пример:"), fmt.hitalic("/reg Имя Фамилия Пароль"))
		await message.bot.send_message(message.chat.id, "<b>Пример:</b>\n <i>/reg Имя Фамилия Пароль</i>", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(content_types=["text"])
async def random_text(message: types.Message):
	await message.answer("Неизвестная команда ❌")
