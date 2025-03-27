from backend.app import app
from .database import get_db, create_alert, get_alerts
from .scraper import get_disaster_updates
from .summarizer import summarize_text

__all__ = [
    "app",
    "get_db",
    "create_alert",
    "get_alerts",
    "get_disaster_updates",
    "summarize_text"
]