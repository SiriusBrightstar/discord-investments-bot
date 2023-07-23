import logging
from datetime import datetime

from discord import Embed
from discord import Client
from discord import Status
from discord import Intents
from discord import app_commands
from discord import Activity, ActivityType

from dotenv import dotenv_values
from customLogger import CustomFormatter

envData = dotenv_values('.env')

log = logging.getLogger("my_app")
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(CustomFormatter())
log.addHandler(ch)


intents = Intents.default()
intents.members = True
client = Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="about", description="About this Bot")
async def aboutBot(interaction):
    log.info(f"About requested by {interaction.user.name}")
    # await interaction.response.send_message(f"The id of the user that invoked this command is {interaction.user.id}")
    embedTitle = 'Portfolio Bot'
    embedDescription = (f'Open Source Portfolio Tracker & Paper Trading Bot'
                        '\n'
                        f'Thanks for using it {interaction.user.name}❤️'
    )
    embedUrl = 'https://github.com/SiriusBrightstar/discord-investments-bot'
    aboutEmbed = Embed(
        title=embedTitle,
        url=embedUrl,
        description=embedDescription,
        color=0x000000
    )
    await interaction.response.send_message(embed=aboutEmbed)


@client.event
async def on_ready():
    await tree.sync()
    await client.change_presence(activity=Activity(type=ActivityType.watching,
                                                   name="Your Trades"),
                                 status=Status.online)
    log.info(f'Bot has logged in as {client.user}')

client.run(envData['DISCORD_TOKEN'])
