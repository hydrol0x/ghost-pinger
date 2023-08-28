import discord
from dotenv import load_dotenv
import os
import random
load_dotenv()  
TOKEN = os.getenv("BOT_TOKEN")


import discord

bot = discord.Bot()
bot.ghost_ping_user = ""
bot.pingchannel = None
bot.time_delay = 0.5 

responses = ["PING", "I hate you", "Loser", "L", "Who asked?", "When did I ask?", "OK", "LOL", "ping"]

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message):
        if message.author == bot.user:
            return

        if str(message.author.id) == str(bot.ghost_ping_user):
            mention_string = message.author.mention
            response= responses[random.randint(0, len(responses)-1)]
            if bot.pingchannel:
                channel = bot.get_channel(bot.pingchannel)
                await channel.send(response + " "+  mention_string, delete_after=bot.time_delay)
                return
            await message.channel.send(response + " "+  mention_string, delete_after=bot.time_delay)

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

    time_delay = max(time_delay, 0)
    bot.time_delay = min(time_delay, 10) 
    await ctx.respond(f"Set time delay for ghost ping deletion to {bot.time_delay}!")

@bot.slash_command()
async def setpingchannel(ctx, pingchannel_id):
    await ctx.respond(f"Set channel where ping will happen to {pingchannel_id}!")
    
    bot.pingchannel = pingchannel_id 


bot.run(TOKEN)