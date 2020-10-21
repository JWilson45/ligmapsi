# Program to determine and randomize teams for bitch chalice

import random

def main():

    people = []

    # 12B
    LF12B = [
    "Phill",
    "Dave",
    "Jake",
    "Pat",
    "Gabe",
    "Evan"
    ]

    # 1308
    WARD1308 = [
    "Jason",
    "Zack",
    "Jack",
    "JC"
    ]

    # 13C
    LF13C = [
    "Lynnanne",
    "Tori",
    "Alyssa",
    "Ollie"
    ]

    # 12A
    LF12A = [
    "Ashley",
    "Carly",
    "Lauren",
    "Alexa",
    "Gabby",
    "Lexi",
    "Steph"
    ]

    team1 = []
    team2 = []

    # List containing all of the houses that are going
    houses = [LF12B, LF13C, LF12A, WARD1308]
    # print(houses)

    for i in houses:
        for j in range(len(i)):
            people.append(i[j])
    print(people)

    total = len(people)
    total1 = str(total)
    print("Total number of people going: " + total1)
    print("")

    # One by one select people at random from total list of people and put them on either team 1 or team 2
    flop = 0

    for i in range(total):
        index = random.randrange(0, total)
        if flop == 0:
            team1.append(people[index])
            total -= 1
            # print("Team 1: ")
            # print(team1)
            flop = 1
        else:
            team2.append(people[index])
            total -= 1
            # print("Team2: ")
            # print(team2)
            flop = 0
        del people[index]
    print("Team 1: ")
    print(team1)
    print("Team 2: ")
    print(team2)

    # Implement everything in different functions and also implement when space bar

main()
