# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int("27526328")
	API_HASH=("db231e73712db0b6397f624a75a760f8")
	BOT_TOKEN=("6791224524:AAHdWd5lTOBZzZqVI3duDRPfejIzdkgtr4E")
	BOT_USERNAME=("Cholefilestorebot")
	DB_CHANNEL = int("-1002193259174")
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
	SHORTLINK_API = os.environ.get('SHORTLINK_API')
	BOT_OWNER = int("7102263732")
	DATABASE_URL=("mongodb+srv://accha:phir@cluster0.dfhnrr7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL=("-1002026961037")
	LOG_CHANNEL=("-1002149638793")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/Cholefilestorebot)
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [Akhand](https://t.me/ariesaep) 
│
├🔹 **Anime:** [Crunchylite](https://t.me/crunchyliteanime)
│
├🔸 **Hentai:** [Haniflix](https://t.me/ongoing_haniflix)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [Akhand](https://t.me/ariesaep)
 
 nah i'hd win

[Donate Me](https://t.me/ariesaep)
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴏғ @ariesaep
ᴛᴏ ᴜsᴇ ᴍᴇ ʏᴏᴜ ᴊᴜsᴛ ʜᴀᴠᴇ ᴛᴏ sɪᴍᴘʟɪғʏ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ғɪʟᴇ & ɪ'ʟʟ ᴄᴏɴᴠᴇʀᴛ ɪᴛ ɪɴᴛᴏ ʟɪɴᴋ

"""
	
