import discord
from discord.ext import commands
from chat import chat_with_bot


Token = 'MTA3MTgyMzI2Nzg1MTE0OTM4Mg.GBEQn9.xWwABR558LNedRHB6gR0o8Eyy_HtbgtB_7qzmc'

async def send_message(message,user_message,is_private):
    try:
        chat = chat_with_bot.talktobot(user_message)
        print(user_message)
        await message.author.send(chat) if is_private else await message.channel.send(chat)
    except Exception as e:
        print(e)


def run_discord_bot():

    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print("{} is now running !".format(client.user))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print("{} said : {} in {}".format(username,user_message,channel))

        if user_message.startswith('%'):
            user_message = user_message[1:]
            await send_message(message , user_message, is_private=True)
        else:
            await send_message(message , user_message, is_private=False)

    client.run(Token)


if __name__ == '__main__':
    run_discord_bot()