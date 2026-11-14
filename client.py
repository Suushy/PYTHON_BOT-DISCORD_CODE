import discord

token = "Your Token"
intents = discord.Intents.all()

client = discord.Client(intents=intents)

client.run(token=token)
