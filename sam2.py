import discord
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # Enable privileged message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We hebben ingelogd als {bot.user}')
    send_message.start()  # Start het taakplanning proces

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "lenen" in message.content.lower():
        await message.channel.send("Hey, ik ben kkr broke. Mag ik geld?")

    if "Thijs" in message.content:
        await message.channel.send("Heb je 20 euro voor me Thijs?")
   
    if "fabio" in message.content.lower():
        await message.channel.send("Fabio heb je 20 euro voor mij? Ik ben een kanker skeere zwerver")

    await bot.process_commands(message)

@tasks.loop(hours=4)  # Taakplanning elke 4 uur
async def send_message():
    for guild in bot.guilds:
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                await channel.send("Heb je 20€ voor me? Ik ben kkr broke en heb geld nodig")
                await asyncio.sleep(1)  # Wacht 1 seconde tussen elk bericht

@bot.command()
async def hello(ctx):
    await ctx.send('Hallo, ik ben een sam de kanker mongool')

bot.run('MTE4NzUxNjM5NjE2NzQ5NTcyMQ.GNmfNE.gA9tdL5OxGfNbGX_oY1Ye4HXUAeSh7CMMFkPE4')
