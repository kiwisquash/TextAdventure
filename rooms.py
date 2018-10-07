import random

class Room:
    def __init__(self,message):
        self.message = message
    def getMessage(self):
        return self.message
    def setMessage(self,message):
        self.message = message
    def printMessage(self):
        print(self.message)
    def affectPlayer(self,player):
        pass

class Exit(Room):
    def affectPlayer(self,player):
        player.win()

map = []
exitX = random.randint(0,2)
exitY = random.randint(0,2)
for i in range(3):
    map.append([])
    for j in range(3):
        if j == exitY and i == exitX:
            map[i].append(Exit("This is the exit!"))
        else:
            map[i].append(Room("This is a room. Nothing special here))
