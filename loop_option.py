import os

dead = False

while dead == False:
    print("Options: (do/wait/die)")
    decision = input("CHOOSE: ")
    if decision.lower() == "do":
        print("YOU DID")
        # continues
        print("You did it and now next stage")
        break
    elif decision.lower()== "wait":
        print("YOU WAITED")
        # tries again
    elif decision.lower() == "die":
        print("you deed")
        # end
        dead = True

if dead == False:
    # continue
else:
    os. _exit() # ENDS PROGRAM