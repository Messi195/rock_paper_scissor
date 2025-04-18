import random
import telebot
from telebot import types

API_TOKEN: str = 'YOUR_API_TOKEN_HERE'  # Replace with your real token

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')
rps: list[str] = ["📄", "🗿", "✂️"]

# Mapping of what beats what
win_map: dict[str, str] = {
    "🗿": "✂️",
    "✂️": "📄",
    "📄": "🗿"
}


@bot.message_handler(commands=['start'])
def game_play(message: types.Message) -> None:
    """
    Starts the game by sending a custom keyboard with Rock, Paper, Scissors options.
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(choice) for choice in rps])
    bot.send_message(message.chat.id, '🎮 Rock, Paper, Scissors game! Choose your move:', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handle_move(message: types.Message) -> None:
    """
    Handles user's move, generates bot's move, and sends the result.
    """
    user_choice: str = message.text
    if user_choice not in rps:
        bot.send_message(message.chat.id, "Please choose a valid option: 🗿, 📄 or ✂️")
        return

    bot_choice: str = random.choice(rps)
    bot.send_message(message.chat.id, f"My choice: {bot_choice}")

    if user_choice == bot_choice:
        result = "It's a draw! 🤝"
    elif win_map[user_choice] == bot_choice:
        result = "You win! 🎉"
    else:
        result = "I win! 😎"

    bot.send_message(message.chat.id, result)


if __name__ == '__main__':
    bot.polling()
