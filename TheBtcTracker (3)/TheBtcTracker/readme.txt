# BTC Tracker Bot – Instructions

Thank you for purchasing the BTC Tracker Bot! This bot monitors a Bitcoin wallet and sends real-time balance updates to your Telegram. Follow these steps to get started.

1. Folder Structure:
   Make sure all files are in the same folder:
   BTCBot/
   ├─ btc_tracker.py
   ├─ requirements.txt
   ├─ run_bot.bat
   └─ .env

2. Configure the .env File:
   Open `.env` in a text editor and fill in your details:
   BTC_WALLET=YOUR_BTC_WALLET
   TELEGRAM_TOKEN=YOUR_BOT_TOKEN
   CHAT_ID=YOUR_CHAT_ID
   CHECK_INTERVAL=60

3. Install Dependencies:
   Double-click `run_bot.bat`
   - It will automatically install required Python packages.

4. Run the Bot:
   Double-click `run_bot.bat`
   - CMD window opens
   - Bot starts tracking your wallet
   - Logs saved in btc_log.txt

5. Notes:
   - Keep CMD window open while the bot runs
   - Change CHECK_INTERVAL in .env if desired
   - Close CMD to stop the bot

6. Troubleshooting:
   - Bot doesn’t send messages? Check Telegram token & chat ID
   - Balance not updating? Check BTC wallet address
   - Python errors? Make sure Python 3.9+ is installed and files are in the same folder
