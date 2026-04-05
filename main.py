import os
import threading
from flask import Flask
from pyrogram import Client
from pyrogram.types import ChatJoinRequest

# --- RENDER PORT FIX (24/7 ke liye) ---
flask_app = Flask(__name__)
@flask_app.route('/')
def health_check():
    return "Bot is Active & Fast! 🚀"

def run_flask():
    # Render ko 10000 port chahiye hota hai deploy success ke liye
    flask_app.run(host='0.0.0.0', port=10000)

# --- TERA NAYA BOT DATA ---
API_ID = 34021699
API_HASH = "0230fa05102dc2819b46fa00abbe7fd9"
BOT_TOKEN = "8791954092:AAEZMuHyKgZgPGzUiRCPPz8xH-tztxSrKFs"
APK_ID = "BQACAgUAAxkDAAMXadlkXxrwjBfVTOk3G-NRrtKt9YoAAq0aAALjflFWa0EWTZiLPYgeBA"

# TERA NAYA CAPTION
CAPTION_TEXT = """🚀 **🎉 ( ONLY FOR PREMIUM USERS  ) 💥( 100% LOSS RECOVER GUARANTEE ) 😵**
Hack future add ☠️
Wingo-Number Hack
Trx1Min-Number Hack

     💸Click and install💸

How To Use and download Hack 👇
https://t.me/JaiclubNumberHack/5
https://t.me/JaiclubNumberHack/5. 🔥"""

app = Client("jai_fresh_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- SIRF APK BHEJEGA (REQUEST PENDING RAHEGI) ---
@app.on_chat_join_request()
async def send_apk(client, request: ChatJoinRequest):
    try:
        # Note: Yahan 'approve' wali line nahi hai, isliye request pending rahega
        await client.send_document(
            chat_id=request.from_user.id, 
            document=APK_ID, 
            caption=CAPTION_TEXT
        )
        print(f"✅ APK Sent to: {request.from_user.id}")
    except Exception as e:
        print(f"❌ Error sending APK: {e}")

if __name__ == "__main__":
    # Flask ko background thread mein start karo
    threading.Thread(target=run_flask).start()
    print("🤖 Fresh Bot Starting...")
    app.run()
  
