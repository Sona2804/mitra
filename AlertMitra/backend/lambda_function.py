import json
import boto3
import requests
from bot.notifier import send_telegram_alert
from backend.summarizer import summarize_text
from backend.scraper import get_disaster_updates

def lambda_handler(event, context):
    # Fetch latest disaster updates
    updates = get_disaster_updates()
    
    if not updates:
        return {"status": "No recent alerts"}
    
    for alert in updates:
        title, details = alert["title"], alert["details"]
        
        # Summarize disaster details
        summary = summarize_text(details)
        
        # Send alert to Telegram
        send_telegram_alert(title, summary)
    
    return {
        "status": "Alerts sent successfully",
        "alerts_count": len(updates)
    }
