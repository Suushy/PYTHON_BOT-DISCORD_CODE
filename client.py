import discord

token = "TON TOKEN"
intents = discord.Intents.all()

client = discord.Client(intents=intents)

client.run(token=token)