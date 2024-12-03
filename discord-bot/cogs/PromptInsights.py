import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import aiohttp  # For asynchronous HTTP requests
import io
from apikeys import *


class PromptInsights(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Guilds for testing; otherwise, need to wait for an hour for Discord bot updates for slash commands
    @nextcord.slash_command(
        name="word_frequencies",
        description="Analyze word frequencies by requesting from an API",
        guild_ids=[TestServerId]
    )
    async def wordfreq(
        self,
        interaction: Interaction,
        user_id: int = nextcord.SlashOption(
            description="Enter the user ID", required=True
        ),
        x: int = nextcord.SlashOption(
            description="Enter the x value", required=True
        )
    ):
        await interaction.response.defer()  # Defer response to allow time for processing
        try:
            # Define the API URL with the provided inputs
            api_url = f"{ApiUrl}/word_frequencies?user_id={user_id}&x={x}"

            # Perform the GET request
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url) as response:
                    if response.status == 200:
                        # Get the image data from the API
                        image_data = await response.read()

                        # Create a nextcord.File object for sending the image
                        file = nextcord.File(
                            io.BytesIO(image_data), filename="word_frequencies.png"
                        )
                        # Send the image in the interaction response
                        await interaction.followup.send("Here is the word frequency analysis:", file=file)
                    else:
                        # Handle non-200 responses
                        await interaction.followup.send(f"API request failed with status code {response.status}")

        except Exception as e:
            # Handle exceptions gracefully
            await interaction.followup.send(f"An error occurred: {e}")


    # Guilds for testing; otherwise, need to wait for an hour for Discord bot updates for slash commands
    @nextcord.slash_command(
        name="word_cloud",
        description="Analyze your prompts and get insight through a word cloud",
        guild_ids=[TestServerId]
    )
    async def wordcloud(
        self,
        interaction: Interaction,
        user_id: int = nextcord.SlashOption(
            description="Enter the user ID", required=True
        ),
        x: int = nextcord.SlashOption(
            description="Enter the x value", required=True
        )
    ):
        await interaction.response.defer()  # Defer response to allow time for processing
        try:
            # Define the API URL with the provided inputs
            api_url = f"{ApiUrl}/word_cloud?user_id={user_id}&x={x}"

            # Perform the GET request
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url) as response:
                    if response.status == 200:
                        # Get the image data from the API
                        image_data = await response.read()

                        # Create a nextcord.File object for sending the image
                        file = nextcord.File(
                            io.BytesIO(image_data), filename="word_cloud.png"
                        )
                        # Send the image in the interaction response
                        await interaction.followup.send("Here is the analysis represented as a word cloud:", file=file)
                    else:
                        # Handle non-200 responses
                        await interaction.followup.send(f"API request failed with status code {response.status}")

        except Exception as e:
            # Handle exceptions gracefully
            await interaction.followup.send(f"An error occurred: {e}")


# Code for main.py to recognize the cog
def setup(client):
    client.add_cog(PromptInsights(client))
