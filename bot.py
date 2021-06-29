import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=">")
rules = ["your mom","your dad","gunners mom"]

dad_jokes = []


f = open("one-liners.txt","r")
one_liners = f.readlines()


#when the bot is done initiating, it will tell you when ready
@client.event
async def on_ready():
    print("Bot is ready")

#if you type the command >hello, the bot will respond with hi
@client.command()
async def hello(ctx):
    await ctx.send("Hi")

#this function takes the rules variable and you can use the >rules [1,2,3] command to call them
@client.command(aliases=['rules','test'])
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])

#this function will take the one-liners variable and generate a joke when called by the command
@client.command()
async def one_liner(ctx):
	await ctx.send(random.choice(one_liners))

#this is the token from the discord dev dashboard for the bot
client.run("get updated token from discord app right noww")