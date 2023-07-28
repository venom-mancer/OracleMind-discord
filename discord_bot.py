import discord
from discord.ext import commands , tasks
from discord import embeds
from chat import chat_with_bot , image_creation , translator
from dota2 import dota2_openapi
import json
import random
import re


with open('config.json') as user_file:
  file_contents = user_file.read()
  
parsed_json = json.loads(file_contents)

Token = parsed_json["Token"]

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
            translate = translator.eng_translator(user_message)

            await message.edit(content=translate)
        else:
            await message.remove_reaction(reaction.emoji,user)

        

@client.command()
async def roll(message):

    user_message = str(message.message.content)[5:]
    if user_message == '':
        emb = discord.Embed(description='⚠️ $roll works with 2 input numbers (beginning - End) like $roll 1-60', color=0x0d67d6)
        await message.channel.send(embed=emb)
    else:
        numbers = re.findall(r'\d+', user_message)
        roll_result = random.randint(int(numbers[0]),int(numbers[1]))
        await message.reply(roll_result)


@client.command()
async def helpme(message):

    user_message = str(message.message.content)
    if user_message == '$helpme':
        emb = discord.Embed(title='OracleMind Help Page', description='⚙️ In order to use commands use the prefix `$`\
        followed by the command name', color=0x0d67d6)
        emb.set_author(name='OracleMind' , icon_url='https://cdn.discordapp.com/app-icons/1071823267851149382/9c6f4e51b95efe0becd4efc1223d2a05.png')
        emb.add_field(name='Utility commands' , value=' `$roll` `$poll` `$donate` `$clapass`')
        emb.add_field(name='$ask command' , value='After using $ask then you gotta ask a question or talk to the bot')
        emb.add_field(name='$image command' , value='After using $image then you gotta describe the image you want to be drawn')
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
    if  str(message.author.id) == parsed_json["admin"]:
        user_message = user_message[8:]
        for guild in client.guilds:
            server = client.get_guild(guild.id)
            text_channels = server.text_channels
            found_channel = False
            for channel in text_channels:
                # check if the bot has permission to send messages in the channel
                permissions = channel.permissions_for(server.me)
                if 'bot' in channel.name or 'command' in channel.name or 'welcome' in channel.name or 'general' in channel.name and permissions.send_messages == True:
                    await channel.send(user_message)
                    found_channel = True
                    break
                if not found_channel and permissions.send_messages:
                    await channel.send(user_message)
                    break
                else:
                    pass
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
#if permission is not granted it wont work for you
@client.command()
async def svcount(message):
    if  str(message.author.id) == parsed_json["admin"]:

        await message.reply('success , bot is running on {} servers'.format(len(client.guilds)))
    else:
        emb = discord.Embed(description='⚠️ You Dont have the Permission for this command', color=0x0d67d6)
        await message.channel.send(embed=emb)

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

    filename = "svnames.txt"
    if  str(message.author.id) == parsed_json["admin"]:

        with open(filename, "w") as f:
            for guild in client.guilds:
                f.write("{} : {} \n".format(guild.name,guild.id))
        with open(filename, 'rb') as result_file:
                file = discord.File(result_file)

        await message.channel.send(file=file)
        file.close()
    else:
        emb = discord.Embed(description='⚠️ You Dont have the Permission for this command', color=0x0d67d6)
        await message.channel.send(embed=emb)

#disablled help command
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

@client.command()
async def inviteme(message):

    user_message = str(message.message.content)[10:]
    # Replace SERVER_ID with the ID of the server you want to create the invite link for
    # gets admin user id from json file and check if the user_massage is admin
    if  str(message.author.id) == parsed_json["admin"]:

        try:
            server = client.get_guild(int(user_message))
            # Get a list of invites for the server
            invites = await server.invites()

            # If there are no invites, create a new one
            if len(invites) == 0:
                invite = await server.text_channels[0].create_invite()
            else:
                # Use the first invite in the list
                invite = invites[0]

            # Send the invite link to the user who requested it
            await message.send(f"Here's an invite link for {server.name}: {invite.url}")
        except Exception as error:
            await message.send("Permission Denied !")
    else:
        emb = discord.Embed(description='⚠️ You Dont have the Permission for this command', color=0x0d67d6)
        await message.channel.send(embed=emb)

#player stats by their ID
@client.command()
async def player(message):

    user_message = str(message.message.content)[7:]
    playerinfo = await dota2_openapi.playerinfo(user_message)
    
    #reading from json file that was made in dota2 > dota2_openapi.py
    with open('match_result.json', 'r') as openfile:
    
        file_contents = openfile.read()
    #parsing and loading json
    parsed_json = json.loads(file_contents)

    #seprating infos from json file
    estimated_mmr =parsed_json[0]['mmr_estimate']['estimate']
    bestfriend = parsed_json[2][0]['personaname']
    winlose = parsed_json[1]["win"],parsed_json[1]["lose"]
    personname = parsed_json[0]["profile"]['personaname']
    avatarpfp = parsed_json[0]["profile"]['avatarfull']
    usersteamid = parsed_json[0]["profile"]['profileurl']

    #embed and send
    emb = discord.Embed(title=personname, color=0x0d67d6)
    emb.set_author(name='Player Info ℹ️')
    emb.set_image(url='{}'.format(avatarpfp))
    emb.add_field(name='Win/Lose' , value='{}'.format(winlose))
    emb.add_field(name='estimated MMR ' , value='{}'.format(estimated_mmr))
    emb.add_field(name='Best Friend' , value='{}'.format(bestfriend))
    emb.add_field(name='Steam id URL' , value='{}'.format(usersteamid))
    await message.reply(embed=emb)

#Look for better API
#Run the Bot using Token
client.run(Token)
