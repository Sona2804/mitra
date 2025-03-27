import telebot
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.scraper import get_disaster_updates
from backend.summarizer import summarize_text
from backend.config import TELEGRAM_BOT_TOKEN
# Initialize Telegram Bot
bot = telebot.TeleBot("7904429925:AAHeB9Al9fA3GlULAEDTJHlt1sk9novDuok")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to Disaster Alert Bot! Use /latest to get recent disaster updates.")

@bot.message_handler(commands=['latest'])
def latest_alerts(message):
    alerts = get_disaster_updates()
    
    if not alerts:
        bot.reply_to(message, "No recent disaster alerts.")
        return
    
    response = "\n\n".join([f"🚨 {alert['title']}:\n{summarize_text(alert['details'])}" for alert in alerts])
    
    bot.reply_to(message, response)

# Start bot polling
if __name__ == "__main__":
    bot.polling()
