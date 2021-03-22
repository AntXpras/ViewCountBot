# (c) 2021-22 < @xditya >
# < @BotzHub >

import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# start the bot
print("Memulai.....")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    FRWD_CHANNEL = config("FRWD_CHANNEL", cast=int)
    BotzHub = TelegramClient('BotzHub', apiid, apihash).start(bot_token=bottoken)
except:
    print("Environment vars gagal..! Chek ulang...")
    print("Bot telah keluar....")
    exit()

@BotzHub.on(events.NewMessage(pattern="/start", func=lambda e: e.is_private))
async def _(event):
    ok = await BotzHub(GetFullUserRequest(event.sender_id))
    await event.reply(f"Hallo cuy... {ok.user.first_name}! \nAku adalah view-counter bot.\nKirimkan aku sebuah pesan dan aku akan menampilkan jumlah penonton tersebut..!",
                    buttons=[
                        [Button.url("Forks.", url="https://t.me/Xpras_id"),
                        Button.url("Repository", url="https://www.xnxx.com")]
                    ])

@BotzHub.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def countit(event):
    if event.text.startswith('/'):
        return
    x = await event.forward_to(FRWD_CHANNEL)
    await x.forward_to(event.chat_id)

print("Sedang memulai bot...")
print("Do visit @cyntaxrobot..")
BotzHub.run_until_disconnected()
