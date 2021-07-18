from aiogram import types
from dispatcher import dp
import config
import db

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
	"""
		Команда /start с кнопками
	"""
	# Кнопки
	button = types.KeyboardButton(text="Авторизация 🔐")
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button)

	text = f"""<i><b><a href="t.me/{message.from_user.username}">{message.from_user.first_name}</a></b></i>, чем могу помочь?"""
	await message.bot.send_message(message.chat.id, text, reply_markup=markup)

@dp.message_handler(lambda message: message.text == "Авторизация 🔐")
@dp.message_handler(commands=["reg"])
async def auth_command(message: types.Message):
	"""
		Регистреция нового аккаунта
	"""
	data = message.text.split()

	if len(data) == 4:
		db.auth_user(
			first_name=data[1],
			last_name=data[2],
			password=data[3]
		)
		await message.answer("Ваши данные успешно сохранены!")

	else:
		remove_button = types.ReplyKeyboardRemove()
		await message.bot.send_message(
			message.chat.id,
			"<b>Пример:</b>\n <i>/reg Имя Фамилия Пароль</i>",
			reply_markup=remove_button
		)

@dp.message_handler(commands=["get_app"])
async def get_app_command(message: types.Message):
	await message.bot.send_message(
		message.chat.id,
		""
	)

@dp.message_handler(content_types=["text"])
async def random_text(message: types.Message):
	await message.answer("Неизвестная команда ❌")
