# edits by jeol <3

from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "Auto Approved Bot",
    bot_token = environ["BOT_TOKEN"],
    api_id = int(environ["API_ID"]),
    api_hash = environ["API_HASH"]
)

CHAT_ID = None
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")


@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    bot = await client.get_me()
    await message.reply_text(
        text=f"**__Hello {message.from_user.mention} Iam Auto Approver Join Request Bot",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("📢 BOT UPDATES", url="https://t.me/REQUSET_ACCEPT_BOT"),
            InlineKeyboardButton("📢 BOT SUPPORT", url="https://t.me/REQUSET_ACCEPT_BOT")
            ],[            
            InlineKeyboardButton("➕️ ADD ME GROUP", url=f"https://t.me/{bot.username}?startgroup=true"),
            InlineKeyboardButton("➕️ ADD ME CHANNEL", url=f"https://t.me/{bot.username}?startchannel=true") 
            ]]
            )
        )

#    await client.send_message(chat_id=message.chat.id, text=f"**__Hello {message.from_user.mention} Iam Auto Approver Join Request Bot Just [Add Me To Your Group Channnl](http://t.me/{approvedbot.username}?startgroup=botstart)**__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    btn = InlineKeyboardMarkup([[InlineKeyboardButton("📢 BOT UPDATES", url="https://t.me/REQUSET_ACCEPT_BOT")]])
    await client.send_message(
         user.id,
            f"**Hello {message.from_user.mention}!\nYou Request To Join {message.chat.title} Was Approved.🏻",
            reply_markup=btn
        )

print("Bot Started. Editz By @jeol_tg")
pr0fess0r_99.run()
