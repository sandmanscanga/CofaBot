"""Module to be used for TSB Security Bots"""
import datetime

import discord
from discord import Intents
from discord.ext import commands

from config import token

client = commands.Bot(command_prefix=">", intents=Intents.all())


@client.event
async def on_connect():
    """Displays status that bot has connected to Discord"""

    print("[*] Bot has connected to Discord")


@client.event
async def on_ready():
    """Displays status that bot is ready to use"""

    print("[+] Bot is ready")


@client.event
async def on_resume():
    """Displays status that bot has resumed"""

    print("[+] Bot resumed")


@client.event
async def on_disconnect():
    """Displays status that bot has disconnected from Discord"""

    print("[!] Bot has disconnected from Discord")


@client.command(aliases=["t", "testy"])
async def test(ctx):
    """Command to test bot functionality"""

    await ctx.send(f"{client.user.name} is online and ready to be used!")


@client.command()
async def embed(ctx, *, info=None):
    """Command to create an embed message"""

    embed = discord.Embed(
        title="Embed",
        description=info,
        color=ctx.author.color
    )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_footer(icon_url=client.user.avatar_url, text=client.user.name)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


if __name__ == "__main__":
    cogs = {"cogs.nuke"}
    for cog in cogs:
        client.load_extension(cog)
        print(f"[*] {cog} has been loaded successfully")

    client.run(token)
