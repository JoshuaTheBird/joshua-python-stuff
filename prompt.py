import time
import os
print ("Welcome to Joshua's Python Shell! Type help for commands. This software is currently in ALPHA STAGE and you should not expect much from it.")
time.sleep(2)
print ("Main prompt, GO!")
mainloopactive = 1
while mainloopactive == 1:

    command = input("READY. ->")
    #print ("Did the command you type go like this?:", command)
    #time.sleep(10)
    if command == "calc":

        print("Addition Calculator, GO!")
        num1 = int(input("Put in a number. ->"))
        num2 = int(input("Put in a number to add to it. ->"))
        sum = num1 + num2
        print(num1, "plus", num2, "adds up to", sum)
    if command == "stringcombine":
        print("String combiner toy, GO!")
        strtoy1 = input("Put in a string. ->")
        strtoy2 = input("Put in another string. ->")
        print(strtoy1, strtoy2)
    if command == "grantwish":
        print("WELCOME TO THE WISH GRANTING COMMAND MONITOR CODED BY THE ANCIENTS OF..... UH..... ok it was actually")
        print("just made by Joshua lol look how professional my software is!")
        wish = input("Wish to grant? (such as flying, invincibility) ->")
        if wish == "flying":
            print("*you suddenly levitate slowly off of your chair and into the sky, you fly directly into the sun*")
            time.sleep(5)
            print("...")
            time.sleep(2)
            print("since you're dead, you can't use my program anymore, so I guess I'll just boot you out instead of letting you continue")
            time.sleep(10)
            break
        if wish == "invincibility":
            print("What the hell? You are wishing to be invincible? That's like.... terrible! You'll be unkillable, you'll live on forever, that will suck for you when you grow old and in pain.")
            yesnowishinv = input("Do you really wanna do this? [Y/N] ->")
            if yesnowishinv == "y":
                print("No! you know what? that's it, you don't get to be here anymore, get out!")
                time.sleep(10)
                break
            if yesnowishinv == "n":
                print("Good choice, you can go back to the shell now.")
    if command == "quit":
        break
    if command == "help":
        print("This is a toy program written by none other than Joshua Vanderbilt")
        print("The commands you can run in here (that I bothered to document) are:")
        print("calc - Adds two numbers")
        print("stringcombine - little toy string combiner thing")
        print("grantwish - grants wishes (unfinished)")
        print("quit - breaks the main loop, causing the program to finish with exit code 0")
        print("print - allows you to print anything (experimental)")
        print("asciibirdon - prints an ascii picture of birdon with some simulated lag for fun")
        print("clearscreen - clears the screen")
        print("dir - lists files in the current directory")
        print("exec - run an OS command")
    if command == "print":
        independentstring = input("What do you want to print? ->")
        print (independentstring)
    if command == "asciibirdon":
        print("                                                                                ")
        time.sleep(0.1)
        print("                                                .(@@@@@@@@&/                    ")
        time.sleep(0.1)
        print("                                           .(@@@@%/(#%&@#,                      ")
        time.sleep(0.1)
        print("                     *%@@@@@@@@@@@@@#,   *%@%/*,,/###%&@@@@@@@@@(.              ")
        time.sleep(0.1)
        print("                *%@@@&%##(((((((#%%%&@@@@&%#/,*(###((/*,..,*/((%&@@@@(.         ")
        time.sleep(0.1)
        print("             .(@&%##(((((((((#%(*,.    *((//*,*(#(/*,...,*////////((#&@%*       ")
        time.sleep(0.1)
        print("           *%@%(/////////(###/,.         ./((////*,..,*////(######((/(#%&@(.    ")
        time.sleep(0.1)
        print("        .(@&#/, .*////((#%%%#/,.         ./(##((/*,..........,*/(#%@@@@@@@@@%*  ")
        time.sleep(0.1)
        print("      *%@&%#((///((#%%%#/,/#%#(/**(%%%%%%%%%%%#(/*,,*////////*,...*(#&@%*       ")
        time.sleep(0.1)
        print("      *%@&%#((#%%%#/,,,,/(##%%%%%%#(/*,.  .,/(###(/(#####%%%%%##(/*,,/#%&@(.    ")
        time.sleep(0.1)
        print("      *%@&%%%#/,,,,/(##%%%%%%%%##/, ,/##%##(*,*/##%%##%%(*,/(##%##((///#&@(.    ")
        time.sleep(0.1)
        print("   .(@&%#/,,,*/(##%%%#(((((#%&@%/,/(*.   ,(%%%####%%#%&@#, .,*(%#####(/#&@(.    ")
        time.sleep(0.1)
        print("   .(@&%%#(##%%%#((//////((#%&@#, *(##%&@@@@&%###&@@@@@@@@@@@@@@&%%@@&%%&@(.    ")
        time.sleep(0.1)
        print("      *%@&%#((((//////(#%@@@@@@%/,,,. .*#(**(####&@&#(///((%@&#(##%@@@@@@@(.    ")
        time.sleep(0.1)
        print("   .(@&#((((((//////(%&@&%%%%%%##/, ,(#/,*/(*,*/#&@%/.   .,*/#&@&%%@@@@@@@(.    ")
        time.sleep(0.1)
        print(" *&@%((((((//////(#%@@&%#(((((((###(/*,.    *(####(/,.     ..,/(%@@@@@@@@@@@%*  ")
        time.sleep(0.1)
        print(" *&@%((((///////(#%&@&#(////////((#%&@@@@@@@&%#((/////*,.....,*(%@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@%(/////////(%&@%(/////////////////////((#%#((//*,.....,*///(%@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print("   .(@&#((((#%&@&#(//////////////////////////((#%%%&@@%((/////((%@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@@@@@@@@@@@%((((///((//////(//////////////((###((/(%@@@@%(#&@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@%####&@&#(#%#(////((/////#%#(/////////((((##%%%&@@@@@&%&@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@@@@@@%#%@@#/////(//////((#%#(((((((((((((((((#%&@@&%%%%&@&%#&@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@@@&##&@&#((////#%#(///(#%%%#((((((((((((((##%&@@@@@@@@@&#(**#@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@@@@@@%#/*,,,(&@%#(///(##%&@@&%#((((((##%&@@@@&%#(((((#%&@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@@@@@&(,,,*/#%@&(*,,*/#%@@%(#&@@@@@@@@@@@&%#(((((///((((%@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@@@@@&(,/(#&@@@&(*,,*/#%@@#//((%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@@@@@@@@@@@@@@@&(*/(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(0.1)
        print(" *&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    if command == "clearscreen":
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    if command == "dir":
        if os.name == 'nt':
            os.system('dir')
        else:
            os.system('ls')
    if command =="exec":
        oscmd = input("Execute OS Command. ->")
        os.system(oscmd)
