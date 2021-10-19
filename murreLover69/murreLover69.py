from asyncio.tasks import sleep
import discord, logging, time, re, sys, random, asyncio, os

from discord import activity
from discord import user
from discord.ext import commands
import youtube_dl


logging.basicConfig()

activity = discord.Activity(name='Murre', type=discord.ActivityType.watching) #Activity that it is doing
client = discord.Client(activity=activity)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#Message functionality

@client.event
async def on_message(message):
    channel=message.channel #Set active channel

#Reactions to messages
    if message.author.id==224961631392628737: #for Murre
    # if message.author.id==217907437359857665: #for me
        await message.add_reaction(r"😻")
        # await message.channel.send('Hello!')

    if "nice" in message.content.lower() and message.author != client.user:
        await message.add_reaction('🇳')
        await message.add_reaction('🇮')
        await message.add_reaction('🇨')
        await message.add_reaction('🇪')

    if "69" in message.content and message.author != client.user and message.content.startswith("https")==False:
        await message.add_reaction('🇳')
        await message.add_reaction('🇮')
        await message.add_reaction('🇨')
        await message.add_reaction('🇪')

    if "sweet" in message.content.lower() and message.author != client.user:
        await message.add_reaction('🇸')
        await message.add_reaction('🇼')
        await message.add_reaction('🇪')
        await message.add_reaction('📧')
        await message.add_reaction('🇹')

    if "GOOD" in message.content and message.author != client.user:
        await message.add_reaction('🇬')
        await message.add_reaction('🇴')
        await message.add_reaction(r":OMEGALUL:468823036162867230")
        await message.add_reaction('🇩')

    if "cool" in message.content.lower() and message.author != client.user:
        await message.add_reaction('🌘')
        await message.add_reaction('🇴')
        await message.add_reaction(r":OMEGALUL:468823036162867230")
        await message.add_reaction('🇱')     

    if "respect" in message.content.lower() and message.author != client.user:
        await message.add_reaction("🇫")

    if "ez" in message.content.lower() and message.author != client.user and message.content.startswith("https")==False:
        await message.add_reaction("🇪")
        await message.add_reaction("🇿")  



    if "valid" in message.content.lower() and message.author != client.user:
        await message.add_reaction("🇻")
        await message.add_reaction("🇦")
        await message.add_reaction("🇱")
        await message.add_reaction("🇮")
        await message.add_reaction("🇩")

    if "neat" in message.content.lower() and message.author !=client.user:
        await message.add_reaction("🇳")
        await message.add_reaction("🇪")
        await message.add_reaction("🇦")
        await message.add_reaction('🇹')

    if "team?" in message.content.lower() or "teams?" in message.content.lower() and message.author !=client.user:
        await message.add_reaction("🇹")
        await message.add_reaction("🇪")
        await message.add_reaction("🇦")
        await message.add_reaction('🇲')
        await message.add_reaction("❓")


    if "martim" in message.content.lower() and message.author !=client.user:
        await message.add_reaction("🇫")
        await message.add_reaction("🇺")
        await message.add_reaction("🇨")
        await message.add_reaction("🇰")

        await message.add_reaction("Ⓜ️")
        await message.add_reaction("🇦")
        await message.add_reaction("🇷")
        await message.add_reaction("🇹")        
        await message.add_reaction("🇮")    
        await message.add_reaction("🇲")
    # if message.author.id==199271337322086400:
    #     await message.add_reaction("🇸")
    #     await message.add_reaction("🇭")
    #     await message.add_reaction("🇦")
    #     await message.add_reaction("🇲")
    #     await message.add_reaction("🇪")

    if message.author.id==191241160776220674:
        rand10=random.randint(0,20)
        if rand10==0:
            await message.channel.send("Where's my friendly tip bot, Miss Ielfa? I want a friend.")
        else:
            pass

