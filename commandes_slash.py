import discord
import random
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")
    try:
        synced = await bot.tree.sync()
        print(f'Commandes sync : {len(synced)}')
    except Exception  as e:
        print(f'Erreur sync : {e}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'𝗣𝗜𝗡𝗚 : {round(bot.latency * 1000)} 𝗺𝘀')

@bot.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'𝗣𝗜𝗡𝗚 : {round(bot.latency * 1000)} 𝗺𝘀')

bot.run("TON TOKEN")