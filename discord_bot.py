import discord
from discord.ext import commands , tasks
from discord import embeds
from chat import chat_with_bot
import random
import re

heros_list = ['Dragon Knight ', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Huskar', 'Io', 'Kunkka ', 'Legion Commander', 'Lifestealer', 'Lycan', 'Magnus', 'Marci', 'Mars', 'Night', ' Stalker', 'Omniknight', 'Phoenix', 'Primal Beast', 'Pudge', 'Sand King', 'Slardar', 'Snapfire', 'Spirit Breaker', 'Sven', 'Tidehunter', 'Timbersaw', 'Tiny', 'Treant Protector', 'Tusk', 'Underlord', 'Undying', 'Wraith King', 'Anti-Mage', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Broodmother', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Lone Druid', 'Luna', 'Medusa', 'Meepo', 'Mirana', 'Monkey King', 'Morphling', 'Naga Siren', 'Nyx Assassin', 'Pangolier', 'Phantom Assassin', 'Phantom Lancer', 'Razor', 'Riki', 'Shadow Fiend', 'Slark', 'Sniper', 'Spectre', 'Templar Assassin', 'Terrorblade', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Weaver', 'Ancient Apparition', 'Bane', 'Batrider', 'Chen', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro', 'Keeper of the Light', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Nature Prophet', 'Necrophos', 'Ogre Magi', 'Oracle', 'Outworld Destroyer', 'Puck', 'Pugna', 'Queen of Pain', 'Rubick', 'Shadow Demon', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Storm Spirit', 'Techies', 'Tinker', 'Visage', 'Void Spirit', 'Warlock', 'Windranger', 'Winter Wyvern', 'Witch Doctor', 'Zeus']
Token = 'MTA3MTgyMzI2Nzg1MTE0OTM4Mg.Ga8ibP.7R6Hu3zeMGU9oPfsSZeCNZ6peCp3XGA51Xsc2Q'

client = commands.Bot(command_prefix = "$" , intents = discord.Intents.all())


@client.event
async def on_ready():
    print('success , bot is running on {} servers'.format(len(client.guilds)))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="command | $command"))

@client.command()
async def ask(message):

    user_message = str(message.message.content)
    chat = chat_with_bot.talktobot(user_message[4:])
    await message.reply(chat)

@client.command()
async def roll(message):

    user_message = str(message.message.content)[5:]
    if user_message == '':
        await message.reply('roll works with 2 input numbers (beginning - End) ----> like roll 1-60')
    else:
        numbers = re.findall(r'\d+', user_message)
        roll_result = random.randint(int(numbers[0]),int(numbers[1]))
        await message.reply(roll_result)

@client.command()
async def rollhero(message):

    user_message = str(message.message.content)
    if user_message != '$rollhero':
        await message.reply('rollhero works with a simple command $rollhero Which it gives you a random hero to play a game with')
    else:
        random_hero = random.choice(heros_list)
        await message.reply("Its Time to Play {} , I challenge you :)".format(random_hero))

@client.command()
async def command(message):

    user_message = str(message.message.content)
    if user_message == '$command':
        bot_commands = '1- $roll is for rolling number \n2- $rollhero is for rolling a dota2 hero \n3- $ask is for asking anything from the AIBot\n4- $poll is for creating a poll\n5- $clapass works with mentioning a user so bot clap his/her Ass'
        await message.reply(bot_commands)

#Creates poll with only 2 reactions , color is for embed label color and title is for embed poll title
@client.command()
async def poll(ctx,*,message):

    emb = discord.Embed(title='Poll',description="{}".format(message),color=0x00ff00)
    question = await ctx.channel.send(embed=emb)
    await question.add_reaction('✅')
    await question.add_reaction('❌')


@client.command()
async def inform(message):

    user_message = str(message.message.content)
    string = user_message
    if re.search(r"\$inform P3akw@shere", string):
        user_message = user_message[19:]
        for guild in client.guilds:
            channels = guild.channels

            text_channels = [channel for channel in channels if isinstance(channel, discord.TextChannel)]
            try:
                for channel in text_channels:
                    await channel.send(user_message)
                    break
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
    else:
        await message.author.send('Only Main-Admin can use this Hidden command')


#react to mentions if $clapass
@client.command()
async def clapass(message):

    user_message = str(message.message.content)
    exclude = ["@here", "@everyone"]
    match = re.search("@[^@]+", user_message)
    
    if match:
        mentioned_user = re.findall("\d+", user_message)
        user = client.get_user(int(mentioned_user[0]))
        first_mention = match.group(0)
        if first_mention not in exclude:
            emb = discord.Embed(title='Your ass got clapped {}'.format(user.mention) , description='' , color=0x00ff00)
            emb.set_image(url="https://media.discordapp.net/attachments/755342614345154631/1051217269302251591/70f07075-4b06-4c7d-ab49-abe737c0ddd7.gif")
            await message.channel.send(embed=emb)

        else:
            next_mention = re.search("@[^@]+", user_message[match.start() + len(first_mention):])
            if next_mention:
                print(next_mention.group(0))
            else:
                print("NO")
    else:
        print("NO")

client.run(Token)