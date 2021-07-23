#The code was written by TaZenoff

import os

try:
    import discord
except:
    os.system("pip3 install discord")
    print("\nModule discord was successfully installed\n")
    import discord

try:
    import keyboard
except:
    os.system("pip3 install keyboard")
    print("\nModule keyboard was successfully installed\n")
    import keyboard

class MyClient(discord.Client):

    #Print the name of the account of the bot
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        #Print who wrote something and what did he write
        print('Message from {0.author}: {0.content}'.format(message))

        #Write in the config what my friend wants to get
        with open("config.txt","w") as f:
            f.write(message.content)

        for user in whitelist: #for each nickname in whitelist
            if str(user)==str(message.author): #if the user who wrote the message is in whitelist
                print("Valid user")
                #Start the script to drop the weapon to my friend
                os.system("start drop.pyw")

client=MyClient() #MyClient is the class with discord bot

try:
    whitelist=[]

    #read all lines from the whitelist.txt file
    with open("whitelist.txt", "r") as f:
        l=f.readlines()

    for user in l: #for each user in list l
        user=user.rstrip("\n") #remove "\n" from each nickname
        whitelist.append(user)
        
    client.run("ODI4MzM1MzIwODYwMTk2OTM1.YGoFYg.jX--wMiE2sKQjQpAEz3u-3sIENo") #My discord bot token (It runs the discord bot)
finally: #Before the code stops
    with open("config.txt","w") as f: #Clear the config.txt file
        f.writelines("")