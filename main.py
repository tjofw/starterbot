import discord
from discord.ext import commands
from discord.utils import get

TOKEN = 'ENTER TOKEN HERE' #Token from Discord Developer Portal

client = discord.Client()
client = commands.Bot(command_prefix = '.') #Change prefix to your choice

@client.event
async def on_ready():
    game = discord.Game("with code.. ")
    await client.change_presence(activity=game)
    print('Online! Succesfully Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def ping(ctx):
    pingspeed = f'{round(client.latency * 1000)}'
    embed = discord.Embed(colour=discord.Colour(0x7ed321), description=":ping_pong: " + pingspeed + " ms")
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def dm(ctx, user: discord.Member, *args):
    message = ""
    for word in args:
      message += word
      message += " "
    await user.send(f"{message}")
    await ctx.message.delete()

client.run(TOKEN)
