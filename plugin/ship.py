import random
from pyrogram import filters
def load(app):
    @app.on_message(filters.command("ship"))
    def ship_users(_, msg):
        if len(msg.command) >= 3:
            name1, name2 = msg.command[1], msg.command[2]
            msg.reply_text(f"🚢 Shipping {name1} ❤️ {name2}... {random.randint(50, 100)}% Match!")
