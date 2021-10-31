"""
Zahlenratespiel mit variablem Schwierigkeitsgrad
"""
import random

maxInt: int = 100
minInt: int = 1
maxTries: int = 0
difficulty: str = input("Schwierigkeitsgrade (einfach, normal, schwer): ")
hints: bool = False
baseGuess: int = 0
closestNumber: int = 0
global tipp
tipp: int = 0

userInput = 0
tries = 0

global toBeGuessed
toBeGuessed: int = random.randint(1, 100)


def hintshelper(param_hints):
    global closestNumber
    if param_hints:
        closestNumber = round(toBeGuessed / baseGuess) * baseGuess
        print("Die nächstgelegene Zahl ist {}".format(closestNumber))
        if tipp > closestNumber:
            print("Die eingegebene Zahl ist größer als die nächstgelegene Zahl")
        elif tipp < closestNumber:
            print("Die eingegebene Zahl ist kleiner als die nächstgelegene Zahl")
        if tipp == closestNumber :
            print("Die eingegebene Zahl ist gleich der nächstgelegenen Zahl")


if difficulty == "einfach":
    maxTries = 100
    baseGuess = 5
    hints = True
elif difficulty == "normal":
    maxTries = 25
    baseGuess = 10
    hints = True
elif difficulty == "schwer":
    maxTries = 10
else:
    print("undefinierter Schwierigkeitsgrad")
    exit()

while toBeGuessed != userInput:
    userInput = input("Bitte gebe die erratene Zahl ein: ")
    tipp = int(userInput)
    tries += 1
    # debugging only
    # print("Ratezahl (nur fürs Debugging):", toBeGuessed)
    hintshelper(hints)
    if difficulty == "schwer":
        if toBeGuessed < 50:
            print("Die gesuchte Zahl ist kleiner als 50")
        if toBeGuessed > 50:
            print("Die gesuchte Zahl ist größer als 50")
        if tipp < toBeGuessed:
            print("Die gesuchte Zahl ist größer als die eingegebene Zahl")
        if tipp > toBeGuessed:
            print("Die gesuchte Zahl ist kleiner als die eingegebene Zahl")
    if tipp == toBeGuessed:
        print("Gewonnen!")
        print("Du hast die Zahl {} erraten".format(toBeGuessed))
        print("Notwendige Versuche: {}".format(tries))
        print("Glückwunsch!")
        break
    elif tries > maxTries:
        print("Sorry, du hast die Zahl nicht erraten können")
        break
    else:
        print("Das schaffst du schon!")
print("Spiel beendet")
