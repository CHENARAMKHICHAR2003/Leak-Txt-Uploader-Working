# config.py
import os

# Bot Configuration
BOT_NAME = os.environ.get('BOT_NAME', 'CR CHOUDHARY BOT')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
API_ID = int(os.environ.get('API_ID', '22746239'))
API_HASH = os.environ.get('API_HASH', 'a98ec8cfd8572a3a7c936cf828fe6215')
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://herukobanna:ankit999@cluster0.xs772me.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

# Additional Configuration
OWNER_ID = int(os.environ.get('OWNER_ID', '7693352537'))
LOG_CHANNEL_ID = int(os.environ.get('LOG_CHANNEL_ID', '-1003228079117'))