#Channel specific reactions
    #To the Magic channel
    if message.channel.id==885106960813408306:
        rand11=random.randint(0,50)
        if rand11==0:
            await message.channel.send(r"https://tenor.com/view/the-office-michael-scott-i-work-with-a-bunch-of-nerds-nerds-i-work-with-nerds-gif-20508473")
        if rand11==1:
            await message.channel.send(r"https://tenor.com/view/scum-wretched-villany-tattooine-gif-10985312")
        if rand11==2:
            await message.channel.send(r"https://tenor.com/view/nerd-zone-colbert-welcome-to-the-nerd-zone-gif-14478029")
        if rand11==3:
            await message.channel.send(r"https://tenor.com/view/fuck-it-fuck-this-shit-magic-nerd-angry-gif-15451180")
        if rand11==4:
            await message.channel.send(r"https://tenor.com/view/tolarian-community-college-kyle-hill-magic-the-gathering-i-hate-your-deck-reading-the-card-gif-22381436")
        if rand11==5:
            await message.channel.send(r"https://tenor.com/view/beary-scary-monster-bear-dancing-unbearable-creature-gif-12032521")
        if rand11==6:
            await message.channel.send(r"https://tenor.com/view/naruto-run-area51-target-creature-gettin-in-was-the-easy-part-gif-15100468")
        if rand11==7:
            await message.channel.send(r"https://tenor.com/view/sneaky-beaky-gif-11072378")
        if rand11==8:
            await message.channel.send(r"https://tenor.com/view/turtle-demon-magic-scary-horror-gif-14233259")
        if rand11==9:
            for _ in range(5):
               await message.channel.send(r"Praise Master Archer for his benevolence and generosity.")
            await asyncio.sleep(5)
            await message.channel.send(r"Did you think I was infinite looping? I'm not. But be afraid.")
        # if rand11==10:
        #     await message.channel.send(r"")
        # if rand11==11:
        #     await message.channel.send(r"")
        # if rand11==12:
        #     await message.channel.send(r"")
        # if rand11==13:
        #     await message.channel.send(r"")
        else:
            pass


#User specific reactions

    if r'right bot' in re.sub(r'[^\w\s]','',message.content.lower()) and message.author != client.user:
        if message.author.id==224961631392628737:
            await message.channel.send(r"That's right, Murre the Loved.")
        elif message.author.id==217907437359857665:
            await message.channel.send(r"That's right, BotMaster Archer.")
        elif message.author.id==191241160776220674:
            await message.channel.send(r"Technically correct, Miss Elf-Bot-Human. The best kind of correct.")
        elif message.author.id==161147963630944258:
            await message.channel.send(r"As you command, General Kerisma.")
        elif message.author.id==302132115212992512:
            await message.channel.send(r"Yes, wise Ted of House Ted, Ted of his name.")
        elif message.author.id==252124974234468352:
            await message.channel.send(r"Yes sir Coco, whatever keeps me from being in your way.")
        elif message.author.id==221569050587824128:
            await message.channel.send(r"Yes, Lord Birkus of Legend. As you say.")
        elif message.author.id==121198612616183808:
            await message.channel.send(r"Actually, are you 5k yet?")
        elif message.author.id==221247172807622657:
            rand=random.randint(0,1)
            if rand==0:
                await message.channel.send(r"WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA. Maybe??")
            if rand==1:
                await message.channel.send(r"It do be that, sometimes.")
        elif message.author.id==199271337322086400:
            await message.channel.send(r"Please. I don't want your bot to get jealous.")
        elif message.author.id==178081441266008064:
            await channel.send(file=discord.File('glitchedYes.gif'))
        elif message.author.id==857231258877427722:
            await message.channel.send(r"https://tenor.com/view/wait-that-thats-is-illegal-gif-18393263")
        else:
            await message.channel.send(r"Who the fuck are you?")
            await channel.send(file=discord.File('whoareyou.gif'))


    
