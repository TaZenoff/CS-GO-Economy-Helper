import keyboard
import time

#Read which gun my friend wants to get from a config file
with open("config.txt","r") as f:
    weapon=f.readline()

#Make the whole line uppercase
if weapon.isupper():
    pass
else:
    weapon=weapon.upper()

if weapon=="USP" or weapon=="GLOCK" or weapon=="P2000":
    weapon="DROP"

weapon=weapon.replace(" ","") #Replace all " " with nothing

dictionary={
    "DUAL": "e12e",
    "DUALBERETTAS": "e12e",
    "P250": "e13e",
    "CZ": "e14e",
    "CZ75": "e14e",
    "TEC9": "e14e",
    "TEC": "e14e",
    "FIVESEVEN": "e14e",
    "DEAGLE": "e15e",
    "REVOLER": "e15e",
    "NOVA": "e21e",
    "XM": "e22e",
    "XM1014": "e22e",
    "SAWEDOFF": "e23e",
    "MAG7": "e23e",
    "M249": "e24e",
    "NEGEV": "e25e",
    "MAC10": "e31e",
    "MAC": "e31e",
    "MP9": "e31e",
    "MP7": "e32e",
    "MP5": "e32e",
    "MP5SD": "e32e",
    "BIZON": "e35e",
    "PPBIZON": "e35e",
    "GALIL": "e41e",
    "GALILAR": "e41e",
    "AK47": "e42e",
    "AK": "e42e",
    "M4": "e42e",
    "M4A4": "e42e",
    "M4A1": "e42e",
    "M4A1S": "e42e",
    "SSG": "e43e",
    "SSG08": "e43e",
    "SG": "e44e",
    "SG553": "e44e",
    "AUG": "e44e",
    "AWP": "e45e",
    "G3SG1": "e46e",
    "G3SG": "e46e",
    "G3": "e46e",
    "AUTO": "e46e",
    "SCAR": "e46e",
    "SCAR20": "e46e",
    "ZEUS": "e53ee",
}

try:
    if weapon=="DROP":
        #Drop primary weapon if someone has dropped it to me
        keyboard.press("1")
        keyboard.release("1")
        time.sleep(0.1) #wait because if there is no time.sleep csgo wont press g
        keyboard.press("g")
        keyboard.release("g")

        time.sleep(0.1) #wait because if there is no time.sleep csgo wont press next button

        #Drop secondary weapon
        keyboard.press("2")
        keyboard.release("2")
        time.sleep(0.1) #wait because if there is no time.sleep csgo wont press g
        keyboard.press("g")
        keyboard.release("g")

        #Drop Zeus
        keyboard.press("3")
        keyboard.release("3")
        time.sleep(0.1) #wait because if there is no time.sleep csgo wont press 3 again
        keyboard.press("3")
        keyboard.release("3")
        time.sleep(0.1) #wait because if there is no time.sleep csgo wont press g
        keyboard.press("g")
        keyboard.release("g")

    elif weapon in dictionary: #if weapon is in the dictionary
        #Drop secondary weapon
        keyboard.press("2")
        keyboard.release("2")
        time.sleep(0.1) #wait because if there is no time.sleep csgo wont press g
        keyboard.press("g")
        keyboard.release("g")

        #Drop primary weapon if someone has dropped it to me
        keyboard.press("1")
        keyboard.release("1")
        time.sleep(0.1) #wait because if there is no time.sleep csgo wont press g
        keyboard.press("g")
        keyboard.release("g")

        #Drop Zeus
        keyboard.press("3")
        keyboard.release("3")
        time.sleep(0.1) #wait because if there is no time.sleep csgo wont press 3 again
        keyboard.press("3")
        keyboard.release("3")
        time.sleep(0.1) #wait because if there is no time.sleep csgo wont press g
        keyboard.press("g")
        keyboard.release("g")

        for char in str(dictionary[weapon]): #Find in dict dictionary the way to buy a gun and go for each letter of it
            #Press every letter and number in variable AWP
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.1) #wait because if there is no time.sleep csgo wont press next button

    else: #if weapon is not "DROP" and is not in dictionary
        pass

finally:
    if weapon=="DROP":
        pass
    elif weapon in dictionary:
        #Drop the weapon I have bought
        keyboard.press("g")
        keyboard.release("g")
    else:
        pass