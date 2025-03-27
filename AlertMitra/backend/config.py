import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("7904429925:AAHeB9Al9fA3GlULAEDTJHlt1sk9novDuok")
TELEGRAM_CHAT_ID = os.getenv("1632633256")
OPENAI_API_KEY = os.getenv("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")

# Web scraping configuration
DISASTER_FEED_URL = "https://example.com/disaster-feed"

# AWS Lambda Configurations
AWS_REGION = "us-east-1"
LAMBDA_FUNCTION_NAME = "DisasterAlertLambda"

