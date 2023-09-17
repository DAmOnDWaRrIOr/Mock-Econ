import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(message):
        if message.author == client.user:
            return

    @commands.command()
    async def cmdtemplate(self, ctx):
        await ctx.send("Test")

    @commands.command()
    async def embedtemplate(self, ctx):
        embed = discord.Embed(title = "Title",url = "",description = "description",color=0x00FFFF) #,color=Hex code
        embed.set_author(name = ctx.author.display_name, url = "",icon_url = ctx.author.avatar.url)
        embed.add_field(name = "Feild 1", value = "Test 1",inline = True)
        embed.add_field(name = "Feild 2", value = "Test 2",inline = True)
        embed.set_footer(text = "Footer")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Commands(client))