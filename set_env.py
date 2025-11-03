#!/usr/bin/env python3
"""
Script to set environment variables for the Telegram bot.
Run this before starting the bot to set all required environment variables.
"""

import os

# Set environment variables
os.environ['BOT_NAME'] = 'CR CHOUDHARY'
os.environ['BOT_TOKEN'] = '7626013382:AAEvmqpHw4otevswmJbtSw7yK03rGYVmc4M'
os.environ['API_ID'] = '22746239'
os.environ['API_HASH'] = 'a98ec8cfd8572a3a7c936cf828fe6215'
os.environ['MONGO_URI'] = 'mongodb+srv://herukobanna:ankit999@cluster0.xs772me.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
os.environ['OWNER_ID'] = '7693352537'
os.environ['LOG_CHANNEL_ID'] = '-1003228079117'

print("✅ Environment variables set successfully!")
print("🚀 You can now run your bot with: python modules/main.py")
print("\n📋 Configuration Summary:")
print(f"Bot Name: {os.environ['BOT_NAME']}")
print(f"API ID: {os.environ['API_ID']}")
print(f"Owner ID: {os.environ['OWNER_ID']}")
print(f"Log Channel ID: {os.environ['LOG_CHANNEL_ID']}")
print("\n⚠️  Bot Token and API Hash are set but hidden for security.")
