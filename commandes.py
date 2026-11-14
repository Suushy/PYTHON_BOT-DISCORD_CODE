import discord 
from discord.ext import commands

token = "Your Token"

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
 print(f'{bot.user} est connecté !')

@bot.command()
async def ping(ctx):
 latency = round(bot.latency * 1000)
 await ctx.send(f'𝗣𝗜𝗡𝗚 : {latency}𝗺𝘀')

if __name__ == '__main__':
 bot.run(token=token)
