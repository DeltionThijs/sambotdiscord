import discord
from discord.ext import commands, tasks
import asyncio
import os
import random
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# List of random messages
random_messages = [
    "Hey, ik ben kkr broke. Mag ik geld?",
    "Heb je 20 euro voor me Thijs?",
    "Fabio heb je 20 euro voor mij? Ik ben een kanker skeere zwerver",
    "Heb je 20€ voor me? Ik ben kkr broke en heb geld nodig",
    "Ik heb geen geld nu"
]

@bot.event
async def on_ready():
    print(f'We hebben ingelogd als {bot.user}')
    send_message.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "lenen" in message.content.lower():
        await message.channel.send(random.choice(random_messages))

    if "Thijs" in message.content:
        await message.channel.send(random.choice(random_messages))

    if "fabio" in message.content.lower():
        await message.channel.send(random.choice(random_messages))
        
    if "faa" in message.content.lower():
        await message.channel.send(random.choice(random_messages))

    await bot.process_commands(message)

@tasks.loop(hours=4)
async def send_message():
    for guild in bot.guilds:
        main_channel = guild.system_channel
        if main_channel is not None:
            await main_channel.send(random.choice(random_messages))
            break
    await asyncio.sleep(1)

@bot.command()
async def hello(ctx):
    await ctx.send('Hallo, ik ben een sam de kanker mongool')

bot.run(os.getenv('DISCORD_TOKEN'))

