import random

def main():
    #Participants
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

    houses = [LF12B, LF13C, LF12A, WARD1308]
    people = []
    #Adds each person for each house to the list of people
    for i in houses:
        for j in range(len(i)):
            people.append(i[j])

    #Each Team that a person can be a part of
    teamOne = []
    teamTwo = []

    #Total Length
    totalLen = len(people)
    #Total Number of People Remaining
    totalRangeRemaining = totalLen
    #Starting teamChoice
    teamChoice = 0

    #Loop through the Range of People
    for i in range(totalLen):
        #Get Random Person from List
        choice = random.choice(range(totalRangeRemaining))

        #Based on teamChoice the next person in the loop
        #will be added to that team and then the teamChoice is flipped
        if teamChoice == 0:
            teamOne.append(people[choice])
            teamChoice = 1
        else:
            teamTwo.append(people[choice])
            teamChoice = 0

        totalRangeRemaining -= 1


        #First and Last Pick of the Drafts
        if i == 0:
            print('First Pick: ' + people[choice])
        elif i == totalLen - 1:
            print('Last Pick: ' + people[0])
        #Remove current choice of person from list of peeople
        people.remove(people[choice])


    printTeam(teamOne,teamTwo)


def printTeam(teamOne,teamTwo):
    print('+======================================================================+')
    print('Team 1:')
    print ', '.join(map(str, teamOne))
    print('-----------------------------------------------------------------------')
    print('Team 2:')
    print ', '.join(map(str, teamTwo))
    print('+======================================================================+')


main()