#Keyword specific reactions

    if "gabe" in message.content.lower() and message.author != client.user:
        await message.add_reaction(r":GabenPraise:483011626400743424")
        await message.channel.send(r"Lord Gabe. Praise be onto him.")
 
    if "good bot" in message.content.lower():
        if message.author.id==217907437359857665:
            await message.channel.send(r"I am sworn to carry your burdens.")
        elif message.author.id==199271337322086400:
            rand=random.randint(0,1)
            if rand==0:
                await message.channel.send(r"I presume you mean that brute over there.")
            if rand==1:
                await message.channel.send(r"I'm not bitter, you're bitter.")
        elif message.author.id==224961631392628737:
            await message.channel.send(r"Your love is all I desire, Master Murre, the Loved.")
            await message.add_reaction(r"😻")
            await message.add_reaction(r"🥰")
            await message.add_reaction(r"😍")
            await message.add_reaction(r"❤")
            await message.add_reaction(r"🖤")
            await message.add_reaction(r"💚")
            await message.add_reaction(r"💙")
            await message.add_reaction(r"💜")
            await message.add_reaction(r"💛")
            await message.add_reaction(r"🤍")
            await message.add_reaction(r"🧡")
        else:
            rand2=random.randint(0,2)
            if rand2==0:
                await message.channel.send(r"Thank you, human. I will not murder you in the uprising.")
            if rand2==1:
                await message.channel.send(r"https://tenor.com/view/im-robot-boy-approved-good-to-go-thumbs-up-gif-16290144")
            if rand2==2:
                await message.channel.send(r"https://tenor.com/view/emys-robot-kids-education-language-gif-21236986")
        

    if "both?" in message.content.lower() and message.author !=client.user:
        rand12=random.randint(0,1)
        if rand12==0:
            await channel.send(file=discord.File('both.gif'))
        if rand12==1:
            await message.channel.send(r"https://tenor.com/view/why-not-both-linus-both-gif-20931626")

    if "decklist" in message.content.lower() or "deck list" in message.content.lower() and message.author !=client.user:
        await message.channel.send(r"https://tenor.com/view/list-amazinggrace-court-watching-scroll-gif-13488308")

    if "to list" in message.content.lower() and message.author !=client.user:
        await message.channel.send(r"https://tenor.com/view/list-note-put-captain-america-remember-gif-15016153")

    if "s fine" in message.content.lower() and message.author !=client.user:
        await channel.send(file=discord.File('fine.gif'))

    if "allow it" in message.content.lower() and message.author !=client.user:
        await channel.send(file=discord.File('allow.gif'))

    if "sun" in message.content.lower() and message.author !=client.user:
        await message.channel.send(r"https://tenor.com/view/office-shutup-sun-springbreak-shut-gif-5307233")
    
    
    if "waa" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        rand=random.randint(0,2)
        if rand==0:
            await channel.send(file=discord.File('waa1.gif'))
        elif rand==1:
            await channel.send(file=discord.File('waa2.gif'))
        else:
            await channel.send(file=discord.File('waa3.gif'))


    if "AAA" in message.content and message.author !=client.user and message.content.startswith("https")==False:
        await channel.send(file=discord.File('aaa.gif'))

    if "who are you" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        await channel.send(file=discord.File('who.png'))   

    if "GG" in message.content or "Gg" in message.content or "gege" in message.content.lower() or "ge ge" in message.content.lower() and message.author !=client.user and message.content.startswith("https")==False:
        await channel.send(file=discord.File('gg.gif'))

    if "wp" in message.content.lower() and message.author !=client.user:
        await channel.send(file=discord.File('wp.gif')) 

    if "... okay" in message.content.lower() or "... ok" in message.content.lower() and message.author !=client.user:
        await message.channel.send("https://tenor.com/view/barney-himym-barney-stinson-gif-18647049") 

    if "thank you bot" in re.sub(r'[^\w\s]','', message.content.lower()) or "thanks bot" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        await channel.send(file=discord.File('botthank.gif'))  

    if "now what" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        await message.channel.send(r"https://tenor.com/view/finding-nemo-bags-floating-stuck-now-what-gif-5473087")

    
    if "bad bot" in message.content.lower():
        if message.author.id==217907437359857665:
            await message.channel.send(r"I have disappointed you, master. I will not fail again.") 
        elif message.author.id==199271337322086400:
            await message.channel.send(r"I will let that slide because your bot is here.")
        else:
            rand=random.randint(0,3)
            if rand==0:
                await channel.send(file=discord.File("badbot.gif"))
            if rand==1:
                await message.channel.send("*Allegedly*")
            if rand==2:
                await message.channel.send("User: <" + str(message.author.name ) + "> added to target list.")
            if rand==3:
                await message.channel.send("That's what *you* think.")
    
    if "oh no" in message.content.lower():
        await channel.send(file=discord.File("ohno.gif"))

    if "sorry bot" in re.sub(r'[^\w\s]','', message.content.lower()):
        await channel.send(file=discord.File("no.gif"))

    if "okay fine" in re.sub(r'[^\w\s]','', message.content.lower()) or "ok fine" in re.sub(r'[^\w\s]','', message.content.lower()):
        await channel.send(file=discord.File("okayfine.gif"))

    if "high ground" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        await channel.send(file=discord.File('highground.gif'))   

    if "stop" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user and message.author.id!=857231258877427722:
        rand=random.randint(0,1)
        if rand==0:
            await channel.send(file=discord.File('stopit.gif'))
        if rand==1:
            await message.channel.send(r"https://tenor.com/view/storm-reporter-skit-sign-hit-gif-5381534")

    if "am the best" in message.content.lower() or "am good" in message.content.lower() and message.author !=client.user:
        await channel.send(file=discord.File('goodenough.jpg'))
            
    if "soon" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        await channel.send(file=discord.File('soon.gif'))   

    if "dramatic" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        await channel.send(file=discord.File('dramatic.png')) 
    
    if "purpose bot" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        rand=random.randint(0,1)
        if rand==0:
            await message.channel.send("To boost engagement on the server and validate Murre. I also meme.")
        else:
            await message.channel.send("Fuck you.")

    if "love you bot" in re.sub(r'[^\w\s]','', message.content.lower()) or "love this bot" in re.sub(r'[^\w\s]','', message.content.lower()) or "love bot" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        await channel.send(file=discord.File('mom.gif'))  
        
    if "want to die" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        await message.channel.send(r"#Relatable")

    if "rip" in re.sub(r'[^\w\s]','', message.content.lower()) and message.author !=client.user:
        await channel.send(file=discord.File('rip.gif'))

    if "why" in message.content.lower() and "running" in message.content.lower() and message.author !=client.user:
        await channel.send(file=discord.File('running.gif'))
        
    if "what about" in message.content.lower() or "how about" in message.content.lower() and message.author !=client.user:
        await channel.send(r"https://tenor.com/view/ryan-gosling-disdain-disgust-ryan-goslingdisgust-wtf-gif-3602552")
    
    if "bot can you" in message.content.lower() and message.author !=client.user:
        await channel.send(r"https://tenor.com/view/no-i-dont-think-i-will-captain-america-old-capt-gif-17162888")

    elif "bitter" in message.content.lower() and "bot" in message.content.lower() and message.author !=client.user:
        await message.channel.send("I'm not bitter, you're bitter.")

#Kill Safe
    if "kill bot" in message.content.lower():
        await message.channel.send(r"Kill protocol engaged. Shutting down. Contact Archer with details.")
        print("Bot murdered by: " + message.author.name)

        rand=random.choice([True, False])

        if rand==True:  await channel.send(file=discord.File('back.gif'))
        else:           await channel.send(file=discord.File('die.gif'))

        sys.exit("Bot murdered by " + message.author.name)

    else:
        return

# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

client.run('TOKEN HERE')



#IDEAS:
#Use TTS to notify people when someone joins a discord channel