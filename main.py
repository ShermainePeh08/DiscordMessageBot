# importing required libraries 
import os 
from dotenv import load_dotenv
import requests 
import json 
import discord
from discord.ext import commands 

# load dotenv
load_dotenv()

# registering a command with $ prefix and intents to allow all permissions
client = commands.Bot(command_prefix = '$', intents = discord.Intents.all())

# accessing token from .env
token = os.getenv('DISCORD_TOKEN')

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

# requesting from API and getting a quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

# testing bot’s login using print statement
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # get the message content & username
    username = str(message.author).split("#")[0]
    user_message = message.content
    
    # if hello in message, reply with hi
    if "hello" in user_message:
        await message.channel.send("hi")
        
    # if message startswith hello, reply hello    
    if user_message.startswith("hello"):
        await message.channel.send("hello")
    
    # check if words exists in sad_words list
    # activating get_quote function set earlier on 
    if any(word in user_message for word in sad_words):
        await message.channel.send(get_quote())
        
    await client.process_commands(message)

# returning arguments if command detected
@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

# activating the bot
client.run(token)