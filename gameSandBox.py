from player import Player

print("Welcome to adventures of Bob.")
print("Would you like to play? (y/n)")
response = input()
again = "y"

while(again=="y"): 
    while response !="y" and response !="n": # Try to get a valid answer
        print("I'm sorry, I didn't understand your response.")
        print("Would you like to play? (y/n)")
        response = input()
    if response == "y": # Game start
        bob = Player()
        while (bob.getStatus() == False): # Game start
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
        again = "n"
    print("Okay, have a nice day!")
if response == "y": # Message for someone who played the game at least once.
    print("Hope you had fun!")

