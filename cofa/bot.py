"""Module to be used for TSB Security Bots"""

import argparse
from typing import Any

from discord import Intents
import discord.ext.commands

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


def main(cmdline: argparse.Namespace) -> None:
    """Main function to run the bot"""

    cogs = {"cogs.nuke"}
    for cog in cogs:
        _result = client.load_extension(cog)  # pylint: disable=invalid-name
        print(f"[*] {cog} has been loaded successfully, result: {_result!r}")

    client.run(cmdline.token)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "token", help="Discord bot token to be used for authentication"
    )
    main(cmdline=parser.parse_args())
