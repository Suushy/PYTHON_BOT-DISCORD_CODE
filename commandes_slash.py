import discord
import datetime
import random
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")
    try:
        synced = await bot.tree.sync()
        print(f'Commandes sync : {len(synced)}')
    except Exception as e:
        print(f'Erreur sync : {e}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'𝗣𝗜𝗡𝗚 : {round(bot.latency * 1000)} 𝗺𝘀')

@bot.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'𝗣𝗜𝗡𝗚 : {round(bot.latency * 1000)} 𝗺𝘀')

@bot.tree.command(name="userinfo", description="User info.")
async def userinfo(interaction: discord.Interaction, member: discord.Member = None):
    if member is None:
        member = interaction.user
    embed = discord.Embed(title=f"Information de {member.name}", color=discord.Color.blue())
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Compte créé le", value=member.created_at.strftime("%d/%m/%Y"), inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="serverinfo", description="Show server info.")
async def serverinfo(interaction: discord.Interaction):
    guild = interaction.guild
    embed = discord.Embed(title=f"Information du serveur : {guild.name}", color=discord.Color.red())
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    embed.add_field(name="Propriétaire : ", value=guild.owner.mention, inline=True)
    embed.add_field(name="Membres : ", value=guild.member_count, inline=True)
    embed.add_field(name="Date de création : ", value=guild.created_at.strftime("%d/%m/%Y"))
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="ping-pong", description="/ping = Pong !")
async def piing(interaction: discord.Interaction):
    await interaction.response.send_message("Pong 🏓!")

@bot.tree.command(name="ntm", description="tg fdp")
async def ntm(interaction: discord.Interaction):
    await interaction.response.send_message("ntm la pute, connard va")

@bot.tree.command(name="say", description="Say your message")
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message, ephemeral=True)

@bot.tree.command(name="roll", description="Lance un dé")
async def dé(interaction: discord.Interaction):
    results = random.randint(1, 6)
    await interaction.response.send_message(results)
    
bot.run("Your Token")
