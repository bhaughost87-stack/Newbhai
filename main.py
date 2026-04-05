import threading
from flask import Flask
from pyrogram import Client
from pyrogram.types import ChatJoinRequest

# --- RENDER 24/7 FIX ---
flask_app = Flask(__name__)
@flask_app.route('/')
def health(): return "Bot is Running 24/7! 🚀"

def run_flask():
    # Render ko 10000 port chahiye hota hai deploy success ke liye
    flask_app.run(host='0.0.0.0', port=10000)

# --- TERA FINAL DATA ---
API_ID = 34021699
API_HASH = "0230fa05102dc2819b46fa00abbe7fd9"
BOT_TOKEN = "8791954092:AAEZMuHyKgZgPGzUiRCPPz8xH-tztxSrKFs"
APK_ID = "BQACAgUAAxkBAAMMadLxyKAY72qJmFJMUvNfv-MjGHUAAq0aAALjflFWAYYu9ZAGgLweBA"

app = Client("jai_final_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- JOIN REQUEST PAR APK BHEJNA ---
@app.on_chat_join_request()
async def send_apk(client, request: ChatJoinRequest):
    try:
        # Request pending rahegi aur user ko APK chala jayega
        await client.send_document(
            chat_id=request.from_user.id, 
            document=APK_ID, 
            caption="""🚀 **🎉 ( ONLY FOR PREMIUM USERS  ) 💥( 100% LOSS RECOVER GUARANTEE ) 😵**
Hack future add ☠️
Wingo-Number Hack
Trx1Min-Number Hack

     💸Click and install💸

How To Use and download Hack 👇
https://t.me/JaiclubNumberHack/5
https://t.me/JaiclubNumberHack/5. 🔥"""
        )
        print(f"✅ APK Bhej diya user ko: {request.from_user.id}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Flask thread start karo taaki Render bot ko band na kare
    threading.Thread(target=run_flask).start()
    print("🤖 Bot is LIVE! Ab maza lo.")
    app.run()
