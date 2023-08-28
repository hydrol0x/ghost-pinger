import discord
from dotenv import load_dotenv
import os
import random
load_dotenv()  
TOKEN = os.getenv("BOT_TOKEN")

import discord
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

bot.ghost_ping_user = ""
bot.pingchannel = None
bot.keyword = None
bot.time_delay = 0.5 

responses = ["PING", "I hate you", "Loser", "L", "Who asked?", "When did I ask?", "OK", "LOL", "ping"]

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

async def no_keyword(message):
        if str(message.author.id) == str(bot.ghost_ping_user):
            mention_string = message.author.mention
            response= responses[random.randint(0, len(responses)-1)]
            channel = bot.get_channel(bot.pingchannel)
            if channel:
                await channel.send(response + " "+  mention_string, delete_after=bot.time_delay)
                return
            await message.channel.send(response + " "+  mention_string, delete_after=bot.time_delay)

async def keyword_response(message):
    if str(bot.keyword) in str(message.content):
        user = await bot.get_or_fetch_user(int(bot.ghost_ping_user))
        print(bot.ghost_ping_user)
        print(user)
        mention_string = user.mention
        response= responses[random.randint(0, len(responses)-1)]
        await message.channel.send(response + " "+  mention_string, delete_after=bot.time_delay)

            
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if not bot.keyword:
        await no_keyword(message)
        return
    await keyword_response(message)


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
async def setpingchannel(ctx, pingchannel_id:str):
    await ctx.respond(f"Set channel where ping will happen to {pingchannel_id}!")
    
    bot.pingchannel = int(pingchannel_id )


@bot.slash_command()
async def setkeyword(ctx, keyword:str):
    await ctx.respond(f"Set ping keyword to {keyword}!")
    
    bot.keyword =keyword 


bot.run(TOKEN)