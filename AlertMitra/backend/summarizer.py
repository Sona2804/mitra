import os
import openai
def get_disaster_updates():
    pass

def create_alert(title, summary):
    pass

def get_alerts():
    pass
    
def summarize_text(text):
    openai.api_key = os.getenv("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")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Summarize the following disaster news:"},
                  {"role": "user", "content": text}]
    )
    return response["choices"][0]["message"]["content"].strip()