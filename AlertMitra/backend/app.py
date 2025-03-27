##### app.py (FastAPI Backend)
from fastapi import FastAPI, BackgroundTasks
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bot.notifier import send_telegram_alert
from scraper import get_disaster_updates
from summarizer import summarize_text
from database import create_alert, get_alerts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Disaster Alert System API is Running"}

@app.get("/latest")
def latest_alerts():
    return get_alerts()

@app.post("/alert")
def alert_disaster(background_tasks: BackgroundTasks):
    disaster_data = get_disaster_updates()
    summary = summarize_text(disaster_data["details"])
    create_alert(disaster_data["title"], summary)
    background_tasks.add_task(send_telegram_alert, disaster_data["title"], summary)
    return {"message": "Alert Sent"}
