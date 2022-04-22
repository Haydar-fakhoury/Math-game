import random
import math

scores = 0
def level1():
    print("Welcome to level 1. In this level you're going to be adding and substracting numbers.\nIf you get 3 right you move on to the next level.")
    score = 0

    while score != 3:
        firstnumber = random.randint(1, 10)
        secondnumber = random.randint(1, 10)
        functlist = ["-", "+"]
        function = random.choice(functlist)
        if firstnumber > secondnumber:
            print(f"What is {firstnumber} {function} {secondnumber} ")
        else:
            print(f"What is {secondnumber} {function} {firstnumber} ")
        Answer = int(input(""))
        Aanswer = 0
        if function == "-":
            if firstnumber > secondnumber:
                Aanswer = firstnumber - secondnumber
            elif secondnumber > firstnumber:
                Aanswer = secondnumber - firstnumber
        else:
            if firstnumber > secondnumber:
                Aanswer = firstnumber + secondnumber
            elif secondnumber > firstnumber:
                Aanswer = secondnumber + firstnumber
        if abs(Answer) == Aanswer:
            score = score+1
            print(f"You got it right! and your score is {score}!")
        else:
            print("You got it wrong...")

level1()


def level2():
    print("Welcome to level 2. In this level you're going to be adding and substracting numbers.\nIf you get 3 right you win!")
    score = 0
    while score != 3:
        firstnumber = random.randint(1, 10)
        secondnumber = random.randint(1, 10)
        functlist = ["x", "/"]
        function = random.choice(functlist)
        if firstnumber > secondnumber:
            print(f"What is {firstnumber} {function} {secondnumber} ")
        else:
            print(f"What is {secondnumber} {function} {firstnumber} ")
        Answer = float(input(""))
        Aanswer = 0
        if function == "x":
            if firstnumber > secondnumber:
                Aanswer = firstnumber * secondnumber
            elif secondnumber > firstnumber:
                Aanswer = secondnumber * firstnumber
        else:
            if firstnumber > secondnumber:
                Aanswer = firstnumber / secondnumber
                print(Aanswer)
            elif secondnumber > firstnumber:
                Aanswer = secondnumber / firstnumber
                print(Aanswer)
        if abs(Answer) == Aanswer:
            score = score+1
            print(f"You got it right! and your score is {score}!")
        else:
            print("You got it wrong...")
level2()

print("Congrats you finished the game!")