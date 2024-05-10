"""Module for the Mod cog"""
import discord
from discord.ext import commands


class Mod(commands.Cog):
    """Class defining the Mod cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def modtest(self, ctx):
        """Command for testing Mod cog"""

        await ctx.send("Cog Mod is working!")

    # @commands.command(aliases=["k"])
    # @commands.has_permissions(kick_members=True)
    # async def kick(self, ctx, member: discord.Member, reason=None):
    #     """Kick a member from the server"""

    #     moderator = ctx.author
    #     guild = ctx.guild

    #     await member.kick(reason=reason)
    #     await ctx.send(f"**[!]** You have been kicked from {guild.name} with reason {reason}")

    # @kick.error
    # async def on_kick_error(self, ctx, error):
    #     """Handles errors on a kick command"""

    #     if isinstance(error, commands.CheckFailure):
    #         await ctx.send("**[-]** You do not have permission to kick this member.")
    #     elif isinstance(error, commands.CommandInvokeError):
    #         await ctx.send("**[-]** I do not have permission to kick this member.")
    #     elif isinstance(error, commands.BadArgument):
    #         await ctx.send("**[-]** I cannot find this member to kick.")
    #     else:
    #         raise Exception

    @commands.command(aliases=["b"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason=None):
        """Ban a member from the server"""

        moderator = ctx.author
        guild = ctx.guild

        await member.ban(reason=reason)
        await ctx.send(f"**[!]** You have been banned from {guild.name} with reason {reason}")

    @ban.error
    async def on_ban_error(self, ctx, error):
        """Handles errors on a ban command"""

        if isinstance(error, commands.CheckFailure):
            await ctx.send("**[-]** You do not have permission to ban this member.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("**[-]** I do not have permission to ban this member.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("**[-]** I cannot find this member to ban.")
        else:
            raise Exception

    @commands.command()
    async def unban(self, ctx, *, member):
        """Command used to unban a previously banned member"""

        reason = f"Unbanned by {ctx.author}"
        banned_users = ctx.guild.bans()
        member_name, member_descriminator = member.split("#")
        author = ctx.author

        for bans in banned_users:
            user = bans.user
            if (user.name, user.descriminator) == (member_name, member_descriminator):
                await ctx.guild.unban(user, reason=reason)
                await ctx.send(f"**[!]** {ctx.author} unbanned {member_name}")
                break
        else:
            ctx.send(f"**[-]** {member_name} is not banned...")


def setup(bot):
    """Adds the cog to the bot"""

    bot.add_cog(Mod(bot))
