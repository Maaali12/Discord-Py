import discord
from discord.ext import commands

#Config
intents = discord.Intents.default()
client = discord.Client(intents=intents)

#you can get your token from https://discord.com/developers/applications/ and create a new application and bot
bot_token ="YOUR TOKEN HERE"

#Event that triggers when the bot is online
@client.event
async def on_ready():
    print(f'Successful Logged in as {client.user.name}')
    print("------------------------------------")

#Command that triggers when you write "!hello"
@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await message.channel.send("Hello!")
        await message.delete() #deletes the message that triggered the command

#Run the bot with your token
client.run(bot_token)