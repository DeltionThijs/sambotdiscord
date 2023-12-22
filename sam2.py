import discord
from discord.ext import commands, tasks
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()  # Laad omgevingsvariabelen uit het .env-bestand

intents = discord.Intents.default()
intents.message_content = True  # Schakel het berichtinhoudsprivilege in
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
        main_channel = guild.system_channel  # Krijg het hoofdkanaal van de server
        if main_channel is not None:  # Controleer of het hoofdkanaal bestaat
            await main_channel.send("Heb je 20€ voor me? Ik ben kkr broke en heb geld nodig")
            break  # Stop met itereren door de servers nadat het bericht is verzonden in het hoofdkanaal
    await asyncio.sleep(1)  # Wacht 1 seconde tussen elk bericht

@bot.command()
async def hello(ctx):
    await ctx.send('Hallo, ik ben een sam de kanker mongool')

bot.run(os.getenv('DISCORD_TOKEN'))

