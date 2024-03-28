from stringcolor import cs 
import time
import pyjokes

def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def printa(string, color="red"):
    print(cs(string,color))

def printx(string, color="green"):
    print(cs(string,color))




intro = """
The air hung heavy with the stench of damp earth and decay. A throbbing headache pulsed behind your eyes as you struggled to open them. Disoriented, you found yourself sprawled on a cold, hard surface. Panic surged through you as you realized you were bound at the wrists and ankles, the rough rope biting into your skin. Memories flickered back - a deserted gas station late at night, a flickering neon sign, a shadowed figure approaching... then darkness. You were trapped, alone, and at the mercy of something unseen. But a faint glimmer of hope flickered in the distance. A single flickering candle cast an eerie glow on a dusty wooden chest a few feet away. As you strained to hear, a raspy voice echoed from somewhere in the inky blackness.
"Welcome, little traveler. Your escape awaits, but there's a price. Make your choice..." 
"""
intro_decisions = "(Open the chest/Yell for help/Stay Silent)"


printx(intro)
time.sleep(2)
name = input ("what should I call you?")
printc(f"nice to see you,{name}.", "lightgreen")
time.sleep(2)
printc(f"what are you going to do,{name} ?", "darkgreen")
time.sleep(1)
print(intro_decisions)
decision = input("choose:")


if "open" in decision.lower():
    printc("The voice chuckles, a cold, slithering sound." "Curious... very well.") 
    print("what do you do?")
    printa("Take out your phone and turn on the flashlight OR Run towards the exit")

elif "yell" in decision:
    print("Silence. The shadows seem to writhe in response, snickering and laughing at your demise.")

elif "stay" in decision:
    printc("Your silence makes the evil spirits ANGRY! Poisonous gas seeps into the room and fills yours lungs, bringing you to a slow, painful and agonizing DEATH... GAME OVER!!!", "darkred")
    time.sleep(3)
    printc("see ya soon!!!", "skyblue")
    printa("but you wanna to hear a Joke to forget that failue?")
    answer = "(yes/no)"
    if "y" in answer.lower() :
        joke = pyjokes.get_joke()
        printc( joke,"cyan")
    else:
        printa("okay,ciao")

else:
    printc("wrong answer, eliminated!!", "red")
    time.sleep(2)
    printa("that was great to palying with you,hope see you soon again!!!", color= "yellow")
    time.sleep(2)
    printa("but here is a joke to make you laugh :D")
    time.sleep(3)
    joke = pyjokes.get_joke()
    time.sleep(3)
    printc(joke , "cyan")