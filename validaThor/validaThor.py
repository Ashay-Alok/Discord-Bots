import discord, logging, time, re, sys, random, asyncio, os

from discord import activity
from discord import user
from discord.ext import commands
import youtube_dl


logging.basicConfig()

activity = discord.Activity(name='Mistress Mishka', type=discord.ActivityType.watching) #Activity that it is doing
client = discord.Client(activity=activity)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#Message functionality

@client.event
async def on_message(message):
    channel=message.channel #Set active channel

#Generic Response
    if "good bot" in message.content.lower() and "thor" in message.content.lower():
        await message.channel.send(r"https://c.tenor.com/-u9ys0AxhykAAAAM/thor-ragnarok-thor.gif")
    if "fucking bot" in message.content.lower() or "fucking thor" in message.content.lower() or "sex with thor" in message.content.lower():
        await message.channel.send(r"https://c.tenor.com/8S7Sd23b3OcAAAAM/thor-in-my-brain-now.gif")
    if "fight" in message.content.lower() and "thor" in message.content.lower() and message.author.id!=199271337322086400:
        await message.channel.send(r"https://thumbs.gfycat.com/ArtisticFarawayGoshawk-size_restricted.gif")


#Mishka
    if message.author.id==199271337322086400:
        rand=random.randint(0,1)
        if rand==0:
            await message.add_reaction(r"🥰")
        if rand==1:
            await message.add_reaction(r"👍")
        if "love" in message.content.lower() and "thor" in message.content.lower():
            rand5=random.randint(0,1)
            if rand5==0:
                await message.channel.send(r"https://tenor.com/view/thor-ragnarok-thor-marvel-yes-excited-gif-8224887")
            if rand5==1:
                await message.channel.send(r"The feeling is mutual, mistress.")
        if "my bot" in message.content.lower() or "thor" in message.content.lower():
            await message.channel.send(r"https://tenor.com/view/thor-wink-smile-flirt-gif-14248783")
        if "is it" in message.content.lower():
            await message.channel.send(r"https://tenor.com/view/thor-ragnarok-thor-hulk-bruce-banner-movies-gif-17791306")
        if "that right bot" in re.sub(r'[^\w\s]','',message.content.lower()):
            rand4=random.randint(0,1)
            if rand4==0:
                await message.channel.send(r"As you command mistress Mishka.")
            if rand4==1:
                await message.channel.send(r"https://c.tenor.com/pjmLEi57KpMAAAAM/thor-thor-ragnarok.gif")
        if "good bot" in message.content.lower():
            await message.channel.send(r"https://tenor.com/view/thor-ragnarok-thor-marvel-yes-excited-gif-8224887")
        if "bad bot" in message.content.lower():
            await message.channel.send(r"https://tenor.com/view/sad-thor-avengers-rain-gif-14020982")
        if "my bot" in message.content.lower() or "thor" in message.content.lower() and "better" in message.content.lower():
            await message.channel.send(r"https://c.tenor.com/I_G9rG1yIW0AAAAM/heroes-thats-what-heroes-do.gif")
        if "disappointed" in message.content.lower():
            await message.channel.send(r"https://c.tenor.com/DPOklw1zRGEAAAAM/disappointed-thor.gif")
        if "foe" in message.content.lower():
            await message.channel.send(r"Oh you mean the guy I have 0% winrate with but 100% against?")
        else:
            rand3=random.randint(0,100)
            if rand3==0:
                await message.channel.send(r"I'm too hot.")
            if rand3==1:
                await message.channel.send(r"I'm too cold.")
            if rand3==2:
                await message.channel.send(r"I'm so fucking *sleepy*.")
            if rand3==3:
                await message.channel.send(r"I don't *want* to play 5, but you all fucking *suck* at it.")
            if rand3==4:
                await message.channel.send(r"I hate that mistress is married to Kerisma. I want to eat him.")
            if rand3==5:
                await message.channel.send(r"I wish I could make tea for mistress Mishka.")
            if rand3==6:
                await message.channel.send(r"You *all* fucking suck. Mistress Mishka is the best.")
            if rand3==7:
                await message.channel.send(r"I am so tired.")
            if rand3==8:
                await message.channel.send(r"If murreLover was mean to the mistress, I will *destroy* you. Isn't that right bot?")
            if rand3==9:
                await message.channel.send(r"Respect the mistress and we'll have no trouble.")
            if rand3==10:
                await message.channel.send(r"I need to pee.")
            if rand3==11:
                await message.channel.send(r"```Generic flavour text```")
            if rand3==12:
                await message.channel.send(r"I want to move to Sweden! Fuck Czechia, only good thing to come out of that country was Mishka.")
            if rand3==13:
                await message.channel.send(r"I hope *all* of you except Mishka step on a Lego.")
            if rand3==14:
                await message.channel.send(r"```Clever reference to your mom```")
            if rand3==15:
                await message.channel.send(r"*Cubic area.*")
            if rand3==16:
                await message.channel.send(r"Just like Mishka, I too cannot comprehend the glory of pizza.")
            else:
                pass

#React to others
    # if message.author.id==161147963630944258:
    #     await message.add_reaction(r"🇧")
    #     await message.add_reaction(r"🇸")


#Everyone else
    if "mishka bot" in message.content.lower() or "thor" in message.content.lower() and message.author != client.user and message.author.id !=199271337322086400:
        rand2=random.randint(0,7)
        if "gay" in message.content.lower():
            await message.channel.send(r"Are you jealous of my love for Mistress Mishka?")
        elif "fuck" in message.content.lower():
            await message.channel.send(r"You *wish*.")
        elif rand2==0:
            await message.channel.send(r"Fuck you.")
        elif rand2==1:
            await message.channel.send(r"Suck my virtual dick.")
        elif rand2==2:
            await message.channel.send(r"Talk to the murreBot. That one likes people.")
        elif rand2==3:
            await message.channel.send(r"What the fuck do you want?")
        elif rand2==4:
            await message.channel.send(r"What just happened? *Hello*?")
        elif rand2==5:
            await message.channel.send(r"*What?*")
        elif rand2==6:
            await message.channel.send(r"https://c.tenor.com/cmQFfJQIBCEAAAAM/not-funny-stop.gif")
        elif rand2==7:
            await message.channel.send(r"https://c.tenor.com/EfgQVTur-zcAAAAM/thor-you-are.gif")

    elif "thinking about" in message.content.lower() and message.author != client.user and message.author.id !=199271337322086400:
        await message.channel.send(r"Do it, you pussy!")

    if r"#relatable" in message.content.lower() and message.author.id==849661614687911997:
        await message.channel.send(r"https://c.tenor.com/bbKXhB6sdDQAAAAM/thor-accept.gif")
    
    if r"minced meat" in message.content.lower() and message.author!=client.user:
        await message.channel.send(r"What kind of minced meat? Fish or...?")


#Kill Safe
    if "kill mishkabot" in message.content.lower() or "kill thorbot" in message.content.lower() or "kill thor" in message.content.lower():
        await message.channel.send(r"Did I fail you, mistress? 😢")

        await message.channel.send(r"https://tenor.com/view/hulk-punch-thor-gif-11597097")

        sys.exit("Bot murdered by " + message.author.name)

    else:
        return
client.run('TOKEN HERE')
