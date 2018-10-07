from player import Player

print("Welcome to adventures of Bob.")
print("Would you like to play? (y/n)")
response = input()
again = "y"

while(again=="y"):
    while response !="y" and response !="n":
        print("I'm sorry, I didn't understand your response.")
        print("Would you like to play? (y/n)")
        response = input()
    if response == "y":
        bob = Player()
        while (bob.getStatus() == False):
            print("Do you want to win?")
            response = input()
            if response == "y":
                bob.win()
                print("Great! You won!")
            else:
                print("Suit yourself.")
        print("Do you want to play again?")
        again = input()
    else:
        print("Okay, have a nice day!")
        again = "n"
print("Hope you had fun!")

