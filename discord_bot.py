import discord
from discord.ext import commands , tasks
from discord import embeds
from chat import chat_with_bot , image_creation , translator
import random
import re

heros_list = ['Dragon Knight ', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Huskar', 'Io', 'Kunkka ', 'Legion Commander', 'Lifestealer', 'Lycan', 'Magnus', 'Marci', 'Mars', 'Night', ' Stalker', 'Omniknight', 'Phoenix', 'Primal Beast', 'Pudge', 'Sand King', 'Slardar', 'Snapfire', 'Spirit Breaker', 'Sven', 'Tidehunter', 'Timbersaw', 'Tiny', 'Treant Protector', 'Tusk', 'Underlord', 'Undying', 'Wraith King', 'Anti-Mage', 'Arc Warden', 'Bloodseeker', 'Bounty Hunter', 'Broodmother', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Hoodwink', 'Juggernaut', 'Lone Druid', 'Luna', 'Medusa', 'Meepo', 'Mirana', 'Monkey King', 'Morphling', 'Naga Siren', 'Nyx Assassin', 'Pangolier', 'Phantom Assassin', 'Phantom Lancer', 'Razor', 'Riki', 'Shadow Fiend', 'Slark', 'Sniper', 'Spectre', 'Templar Assassin', 'Terrorblade', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Weaver', 'Ancient Apparition', 'Bane', 'Batrider', 'Chen', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Enchantress', 'Enigma', 'Grimstroke', 'Invoker', 'Jakiro', 'Keeper of the Light', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Nature Prophet', 'Necrophos', 'Ogre Magi', 'Oracle', 'Outworld Destroyer', 'Puck', 'Pugna', 'Queen of Pain', 'Rubick', 'Shadow Demon', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Storm Spirit', 'Techies', 'Tinker', 'Visage', 'Void Spirit', 'Warlock', 'Windranger', 'Winter Wyvern', 'Witch Doctor', 'Zeus']
Token = 'MTA3MTgyMzI2Nzg1MTE0OTM4Mg.Ga8ibP.7R6Hu3zeMGU9oPfsSZeCNZ6peCp3XGA51Xsc2Q'

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "$", intents = intents ,help_command=None)


@client.event
async def on_ready():
    print('success , bot is running on {} servers'.format(len(client.guilds)))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Help | $helpme"))

@client.command()
async def ask(message):

    user_message = str(message.message.content)

    if user_message == '$ask':
        emb = discord.Embed(description='⚠️ $ask requires a question after $ask command', color=0x0d67d6)
        await message.channel.send(embed=emb)
    else:
        chat = chat_with_bot.talktobot(user_message[4:])
        await message.reply(chat)

@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message

    if message.reference is not None:
        channel = client.get_channel(message.channel.id)
        question_author_message = await channel.fetch_message(message.reference.message_id)
        if question_author_message.author.id == user.id and reaction.emoji == '🇮🇷':

            user_message = str(message.content)
            translate = translator.eng_to_farsi_translate(user_message)

            await message.edit(content=translate)
        else:
            await message.remove_reaction(reaction.emoji,user)

        

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
        emb = discord.Embed(description='⚠️ $rollhero doenst require anymore input - just use $rollhero', color=0x0d67d6)
        await message.channel.send(embed=emb)
    else:
        random_hero = random.choice(heros_list)
        await message.reply("Its Time to Play {} , I challenge you :)".format(random_hero))

@client.command()
async def helpme(message):

    user_message = str(message.message.content)
    if user_message == '$helpme':
        emb = discord.Embed(title='OracleMind Help Page', description='⚙️ In order to use commands use the prefix `$`\
        followed by the command name', color=0x0d67d6)
        emb.set_author(name='OracleMind' , icon_url='https://cdn.discordapp.com/app-icons/1071823267851149382/9c6f4e51b95efe0becd4efc1223d2a05.png')
        emb.add_field(name='Utility commands' , value=' `$ask` `$roll` `$rollhero` `$poll` `$image` `$donate`')
        emb.set_footer(icon_url ='https://img.icons8.com/color/512/python.png' , text = 'This Bot is made of Python and Openai(chatgpt)' )
        await message.channel.send(embed=emb)


