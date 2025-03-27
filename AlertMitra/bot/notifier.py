import os
import telebot

# Load Telegram Bot Token from environment variables
BOT_TOKEN = os.getenv("7904429925:AAHeB9Al9fA3GlULAEDTJHlt1sk9novDuok")
CHAT_ID = os.getenv("1632633256")

bot = telebot.TeleBot("7904429925:AAHeB9Al9fA3GlULAEDTJHlt1sk9novDuok")

def send_telegram_alert(title, summary):
    """
    Sends a disaster alert to the Telegram chat.
    """
    message = f"🚨 *Disaster Alert!* 🚨\n\n*{title}*\n{summary}"
    bot.send_message(CHAT_ID, message, parse_mode="Markdown")

if __name__ == "__main__":
    print("Notifier module ready for sending alerts.")
