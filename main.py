import threading
from flask import Flask
from pyrogram import Client, filters

# --- RENDER FIX ---
flask_app = Flask(__name__)
@flask_app.route('/')
def health(): return "Bot is Online & Ready for ID Extraction! 🚀"

def run_flask():
    flask_app.run(host='0.0.0.0', port=10000)

# --- TERA DATA (Token ek baar phir se check kar lena bhai) ---
API_ID = 34021699
API_HASH = "0230fa05102dc2819b46fa00abbe7fd9"
BOT_TOKEN = "8664894205:AAGvnqPloabIfIe0sV_wZG7H1roghJq5ONg"

app = Client("debug_bot_new", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document)
async def get_id(client, message):
    file_id = message.document.file_id
    print(f"\n\n🚀 ID MIL GAYI: {file_id}\n\n")
    await message.reply_text(f"✅ Teri APK ID mil gayi!\n\nID: `{file_id}`\n\nAb isse final code mein dalo.")

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    print("🤖 Bot start ho raha hai... Logs check karte raho.")
    app.run()
