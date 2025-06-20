from pyrogram import filters
def load(app):
    @app.on_message(filters.command("slap") & filters.reply)
    def slap(_, msg):
        msg.reply_animation("https://media.tenor.com/IauL6U7gkeMAAAAC/slap.gif", caption=f"{msg.from_user.first_name} slapped {msg.reply_to_message.from_user.first_name} 😂")

    @app.on_message(filters.command("punch") & filters.reply)
    def punch(_, msg):
        msg.reply_animation("https://media.tenor.com/OLxW4Nrr6e4AAAAC/punch-anime.gif", caption=f"{msg.from_user.first_name} punched {msg.reply_to_message.from_user.first_name} 💥")
      
