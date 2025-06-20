from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from plugins import love, ship, actions, coupleofday

app = Client("lovebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Load handlers
love.load(app)
ship.load(app)
actions.load(app)
coupleofday.load(app)

print("Bot started...")
app.run()
