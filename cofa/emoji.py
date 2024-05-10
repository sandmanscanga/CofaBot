import discord
import os
import requests

# Create a directory for emojis if it doesn't already exist
if not os.path.exists('emojis'):
    os.makedirs('emojis')

class EmojiDownloaderBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        for guild in self.guilds:
            await self.download_emojis(guild)

    async def download_emojis(self, guild):
        print(f'Downloading emojis from {guild.name}')
        for emoji in guild.emojis:
            # Construct the file path
            file_path = f'emojis/{emoji.name}.png'
            # Download and save the emoji
            with open(file_path, 'wb') as f:
                image = requests.get(emoji.url)
                f.write(image.content)
            print(f'Downloaded {emoji.name}')

bot = EmojiDownloaderBot()
bot.run('30b52cc50632bd8e3abe08e32de1861c8861ec1eb07a40e92ba3e37dcd834059')
