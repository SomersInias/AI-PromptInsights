import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())



@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("hello, I am the your PromptInsights bot")

#token removed for security reasons, change to promptinsight discord bot token
client.run('token')