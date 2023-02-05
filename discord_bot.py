import discord
from discord.ext import commands
from chat import chat_with_bot


Token = 'MTA3MTgyMzI2Nzg1MTE0OTM4Mg.GBEQn9.xWwABR558LNedRHB6gR0o8Eyy_HtbgtB_7qzmc'

client = commands.Bot(command_prefix = "$" , intents = discord.Intents.all())

@client.event
async def on_ready():
    print('success bot is running ')

@client.command()
async def ask(message):
    await message.reply('pinnged !')

client.run(Token)