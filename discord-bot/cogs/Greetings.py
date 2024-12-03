import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from apikeys import *




class Greetings(commands.Cog):
    def __init__(self,client):
        self.client = client

        
    #guilds it is for testing otherwise need to wait 1hour for discord bot update for the slash commands
    @nextcord.slash_command(name = "testcog", description = "testing using commands from cogs", guild_ids=[TestServerId])
    async def testcog(self, interaction: Interaction):
        await interaction.response.send_message("hello, testing slash commands")

    
    #testing listeners in cogs
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user:
            return
        
        if ("test") in message.content:
            await message.channel.send("testing listener works from cog")





#code for that main.py can reconize the code and allow the bot to use it
def setup(client):
    client.add_cog(Greetings(client))
