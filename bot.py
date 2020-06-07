import discord
import random


BOT_PREFIX = ("?", "!")

f=open("TOKEN.txt", "r")
TOKEN = f.readline()
f.close()

client = discord.Client()

#################################
# custom functions
#################################

def GetIdea():
    Genre = ["Simulation","Arcade","Educational","Action","Racing","Strategy","Puzzle","Role Playing Game","Adventure"]
    Chosengenre = random.choice(Genre)
    Rules = ["One life only","Aviod enemies","Must not be seen","Limited inventory","Bounce off walls","Can't touch the floor","Limited time","Can only move forwards"]
    Chosenrules = random.choice(Rules)
    Environment = ["Inside a computer","Jungle","City","Castle","Supermarket","At home","Island","Alternate reality","Space","Ocean"]
    Chosenenvironment = random.choice(Environment)
    Goal = ["Rescue","Capture","Find all items","Reach a destination","Complete the puzzle","Use all items","Escape","Survive","Remove all enemies","Destroy objects"]
    Chosengoal = random.choice(Goal)
    Wildcards = ["Something Spooky","Magic Spell","Colours","Household Chores","Music","Fairytale","Multiplayer","Fruit","Robots"]
    Chosenwildcards = random.choice(Wildcards)

    return [Chosengenre, Chosenrules, Chosenenvironment, Chosengoal, Chosenwildcards]


#################################
# End Of Custom Functions
#################################


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    message.content = message.content.lower()
    if message.content.startswith("!idea"):
        idea = GetIdea()
        await message.channel.send("Here's an idea:")
        await message.channel.send(f"Can you make a game in the **{idea[0]}** genre using **{idea[1]}** rule,\nthe environment could be **{idea[2]}** and the goal is **{idea[3]}**.\nAnd here's a wildcard, use **{idea[4]}**")
        await message.channel.send("I've used the Bafta Game Idea cards to create this! http://ygd.bafta.org/resources/game-idea-generator")
        await message.channel.send("If you don't like this idea, just reply with **!idea**")    

@client.event
async def on_ready():
    print(f"{client.user} has connected to discord!")

client.run(TOKEN)
