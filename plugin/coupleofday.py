import random
from pyrogram import filters
from pyrogram.types import Message
def load(app):
    couples = []
    @app.on_message(filters.command("coupleofday"))
    def couple_of_day(_, msg: Message):
        chat = msg.chat
        users = []
        async for member in app.get_chat_members(chat.id):
            if not member.user.is_bot:
                users.append(member.user)
        if len(users) < 2:
            return msg.reply("Not enough users.")
        lover1, lover2 = random.sample(users, 2)
        msg.reply_text(f"❤️ Couple of the day: {lover1.first_name} + {lover2.first_name} ❤️")
      
