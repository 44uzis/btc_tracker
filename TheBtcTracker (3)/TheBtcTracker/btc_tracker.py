import os
import sys
import time
import requests
import asyncio
from telegram import Bot
from dotenv import load_dotenv
from datetime import datetime

# ==== LOAD ENV VARIABLES ====
load_dotenv()

BTC_WALLET = os.getenv("BTC_WALLET")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))  # seconds
LOG_FILE = "btc_log.txt"

# ==== CHECK VARIABLES ====
if not BTC_WALLET or not TELEGRAM_TOKEN or not CHAT_ID:
    print("Error: Please set BTC_WALLET, TELEGRAM_TOKEN, and CHAT_ID in the .env file.")
    sys.exit(1)

bot = Bot(token=TELEGRAM_TOKEN)

# ==== FUNCTION TO LOG MESSAGES ====
def log_message(message):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

# ==== FUNCTION TO GET BTC BALANCE ====
def get_btc_balance(address):
    url = f"https://blockchain.info/q/addressbalance/{address}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        satoshis = int(response.text)
        btc = satoshis / 1e8
        return btc
    except Exception as e:
        log_message(f"Error fetching balance: {e}")
        return None

# ==== MAIN LOOP ====
async def main():
    last_balance = None
    while True:
        balance = get_btc_balance(BTC_WALLET)
        if balance is not None:
            if last_balance is None:
                last_balance = balance
                msg = f"🚀 Tracking started\nCurrent balance: {balance:.8f} BTC"
                await bot.send_message(chat_id=CHAT_ID, text=msg)
                log_message(msg)
            elif balance != last_balance:
                diff = balance - last_balance
                sign = "⬆️" if diff > 0 else "⬇️"
                msg = f"{sign} Balance changed by {diff:.8f} BTC\nNew balance: {balance:.8f} BTC"
                await bot.send_message(chat_id=CHAT_ID, text=msg)
                log_message(msg)
                last_balance = balance
        else:
            log_message("Balance fetch failed, retrying in next interval.")
        await asyncio.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped manually.")
        log_message("Bot stopped manually.")
