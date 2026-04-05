import threading
from flask import Flask
from pyrogram import Client, filters

# --- RENDER FIX (Iske bina Status 1 aata hai) ---
flask_app = Flask(__name__)
@flask_app.route('/')
def health(): return "ID extraction mode is LIVE! 🚀"

def run_flask():
    flask_app.run(host='0.0.0.0', port=10000)

# --- TERA DATA ---
API_ID = 34021699
API_HASH = "0230fa05102dc2819b46fa00abbe7fd9"
BOT_TOKEN = "8791954092:AAEZMuHyKgZgPGzUiRCPPz8xH-tztxSrKFs"

app = Client("debug_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document)
async def get_id(client, message):
    # Ye line Render ke logs mein ID print karegi
    print(f"\n\n🚀 TERI NAYI APK ID YE HAI: {message.document.file_id}\n\n")
    await message.reply_text(f"✅ ID mil gayi! Render ke Logs check kar bhai.")

if __name__ == "__main__":
    # Flask thread start karo
    threading.Thread(target=run_flask).start()
    print("🤖 Debug Bot Live Hai! Ab APK bhejo...")
    app.run()
