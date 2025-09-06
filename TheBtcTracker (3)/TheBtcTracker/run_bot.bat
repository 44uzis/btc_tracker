@echo off
REM Navigate to the folder of this script
cd /d %~dp0

REM Install dependencies (only if not already installed)
pip install -r requirements.txt

REM Run the bot
python btc_tracker.py

pause
