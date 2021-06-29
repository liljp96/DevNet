import discord
import random
from discord.ext import commands
import sched
import time

client = commands.Bot(command_prefix=">")
rules = ["your mom","your dad","gunners mom"]

d = open("dad-jokes.txt","r")
dad_jokes = d.readlines()

f = open("one-liners.txt","r")
one_liners = f.readlines()

a = open("facts.txt", "r")
facts = a.readlines()

s = sched.scheduler(time.time, time.sleep)

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

#this function will take the dad-jokes variable and generate a dad joke when called by >dad_joke
@client.command()
async def dad_joke(ctx):
	await ctx.send(random.choice(dad_jokes))

#this function makes the bot periodically post random facts to the discord chat
@client.command()
channel = client.get_channel()
async def facts(ctx):
	await ctx.send(s.enter())

#this function will clear messages given the amount of messages to delete when using the command >clear (#)
@client.command(alises=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit = amount)








#this is the token from the discord dev dashboard for the bot
client.run("NzYzNjI4NDE4MzkzODMzNDcy.X36eYg.FfDWpZK2t6I3XtVfvhj1s3cRh_4")