#Creates poll with only 2 reactions , color is for embed label color and title is for embed poll title
@client.command()
async def poll(ctx,*,message):

    emb = discord.Embed(title='Poll',description="{}".format(message),color=0x0d67d6)
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
            if guild.id == 350682198011019289 :
                channels = guild.channels
                text_channels = [channel for channel in channels if isinstance(channel, discord.TextChannel)]
                try:
                    for channel in text_channels:

                        match = re.search(r"\b(bot|command)\b", channel.name, re.IGNORECASE)
                        if match:
                            await channel.send(user_message)
                            break
                        else:
                            # If "bot" is not found, search for "welcome" instead (case-insensitive)
                            match = re.search(r"\b(welcome)\b", channel.name, re.IGNORECASE)
                            if match:
                                await channel.send(user_message)
                                break
                            else:
                                print("No match found.")
                    break
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
        first_mention = match.group(0)
        if first_mention not in exclude:
            user = client.get_user(int(mentioned_user[0]))
            emb = discord.Embed(title='Your ass got clapped {}'.format(user.name) , description='{}'.format(user.mention) , color=0x0d67d6)
            emb.set_image(url="https://media.discordapp.net/attachments/755342614345154631/1051217269302251591/70f07075-4b06-4c7d-ab49-abe737c0ddd7.gif")
            await message.channel.send(embed=emb)

        else:
            await message.reply('Cannot mention everyone !')
    else:
        await message.reply('Could Not clap the User')



#counts in how many servers Oraclemind is running
@client.command()
async def svcount(message):

    await message.reply('success , bot is running on {} servers'.format(len(client.guilds)))


#create image $image
@client.command()
async def image(message):

    user_message = str(message.message.content)
    image_url = image_creation.generate_image(user_message[6:])
    
    if image_url[1] == 1:
        emb = discord.Embed(title=image_url[0], color=0x0d67d6)
        emb.set_image(url="https://media.discordapp.net/attachments/915659599045075025/936386591524544592/20220128_015424.gif")
        await message.channel.send(embed=emb)

    elif image_url[1] == 2:

        await message.reply(image_url[0])


#check for server names using OracleMind $svname
@client.command()
async def svnames(message):

    server_names = []
    for guild in client.guilds:
        server_names.append(guild.name)
    await message.author.send(server_names)


@client.command()
async def help(ctx):

    emb = discord.Embed(description='⚠️ This Command doesnt work ,Try $helpme', color=0x0d67d6)
    await ctx.channel.send(embed=emb)


@client.command()
async def donate(message):

    user_message = str(message.message.content)
    if user_message == '$donate':
        emb = discord.Embed(title='Crypto Donation', description='📥 In order to donate , Use of the\
        following ways', color=0x0d67d6)
        emb.set_author(name='OracleMind' , icon_url='https://cdn.discordapp.com/app-icons/1071823267851149382/9c6f4e51b95efe0becd4efc1223d2a05.png')
        emb.add_field(name='Tether (TRC20)' , value='TYESPZQMD31oU6bpgPQNbXizYhmhRiYMeC')
        emb.add_field(name='Cardano (Coin)' , value='addr1q9q378deyvt529zpp0nne5rv8fs5dzadcum7pcfzvgv8ll6v20ax8vff6gku6lej06vx0zx07jxen3m9g6tckevvctuqdmz38v')
        emb.add_field(name='USD COIN (TRC20)' , value='TYESPZQMD31oU6bpgPQNbXizYhmhRiYMeC')
        emb.add_field(name='TRON (COIN)' , value='TYESPZQMD31oU6bpgPQNbXizYhmhRiYMeC')
        emb.add_field(name='XRP (Coin)' , value='rao3Wec9zGwVDVn6g6RQbMR8ycBP1bA2QA')
        emb.set_footer(icon_url ='https://cdn.discordapp.com/attachments/1071841070977126420/1074419988284309544/generic-cryptocurrency-icon-512x508-icecu3wp.png' , text = 'Glad Youre on This Page 👀' )
        await message.channel.send(embed=emb)


#Run the Bot using Token
#WORK ON NOTIF FOR LOOP USE 'IN' METHOD ASWELL
client.run(Token)
