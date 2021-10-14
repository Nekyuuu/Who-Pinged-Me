#coding:utf-8



# ------------------------------------------------------------------ CONFIG ------------------------------------------------------------------

token = ""
webhook_url = ""

# --------------------------------------------------------------------------------------------------------------------------------------------




import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix = "+")

@bot.event
async def on_ready():
	print(f'''
░██╗░░░░░░░██╗██╗░░██╗░█████╗░  ██████╗░██╗███╗░░██╗░██████╗░███████╗██████╗░  ███╗░░░███╗███████╗  ░█████╗░
░██║░░██╗░░██║██║░░██║██╔══██╗  ██╔══██╗██║████╗░██║██╔════╝░██╔════╝██╔══██╗  ████╗░████║██╔════╝  ██╔══██╗
░╚██╗████╗██╔╝███████║██║░░██║  ██████╔╝██║██╔██╗██║██║░░██╗░█████╗░░██║░░██║  ██╔████╔██║█████╗░░  ╚═╝███╔╝
░░████╔═████║░██╔══██║██║░░██║  ██╔═══╝░██║██║╚████║██║░░╚██╗██╔══╝░░██║░░██║  ██║╚██╔╝██║██╔══╝░░  ░░░╚══╝░
░░╚██╔╝░╚██╔╝░██║░░██║╚█████╔╝  ██║░░░░░██║██║░╚███║╚██████╔╝███████╗██████╔╝  ██║░╚═╝░██║███████╗  ░░░██╗░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░╚════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═════╝░  ╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░
\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
   User : {bot.user.name}
   ID : {bot.user.id}
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
''')


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        data = {
                "username" : "Who pinged me ?",
                "avatar_url": "https://emoji.gg/assets/emoji/5239_ping.png"
            }
        data["embeds"] = [
            {
                "description" : f"```Server : {message.guild.name}\nChannel : {message.channel}\n\n{message.author.name} : {message.content}```",
                "title" : ""
            }
        ]
        result = requests.post("https://discord.com/api/webhooks/891491854288314389/FyGZQWWi42sJOOlfcGZU52t6VkA-PAGwHnaAuAUMH2ZGiSGmAsxTr3jodVyjMCUuKR-Y", json = data)
        print(f"\nServer : {message.guild.name}\nChannel : {message.channel}\n\n{message.author.name} : {message.content}\n\n")


bot.run(token, bot = False)


