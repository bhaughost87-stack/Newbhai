import threading
from flask import Flask
from pyrogram import Client
from pyrogram.types import ChatJoinRequest

# --- RENDER FIX ---
flask_app = Flask(__name__)
@flask_app.route('/')
def health(): return "Bot is Online 24/7! 🚀"

def run_flask():
    flask_app.run(host='0.0.0.0', port=10000)

# --- TERA DATA ---
API_ID = 34021699
API_HASH = "0230fa05102dc2819b46fa00abbe7fd9"
BOT_TOKEN = "8791954092:AAEZMuHyKgZgPGzUiRCPPz8xH-tztxSrKFs"
APK_ID = "BQACAgUAAxkBAAMMadLxyKAY72qJmFJMUvNfv-MjGHUAAq0aAALjflFWAYYu9ZAGgLweBA"

app = Client("jai_final_v3", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_chat_join_request()
async def send_apk(client, request: ChatJoinRequest):
    print(f"📩 Request Aayi User ID: {request.from_user.id}") # Ye Render logs mein dikhega
    try:
        await client.send_document(
            chat_id=request.from_user.id, 
            document=APK_ID, 
            caption=(
                "🚀 **ONLY FOR PREMIUM USERS** 💥\n\n"
                "✅ **100% LOSS RECOVER GUARANTEE**\n"
                "• Wingo-Number Hack\n"
                "• Trx1Min-Number Hack\n\n"
                "💸 **Click and Install Hack Below** 👇\n"
                "https://t.me/JaiclubNumberHack/5"
            )
        )
        print(f"✅ APK Successfully Sent to: {request.from_user.id}")
    except Exception as e:
        print(f"❌ Error Bhejne Mein: {e}") # Agar caption ya ID mein galti hogi toh yahan dikhega

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    print("🤖 Bot Start Ho Gaya Hai...")
    app.run()
