from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

@app.route('/', methods=['POST'])
def send_to_telegram():
    data = request.json
    title = data.get('title', '📢 خبر جدید از کالاف!')
    link = data.get('link', '')
    
    message = f"📢 {title}\n🔗 {link}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHANNEL_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    
    requests.post(url, data=payload)
    return 'ok'

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == '__main__':
    app.run()
