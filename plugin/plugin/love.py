import random
from pyrogram import filters
def load(app):
    @app.on_message(filters.command("love") & filters.reply)
    def love_percentage(_, msg):
        percent = random.randint(1, 100)
        msg.reply_text(f"❤️ Love between {msg.from_user.first_name} and {msg.reply_to_message.from_user.first_name} is {percent}%")
