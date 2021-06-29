import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt

client = commands.Bot(command_prefix=">")

#when the bot is done initiating, it will tell you when ready
@client.event
async def on_ready():
    print("Bot is ready")

