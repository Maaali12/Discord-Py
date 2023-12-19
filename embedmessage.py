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

#Command that triggers when you write "!embedmessage"
@client.event
async def on_message(message):
    if message.content.startswith('!embedmessage'):

        embedVar = discord.Embed(title="**This is a Embed Message**", description="", color=0xD88E61)
        embedVar.add_field(name="**Hello**", value="Hello World", inline=False)
        embedVar.add_field(name="", value="Hello again!", inline=False)

        await message.delete() #deletes the message that triggered the command
        await message.channel.send(embed=embedVar)

#Run the bot with your token
client.run(bot_token)