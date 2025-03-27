import os
import sys
import telebot
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.database import get_alerts
from backend.scraper import get_disaster_updates
BOT_TOKEN = os.getenv("BOT_TOKEN", "7904429925:AAHeB9Al9fA3GlULAEDTJHlt1sk9novDuok").strip()

# Check if the bot token is valid
if not BOT_TOKEN:
    raise ValueError("Error: BOT_TOKEN is missing or invalid!")
bot = telebot.TeleBot("7904429925:AAHeB9Al9fA3GlULAEDTJHlt1sk9novDuok")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to Disaster Alert Bot! Type /latest to see recent disasters.")

@bot.message_handler(commands=['latest'])
def latest_alerts(message):
    alerts = get_alerts()
    if not alerts:
        alerts = get_disaster_updates()
        response = "\n".join([f"{a[0]} - {a[1]}" for a in alerts])
    bot.reply_to(message, response if response else "No recent alerts.")

def send_telegram_alert(title, summary):
    bot.send_message(os.getenv("1632633256"), f"🚨 {title} \n {summary}")

bot.polling()