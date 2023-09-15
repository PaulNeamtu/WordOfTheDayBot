import datetime, pytz
import discord, requests
from bs4 import BeautifulSoup
from discord.ext import tasks

#gets the text out of the merriam-webster website so that the bot may extract the relevant information
def getWebOut():
    #important variables
    url = 'https://www.merriam-webster.com/word-of-the-day'
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    wordType = ''

    #in order to clean up the html text from the website, blacklist common elements
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        # there may be more elements you don't want, such as "style", etc.
    ]

    #put text into output string
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    #return the output string
    return output

#function that returns the type of word by splitting the output string on specific parameters
def getWordType():
    output = getWebOut()

    wordType = output.split('header')[-1].split('<')[0]
    wordType = wordType.strip()
    return wordType

#function that returns the pronunciation of word by splitting the output string on specific parameters
def getWordPronunce():
    output = getWebOut()

    wordPro = output.split('>\\')[-1].split('\\<')[0]
    return wordPro

#function that returns the word of the day by splitting the output string on specific parameters
def getWord():
    output = getWebOut()

    word = output.split('Word Of The Day:')[-1].split('|')[0]
    return " " + word

#function that returns the definition of the word by splitting the output string on specific parameters
def getDef():
    output = getWebOut()

    definition = output.split('What It Means')[-1].split('See the entry')[0]
    return definition

#function that returns the word in a specific context by splitting the output string on specific parameters
def getCon():
    output = getWebOut()

    context = output.split('in Context')[-1].split('Subscribe WOD Box ')[0]
    context = context.strip()
    return context

#function that returns a fun fact for the word by splitting the output string on specific parameters
def getFunFact():
    output = getWebOut()

    didYouKnow = output.split('Did You Know?')[-1].split('Test Your Vocabulary with')[0]
    return didYouKnow


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Set time for bot to post in specified channel
# 14:30 UTC is 10:30 EST
time = datetime.time(hour=14, minute=30)

@tasks.loop(time = time) #Create the task
#function to schedule the message daily
async def scheduleDaily():
    channel = client.get_channel(1148423607253479486)
    await channel.send("**" + getWord() + "** \n*" + getWordType() + "* | " + getWordPronunce() + "\n\nWhat it means: " + getDef())

@client.event
async def on_ready():
    if not scheduleDaily.is_running():
        scheduleDaily.start() #If the task is not already running, start it.

@client.event
#function which handles the messages that the bot sends
async def on_message(message):
    if client.user.id != message.author.id:
        #the channel.id of the channel you wish the bot to send messages to should be put here
        if message.channel.id == : #make sure you add the channel id or the code wont work
            #if another person in the discord server sends a specific message in the 'word of the day' channel, the bot will respond with a specific type of message
            if message.content.startswith('!context'):
                channel = client.get_channel() #make sure you add the channel id or the code wont work
                await channel.send("The word in context: \n" + getCon())
            elif message.content.startswith('!funfact'):
                channel = client.get_channel() #make sure you add the channel id or the code wont work
                await channel.send("Did you know: " + getFunFact())

#Each discord bot has a token that must be placed here
client.run('put token here')

