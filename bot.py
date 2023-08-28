import discord
from dotenv import load_dotenv
import os
load_dotenv()  
TOKEN = os.getenv("BOT_TOKEN")


import discord

bot = discord.Bot()
bot.ghost_ping_user = ""
bot.time_delay = 0.5 

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message):
        if message.author == bot.user:
            return

        if str(message.author.id) == str(bot.ghost_ping_user):
            mention_string = message.author.mention
            await message.channel.send('Hello! ' + mention_string, delete_after=bot.time_delay)

@bot.slash_command()
async def setuser(ctx, ghost_ping_user_id):
    await ctx.respond(f"Set user to be ghost pinged to {ghost_ping_user_id}!")
    
    bot.ghost_ping_user = ghost_ping_user_id 

@bot.slash_command()
async def setdelay(ctx, time_delay: float):
    try: 
        float(time_delay)
    except:
        await ctx.respond(f"Please enter a valid decimal number")
        return

    await ctx.respond(f"Set time delay for ghost ping deletion to {time_delay}!")
    bot.time_delay = time_delay 


bot.run(TOKEN)