"""
Portfolio Bot

File            : main.py
Created Date    : 23 July 2023
Version         : v0.0.1
"""

import logging

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
async def about_bot(interaction):
    """
    Sends an embed of this Bot's details
    """
    log.info("About requested by %s", interaction.user.name)
    # f"The id of the user that invoked this command is {interaction.user.id}"
    embed_title = 'Portfolio Bot'
    embed_escription = (f'Open Source Portfolio Tracker & Paper Trading Bot'
                        '\n'
                        f'Thanks for using it {interaction.user.name}❤️'
                        )
    embed_url = 'https://github.com/SiriusBrightstar/discord-investments-bot'
    about_embed = Embed(
        title=embed_title,
        url=embed_url,
        description=embed_escription,
        color=0x000000
    )
    await interaction.response.send_message(embed=about_embed)


@client.event
async def on_ready():
    """
    Runs when Ready
    """
    await tree.sync()
    await client.change_presence(activity=Activity(type=ActivityType.watching,
                                                   name="Your Trades"),
                                 status=Status.online)
    log.info("Bot has logged in as %s", client.user)

client.run(envData['DISCORD_TOKEN'])
