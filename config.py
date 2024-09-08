import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23940130"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4d717a6f888e37b7ebde0ace80cd22c6")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://pooranji721:oEaCQoycs1bXfbPd@firemon.gjtpd.mongodb.net/?retryWrites=true&w=majority&appName=Firemon")
