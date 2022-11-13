import random
from pickle import TRUE


# builds a card
class Card:
    def __init__(self, suit, value):
        # suits
        # 0 = ♥
        # 1 = ♦
        # 2 = ♣
        # 3 = ♠
        self.suit = "♥♦♣♠"[suit]
        # if the value is certain values, then change to face cards
        match value:
            case 1:
                value = "A"
            case 11:
                value = "J"
            case 12:
                value = "Q"
            case 13:
                value = "K"
        # assign the value
        self.value = value

    # builds the display of the card, example:
    # ┌───────┐
    # | 6     |
    # |       |
    # |   ♦   |
    # |       |
    # |     6 |
    # └───────┘
    def display(self):
        print("┌───────┐")
        print(f"| {self.value:<2}    |")
        print("|       |")
        print(f"|   {self.suit}   |")
        print("|       |")
        print(f"|    {self.value:>2} |")
        print("└───────┘")


# calculate score by comparing guess with the card
class Scoring:
    def __init__(self):
        pass

    def calculate(self, guess, prevValue, currentValue):
        global score

        # convert display values of face cards for comparing
        match currentValue:
            case "A":
                currentValue = 1
            case "J":
                currentValue = 11
            case "Q":
                currentValue = 12
            case "K":
                currentValue = 13

        # convert display values of face cards for comparing
        match prevValue:
            case "A":
                prevValue = 1
            case "J":
                prevValue = 11
            case "Q":
                prevValue = 12
            case "K":
                prevValue = 13

        match guess:
            case "h":
                if currentValue > prevValue:
                    score = score + 100
                else:
                    score = score - 75
            case "l":
                if currentValue < prevValue:
                    score = score + 100
                else:
                    score = score - 75
            case "s":
                if currentValue == prevValue:
                    score = score + 100
                else:
                    score = score - 75
        return score


# initialize first card, can't be lowest or highest card
value = random.randint(2, 12)
suit = random.randint(0, 3)

# initialize score
score = 0

# initialize first card, can't be lowest or highest card
value = random.randint(2, 12)
suit = random.randint(0, 3)

# initialize keepGoing
keepGoing = 0

print("\n---- Welcome to HiLo! ----\n ")
print("The goal of the game is to receive a card and guess if the next")
print("card drawn is higher, lower, or the same as the current one.\n")
print("Your beginning score is 300 points, and it can be changed as follows:")
print(" ⌘ If you guess correctly, your score increases by 100.")
print(" ⌘ If you guess incorrectly, your score decreases by 75.\n")
print("Ready to begin? [Y/N]")
start = input(">>> ")

#set the score only if the user is ready to play
if start.lower() == "y":
    score = 300

# if score > 0, keep going, else game over
while score > 0:

    # display previous card
    print("\nCurrent card:")
    prev = Card(suit, value)
    prevValue = prev.value
    prev.display()

    # ask guess
    print("\nWill the next card be higher, lower, or the same? [H/L/S]")
    guess = input(">>> ")

    # current = random.randint(1, 13)
    value = random.randint(1, 13)
    suit = random.randint(0, 3)
    current = Card(suit, value)
    currentValue = current.value
    current.display()

    # compare card with guess and calculate score
    scoring = Scoring()
    score = scoring.calculate(guess, prevValue, currentValue)
    print(f"\nYour score is: {score}")

    if score <= 0:
        print(f"\nGame over! Your ending score is {score}")
        break
    else:
        # ask user to continue
        print("\nWould you like to continue? [Y/N]")
        choice = input(">>> ")
        if choice.lower() == "y":
            keepGoing = 1
        else:
            keepGoing = 0

    # new previous card
    prev = current

else:
    print(f"\nGame over! Your ending score is {score}")
