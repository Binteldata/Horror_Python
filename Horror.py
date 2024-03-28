from stringcolor import cs
import time

# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def printa(string, color="yellow"):
    print(cs(string,color))


intro = """
The air hung heavy with the stench of damp earth and decay. A throbbing headache pulsed behind your eyes as you struggled to open them. Disoriented, you found yourself sprawled on a cold, hard surface. Panic surged through you as you realized you are trapped in a basement. Memories flickered back - a deserted gas station late at night, a flickering neon sign, a shadowed figure approaching... then darkness. You were trapped, alone, and at the mercy of something unseen. But a faint glimmer of hope flickered in the distance. A single flickering candle cast an eerie glow on a dusty wooden chest a few feet away. As you strained to hear, a raspy voice echoed from somewhere in the inky blackness. "Welcome, little traveler. Your escape awaits, but there's a price. Make your choice..." 
"""
intro_decisions = "(Left: Open the chest / Right: Yell for help / Stay Silent)"




######## PROGRAM START #########
printa(intro)
time.sleep(3)
printc(intro_decisions, "cyan")
time.sleep(0.5)
decision = input("CHOOSE: ") 
if any(word in decision.lower() for word in ["left", "left:", "open", "chest",]):
    printc("The voice chuckles, a cold, slithering sound." "Curious... very well." "what do you do?","green")
    printc("You gasp as you open the chest to find a book with a key hidden inside. Now if only you knew what the key is for...", "green")
    time.sleep(1)

elif any(word in decision.lower() for word in ["yell", "help", "for"]):
    printc("Silence. The shadows seem to writhe in response, snickering and laughing at your demise.","green")
    time.sleep(3)
  
elif any(word in decision.lower() for word in ["stay", "silent"]):
    printc("Your silence makes the evil spirits ANGRY! Poisonous gas seeps into the room and fills yours lungs, bringing you to a slow, painful and agonizing DEATH... GAME OVER!!!","red")
    time.sleep(1)

else:
    printc("INVALID INPUT.","red")