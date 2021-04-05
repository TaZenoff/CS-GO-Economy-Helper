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
        
        #Start the script to drop the weapon to my friend
        os.system("start drop.pyw")

client=MyClient() #MyClient is the class with discord bot

with open("discordBotToken.txt","r") as f: #Read the token from "discordBotToken.txt"
    botToken=f.readline()

try:
    client.run(botToken) #My discord bot token
finally: #Before the code stops
    with open("config.txt","w") as f: #Clear the config.txt file
        f.writelines("")