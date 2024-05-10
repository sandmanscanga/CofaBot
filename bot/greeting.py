from discord.ext import commands
import discord
import json


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def greet(ctx):
    """Responds with a greeting message."""
    await ctx.send("Hello!")


def main(token_path: str = "token.json") -> None:
    # Define the bot and the command prefix
    bot = commands.Bot(command_prefix='!')

    with open(token_path, "r") as file:
        token_json = json.load(file)

    token = token_json["token"]

    bot.run(token)


if __name__ == "__main__":
    main()
