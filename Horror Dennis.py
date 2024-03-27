from stringcolor import cs
import time

# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def printa(string, color="cyan"):
    # string first, then color optional - default cyan
    print(cs(string,color))

def printb(string, color="lightgreen"):
    # string first, then color optional - default cyan
    print(cs(string,color))


def printd(string, color="yellow"):
    # string first, then color optional - default cyan
    print(cs(string,color))


intro = """
The air hung heavy with the stench of damp earth and decay. A throbbing headache pulsed behind your eyes as you struggled to open them. Disoriented, you found yourself sprawled on a cold, hard surface. Panic surged through you as you realized you were bound at the wrists and ankles, the rough rope biting into your skin. Memories flickered back - a deserted gas station late at night, a flickering neon sign, a shadowed figure approaching... then darkness. You were trapped, alone, and at the mercy of something unseen. But a faint glimmer of hope flickered in the distance. A single flickering candle cast an eerie glow on a dusty wooden chest a few feet away. As you strained to hear, a raspy voice echoed from somewhere in the inky blackness.
"Welcome, little traveler. Your escape awaits, but there's a price. Make your choice..." 
"""
intro_decisions = "(Left: Open the chest/ Right: Yell for help/ Stay Silent)"



######## PROGRAM START #########
printb(intro)
time.sleep(5)
name = input("What's your name? ")
printc(f"Welcome, {name}!", "yellow")
printd(intro_decisions)
time.sleep(0.5)
decision = input("CHOOSE: ")
if any(word in decision.lower() for word in ["left", "left:", "open", "the", "chest"]):
    printb("The voice chuckles, a cold, slithering sound.")
    time.sleep(1)
    printb("'Curious... very well.'", "orange")
    time.sleep(3)
    printb("You crawl towards the chest, your heart pounding in your chest. The lid creaks open, revealing a glinting silver key resting on a bed of velvet. As you reach out to grasp it, a sudden gust of wind extinguishes the candle, plunging you into darkness.")
    printc("WHAT DO YOU DO?", "blue")
    printd("Take out your phone and turn on the flashlight/ Run towards the exit")
    decision = input("CHOOSE: ")
    if any(word in decision.lower() for word in ["take", "out", "phone", "your", "turn", "on", "flashlight"]):
        printb("You fumble for your phone, your hands shaking. The screen illuminates the room in a harsh, white light. Shadows dance on the walls, twisting and contorting into grotesque shapes. You see a door at the far end of the room, its outline barely visible in the darkness.")
        time.sleep(3)
        printa("BOO!")
        time.sleep(3)
        printb("You get startled, in front of you stands a tall figure, ugly both in voice and appearance. You drop your phone and it shatters on the ground. The figure laughs, a cruel, mocking sound.")	
        time.sleep(3)
        printa(f"I'm Herr Tauber from the Finanzamt, and our records show that you haven't paid your taxes in years Mr. {name}. You're in big trouble, my friend!")
        time.sleep(3)
        printb("You feel a cold hand close around your throat, squeezing the air from your lungs. Panic claws at your chest as you struggle to break free. But it's too late. Darkness swallows you whole.")
        time.sleep(1)
        printc("YOU DIED! TAX EVASION IS NO JOKE!", "red")
    elif any(word in decision.lower() for word in ["run", "towards", "the", "exit"]):
        printb("You sprint towards the exit, your heart pounding in your chest. The darkness seems to press in on you, suffocating and thick. You can hear the sound of footsteps behind you, growing louder and closer with each passing second.")
        time.sleep(3)
        printb("You try to get up, but it's too late, a litter of golden retriever puppies runs towards you and overpower you with their cuteness. You're too mesmerized to move, as more and more pile up on your face you slowly sufficate")
        time.sleep(1)
        printc("YOU DIED! PUPPY OVERLOAD!", "red")
        # starting a fight in the jc
    else:
        printc("INVALID INPUT", "red")
elif decision.lower() == "call agent":
    printc("You called your agent and waited for him to answer - but nothing.", "green")
    time.sleep(1)
    printc("After a long waiting, you stopped trying and accept you can't reach that guy...", "green")
    time.sleep(3)
    printc("WHAT DO YOU DO?", "cyan")
    # decisions (
elif "wait" in decision.lower():
    printc("After a long and polite waiting time, you feel how the injustice of this whole situation begins to corrupt you.", "green")
    time.sleep(1)
    printc("Every damn time you're here they let you wait, and wait, and wait for what? For like enough cash to not die in the street? Maybe? You've had enough.", "orange")
    time.sleep(1)
    printc("Your soul fills with dark anger and violence - fueled by this, you storm out of that damn room and search for the first person to unload your anger upon. Ready to say: 'This is unacceptable'", "red")
    time.sleep(3)
    printc("WHAT DO YOU DO?", "cyan")
    # decisions (
else:
    printc("INVALID INPUT.", "red")