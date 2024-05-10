"""Module for the Dev cog"""

from typing import Any

import discord.ext.commands


class Dev(discord.ext.commands.Cog):
    """Class defining the Dev cog"""

    def __init__(self, bot: Any) -> None:
        self.bot = bot

    @discord.ext.commands.command(aliases=["r", "reload"])
    @discord.ext.commands.is_owner()
    async def restart(self, ctx: Any, cog: Any) -> None:
        """Command to restart a cog"""

        message = await ctx.send(f"Restarting {cog}...")
        self.bot.unload_extension(f"cogs.{cog}")
        self.bot.load_extension(f"cogs.{cog}")
        await message.edit(content=f"Restarted `{cog}`")

    @discord.ext.commands.command()
    @discord.ext.commands.is_owner()
    async def load(self, ctx: Any, cog: Any) -> None:
        """Command to load a cog"""

        self.bot.load_extension(f"cogs.{cog}")
        await ctx.send(f"Loaded {cog}")

    @discord.ext.commands.command()
    @discord.ext.commands.is_owner()
    async def unload(self, ctx: Any, cog: Any) -> None:
        """Command to unload a cog"""

        self.bot.unload_extension(f"cogs.{cog}")
        await ctx.send(f"Unloaded {cog}")


def setup(bot: Any) -> None:
    """Adds the cog to the bot"""

    bot.add_cog(Dev(bot))
