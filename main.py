import discord
import os
from discord.ext import commands
from apikeys import * #get token

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.message_content = True

client = commands.Bot(command_prefix='$', intents = intents)

@client.event #Bot starts
async def on_ready():
    await client.change_presence(activity = discord.Game("Fuck Sayer"))
    print("Bot is ready, " + "Token = " + token)
    print("-------------------------")

inital_extensions = []
for filename in os.listdir(path='./cogs'):
    if filename.endswith('.py'):
        inital_extensions.append("cogs." +filename[:-3])


if __name__ == '__main__':
    for extensions in inital_extensions:
        client.load_extension(extensions)



client.run(token)