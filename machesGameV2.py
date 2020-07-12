# this is my first program, I am making it public for those who want
# to improve it, or just for those who want to play.

# matchesGame v2.1 run on Python 3.7(jeu des allumettes)
import sys
import time
import random

# nm is number of matches
nm = 13
# t is turn
t = 0
choiceCp = 0


def choice():
    choice = input


def choiceGamer():
    global choiceCp
    global nm
    global t
    print("there are ", nm, " matches")
    choiceG = int(input("How many matches to remove 1,2 or 3?"))
    if choiceG > 3 or choiceG < 1:
        print("Error, entre a number enter 1 and 3.")
        return choiceGamer()
    else:
        nm -= choiceG
        t = t + 1


def menu():
    print("   *********************************")
    print("      Welcome on the matches game.")
    print("   *********************************")
    time.sleep(0.65)
    choice = input("""
              A: Level easy
              B: level hard 
              C: level very hard
              E: exit  
              Please enter your choice:

    """)

    if choice == "A" or choice == "a":
        easy()
    elif choice == "B" or choice == "b":
        hard()
    elif choice == "C" or choice == "c":
        veryHard()
    elif choice == "E" or choice == "e":
        exit()
    else:
        print("Sorry,tape A,B,C or E")
        return menu()

def exit():
    print("Program by Vincent Delessard")
    time.sleep(1.75)
    sys.exit()

def easy():
    global choiceCp
    global nm
    global t
    nm = 13
    t = 0

    print("there are 13 matches,you can remove 1,2,or 3.The player who takes the last match has lost.")


    while nm > 1:

        if t % 2 == 0:
            print(" |  " * nm)
            print(" |  " * nm)
            choiceGamer()
        else:
            choiceCp = random.randint(1, 3)
            print("The computer remove", choiceCp, "matche(s)")
            nm = nm - choiceCp
            t = t + 1

    if nm == 1 & t % 2 != 0:
        print(" |  " * nm)
        print(" |  " * nm)
        print("The last one is for the computer,you win")
        time.sleep(1.25)
        menu()
    elif nm == 0 & t % 2 == 0:
        print("The last one is for you,computer win.")
        time.sleep(1.25)
        menu()
    else:
        print(" |  " * nm)
        print(" |  " * nm)
        print("The last one is for you,computer win.")
        time.sleep(1.25)
        menu()


def hard():
    global nm
    global t
    nm = 13
    print("there are 13 matches,you can remove 1,2,or 3.The player who takes the last match has lost.")

    t = random.randint(0, 1)
    if t == 1:
        print(" |  " * nm)
        print(" |  " * nm)
        print("Chance has decided that the computer start. ")



    while nm > 1:

        if t % 2 == 0:
            print(" |  " * nm)
            print(" |  " * nm)
            choiceGamer()

        elif t % 2 != 0:

            if (nm - 4) % 4 == 0:
                print("The computer remove 3 matches")
                nm = nm - 3
                t = t + 1
            elif (nm - 3) % 4 == 0:
                print("The computer remove 2 matches")
                nm = nm - 2
                t = t + 1
            elif (nm - 2) % 4 == 0:
                print("The computer remove 1 matche")
                nm = nm - 1
                t = t + 1
            elif (nm - 1) % 4 == 0:
                print("The computer remove 1 matche")
                nm = nm - 1
                t = t + 1

    if nm == 1 & t % 2 != 0:
        print(" |  " * nm)
        print(" |  " * nm)
        print("The last one is for the computer,you win")
        time.sleep(1.25)
        menu()
    elif nm == 0 & t % 2 == 0:
        print("The last one is for you,computer win.")
        time.sleep(1.25)
        menu()
    else:
        print(" |  " * nm)
        print(" |  " * nm)
        print("The last one is for you,computer win.")
        time.sleep(1.25)
        menu()


def veryHard():
    global nm
    global t
    nm = 13
    t = 0



    print("there are ", nm, " matches,you can remove 1,2,or 3.The player who takes the last match has lost.")
    while nm > 1:

        if t % 2 == 0:
            print(" |  " * nm)
            print(" |  " * nm)
            choiceGamer()

        else:
            if nm == 12:
                print("The computer remove 3 matches")
                nm = nm - 3
                t = t + 1
            elif nm == 11:
                print("The computer remove 2 matches")
                nm = nm - 2
                t = t + 1
            elif nm == 10:
                print("The computer remove 1 matche")
                nm = nm - 1
                t = t + 1
            elif nm == 9:
                print("The computer remove 1 matche")
                nm = nm - 1
                t = t + 1
            elif nm == 8:
                print("The computer remove 3 matches")
                nm = nm - 3
                t = t + 1
            elif nm == 7:
                print("The computer remove 2 matches")
                nm = nm - 2
                t = t + 1
            elif nm == 6:
                print("The computer remove 1 matche")
                nm = nm - 1
                t = t + 1
            elif nm == 5:
                print("The computer remove 1 matche")
                nm = nm - 1
                t = t + 1
            elif nm == 4:
                print("The computer remove 3 matches")
                nm = nm - 3
                t = t + 1
            elif nm == 3:
                print("The computer remove 2 matches")
                nm = nm - 2
                t = t + 1
            elif nm == 2:
                print("The computer remove 1 matche")
                nm = nm - 1
                t = t + 1
    if nm == 1 & t % 2 != 0:
        print(" |  " * nm)
        print(" |  " * nm)
        print("The last one is for the computer,you win")
        time.sleep(1.25)
        menu()
    elif nm == 0 & t % 2 == 0:
        print("The last one is for you,computer win.")
        time.sleep(1.25)
        menu()
    else:
        print(" |  " * nm)
        print(" |  " * nm)
        print("The last one is for you,computer win.")
        time.sleep(1.25)
        menu()






menu()




