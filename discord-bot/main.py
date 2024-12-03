#import required dependicies
import discord
from discord.ext import commands
import requests
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os


#import Api keys
from apikeys import *

intents = discord.Intents.all()
intents.members = True


client = commands.Bot(command_prefix='!', intents=intents)





@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")

#when users uses !hello the bot will repond with the send text
@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the your PromptInsights bot")


@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye my friend")


@client.event
async def on_member_join(member):
    #print("User joined") #just prints in command line here
    #await member.send("Welcome")   #this line send "welcome in Pm to the user"

    channel = client.get_channel(1313505832205553676)
    await channel.send("Welcome")



@client.event
async def on_member_remove(member):
    channel = client.get_channel(1313505832205553676)
    await channel.send("Goodbye")




#slash commands

#guilds it is for testing otherwise need to wait 1hour for discord bot update for the slash commands
@client.slash_command(name = "test", description = "test", guild_ids=[TestServerId])
async def test(interaction: Interaction):
    await interaction.response.send_message("hello, testing slash commands")



#token removed for security reasons, change to promptinsight discord bot token
client.run(Discord_bot_token)