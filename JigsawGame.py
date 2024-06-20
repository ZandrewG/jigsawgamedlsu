#####JIGSAWGAMEEMPTECH2PROJECT#####
# Nebrida, Ricalyn (50%)
# Garais, Zandrew (50%)
# Sources:
# Functions: https://www.w3schools.com/python/python_functions.asp
# Functions and Lesson Refresh: https://www.youtube.com/watch?v=rfscVS0vtbw
# Other sources are from lessons in class.


def tryagain_function(try_again):
    global q  # variable "q" is a global function meaning that it can be used everywhere in the code

    if try_again == "yes":
        q = 1
        return "The game is restarting..."

    elif try_again == "no":
        q -= 1

        return "THANK YOU FOR PLAYING"




# Start of the game
gametitle = "Jigsaw Scientist: Escape Game"
print(gametitle)

# restartprototype#1

q = 1
while q != 0:

    # Willyousleepagain

    print("You wake up....")
    name = str(input("What's your name? "))

    againsleep = 1

    while againsleep != 0:

        sleepagain = str(input("Will you sleep again? yes or no. "))

        if sleepagain == "yes":
            againsleep == 1
            print("USELESS!")
            try_again = str(input("Try again? "))
            if try_again == "yes":

                print("The game is restarting...")
                break
            elif try_again == "no":

                print("THANK YOU FOR PLAYING")
                break


        elif sleepagain == "no":
            againsleep -= 1

            # Getkeydecision Gas Room
            print("[VHS TAPE PLAYING] with useless dialogue, you should get key boyfriend")

            getkey = str(input("Will you get keys from BF? "))

            if getkey == "no" and getkey != "yes":
                print("YOU DIED")
                try_again = str(input("Try again? "))
                print(tryagain_function(try_again))
                # I called the function here
                # I thought of using a function to save space and to be efficient


            elif getkey == "yes" and getkey != "no":  # BEST OPTION

                # KILLMabelleDecisionEvent-GlassCoffin
                print(name, "and Mabelle kill each other please.")

                killmabelle = str(input("Will you kill Mabelle? "))

                if killmabelle == "yes" and killmabelle != "no":
                    print("YOU DIED")
                    try_again = str(input("Try again? "))
                    print(tryagain_function(try_again))

                elif killmabelle == "no" and killmabelle != "yes":

                    print("More dialogue......")
                    print("MABELLE DIED")

                    # EventVariableGunDecisionEvent
                    print("You found Mabelle's gun")

                    getgunresponse = str(input("Will you get gun? yes or no. "))

                    get_gun = 0  # this signifies that you don't have a gun before decision

                    if getgunresponse == "yes" and getgunresponse != "no":
                        get_gun += 1
                    elif getgunresponse == "no" and getgunresponse != "yes":
                        get_gun == 0

                    print("More dialogue bullshit......")
                    print("You found a scientist uniform")

                    # EventVariableUniformDecisionEvent

                    getnerdclothesq = str(input("Will you get the scientist uniform? yes or no. "))

                    get_clothes = 0  # this signifies that you don't have a gun before decision

                    if getnerdclothesq == "yes" and getnerdclothesq != "no":
                        get_clothes += 1
                    elif getnerdclothesq == "no" and getnerdclothesq != "yes":
                        get_clothes == 0

                    # EventVariableScalpelDecisionEvent

                    getscalpelq = str(input("Will you get the scalpel? yes or no. "))

                    getscalpel = 0  # this signifies that you don't have a scalpel/knife before decision

                    if getscalpelq == "yes" and getscalpelq != "no":
                        getscalpel += 1
                    elif getscalpelq == "no" and getscalpelq != "yes":
                        getscalpel == 0

                    print("""More dialogue bullshit......
                                                wandering around shit""")

                    # You met bernard
                    print("You met Bernard")

                    # decisioneventhelpbernard
                    manners = 0

                    helpman = str(input("Will u help? "))

                    if helpman == "yes" and helpman != "no":
                        manners += 1

                    elif helpman == "no" and helpman != "yes":

                        manners == 0

                        print("Bernard:Pleaseeeee : ( ")

                        helpman = str(input("Will u reconsider please? "))

                        if helpman == "yes" and helpman != "no":
                            manners += 1

                        elif helpman == "no" and helpman != "yes":

                            manners == 0

                    # after-helpbernard decision event

                    if manners == 1:
                        print("Bernard treats your wounds")
                        print("""Your pair found a Map.
Decide now to go to Gate A or B.""")

                        # GateDecisionEvent
                        gateA = 1
                        gateA = str(input("""Will you go to
                                        A. Gate A
                                        or
                                        B. Gate B? """))
                        if gateA == "A" and "a" and gateA != "B" and "b":
                            print("You proceeded to Gate A")
                            print("You saw Jigsaw")

                            sparejigsaw = str(input("Will you spare Jigsaw?"))

                            if sparejigsaw == "yes" and sparejigsaw != "no":
                                print("He got arrested")
                                print("END")
                                tryagain_function(try_again)

                            elif sparejigsaw == "no" and sparejigsaw != "yes":
                                if get_gun == 1:
                                    print("You shoot Jigsaw")
                                    print("Jigsaw Dead")
                                    try_again = str(input("Try again? "))
                                    tryagain_function(try_again)

                                else:
                                    print("Punch Jigsaw")

                                    amountpunch = 0

                                    while amountpunch <= 25:

                                        punchaction = str(input("Will you punch Jigsaw?" "yes or no?"))

                                        if punchaction == "yes" and punchaction != "no":
                                            print("You punched Jigsaw")

                                            amountpunch += 1

                                        elif punchaction == "no" and punchaction != "yes":
                                            print("You stopped punching")

                                            break
                                    if amountpunch <= 15:
                                        print("Not enough, more!")
                                        print("YOU DIED")
                                        print("GAME OVER")
                                        try_again = str(input("Try again? "))
                                        tryagain_function(try_again)
                                    elif 15 < amountpunch < 25:
                                        print("Jigsaw Got arrested")
                                        print("GAME OVER")
                                        try_again = str(input("Try again? "))
                                        tryagain_function(try_again)
                                    elif amountpunch >= 25:
                                        print("Wow you killed him!")
                                        print("GAME OVER")
                                        try_again = str(input("Try again? "))
                                        tryagain_function(try_again)

                        elif gateA == "B" or "b" and gateA != "A" or "a":
                            print("You won.")
                            try_again = str(input("Try again? "))
                            tryagain_function(try_again)



                    elif manners == 0:
                        print("You explored the facility alone")
                        print("You saw a facility guard also trying to escape")
                        print("")

                        if get_clothes == 1 and get_clothes != 0:
                            changeoutfit = str(input("Will you change to your scientist uniform? "))

                            if changeoutfit == "Yes" or "yes" and changeoutfit != "No" or "no":
                                print("")
                                guardapproach = str(input("Will you approach the guard? "))

                                if guardapproach == "Yes" or "yes" and guardapproach != "No" or "no":

                                    if get_gun == 1 and get_gun != 0 or getscalpel == 1 and getscalpel != 0:
                                        print("Ask for help, gate a exit point; you see jigsaw.")
                                        print("Jigsaw told the guard to arrest you.")
                                        print("Resist. You kill Jigsaw and guard.")
                                        print("Exit in Gate A")
                                        print("You won.")
                                        try_again = str(input("Try again? "))
                                        tryagain_function(try_again)

                                    elif get_gun != 1 and get_gun == 0:
                                        print("Ask for help, gate a exit point; you see jigsaw.")
                                        print("Jigsaw told the guard to arrest you.")
                                        print("Resist. You tried stabbing guard.")
                                        print("Injected you a lethal substance.")
                                        print("You Died.")
                                        try_again = str(input("Try again? "))
                                        tryagain_function(try_again)

                                    elif get_gun != 1 and get_gun == 0 or getscalpel != 1 and getscalpel == 0:
                                        print("Ask for help, gate a exit point; you see jigsaw.")
                                        print("Jigsaw told the guard to arrest you.")
                                        print("Injected you a lethal substance.")
                                        print("You Died.")
                                        try_again = str(input("Try again? "))
                                        tryagain_function(try_again)

                                elif guardapproach != "Yes" or "yes" and guardapproach == "No" or "no":
                                    print("You unravel alone")
                                    print("Jigsaw caught your from behind")
                                    print("reveal weapon")

                                    if getscalpel == 1 and getscalpel != 0 or get_gun == 1 and get_gun != 0:
                                        useweapon = str(input("""
will you use the A.Knife or B.Gun? """))

                                        if useweapon == "A" or "a" and useweapon != "B" or "b":
                                            print("You stab Jigsaw.")
                                            print("You Win.")
                                            try_again = str(input("Try again? "))
                                            tryagain_function(try_again)

                                        elif useweapon != "A" or "a" and useweapon == "B" or "b":
                                            print("")
                                            print("You shot jigsaw")
                                            try_again = str(input("Try again? "))
                                            tryagain_function(try_again)

                                    elif getscalpel != 1 and getscalpel == 0 or get_gun != 1 and get_gun == 0:
                                        print("")
                                        print("You got injected.")
                                        print("You Died.")
                                        try_again = str(input("Try again? "))
                                        tryagain_function(try_again)

                        elif get_clothes != 1 and get_clothes == 0:
                            print("")
                            guardapproach = str(input("Will you approach the guard? "))

                            if guardapproach == "Yes" or "yes" and guardapproach != "No" or "no":

                                print("He points gun at you")
                                print("Tricks you.")
                                print("You Died.")
                                try_again = str(input("Try again? "))
                                tryagain_function(try_again)

                            elif guardapproach == "No" or "no" and guardapproach != "Yes" or "yes":
                                print("Turns to you")
                                print("Shoots you")
                                print("You Died.")
                                try_again = str(input("Try again? "))
                                tryagain_function(try_again)
                                break




