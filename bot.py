# edits by jeol <3

from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest
from database import add_user, add_group, all_users, all_groups, users, remove_user

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
    add_user(user.id)
except errors.PeerIdInvalid as e:
    print("user isn't start bot(means group)")
except Exception as err:
    print(str(err))   

@pr0fess0r_99.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")



print("Bot Started. Editz By @jeol_tg")
pr0fess0r_99.run()
