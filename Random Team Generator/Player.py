# Define player object
class Player:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.hasNumber = False

    # Method for setting users phonenumbers
    def setPhonenumber(self, phoneNumber):
        self.phoneNumber = phoneNumber
        self.hasNumber = True

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

# Array of all houses which contain people in each house
houses = [LF12B, LF13C, LF12A, WARD1308]
houseNames = ['Lower Fulton 12B','Lower Fulton 13C', 'Lower Fulton 12A', 'Ward 1308']
# Empty people array to be appended to
people = []
index = -1;

# Adds each person for each house to the list of people
for i in houses:
    index += 1
    for j in range(len(i)):
        people.append(Player(i[j], houseNames[index]))
        # people.append(i[j])

for i in people:
    print(i.name + ' Representing ' + i.house)
