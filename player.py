import random 
import time

class Player:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.victory = 0
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
        self.x = x
    def setY(self,y):
        self.y = y
    def moveL(self):
        self.x-=1
    def moveR(self):
        self.x+=1
    def moveU(self):
        self.y+=1
    def moveD(self):
        self.y-=1
    def position(self):
        return (self.getX(),self.getY())
    def printPos(self):
        output = "Your current position is "
        output += self.position()
        print(output)

def testPlayer(x,y,nSteps):
    bob = Player(x,y)
    print("Start from the point ("+str(bob.getX())+","+str(bob.getY())+") let's move.")
    for i in range(nSteps):
        time.sleep(1)
        randVal = random.randint(0,3)
        if randVal == 0:
            print("Move to the right.")
            bob.moveR()
            bob.printPos()
        if randVal == 1:
            print("Move to the left.")
            bob.moveL()
            bob.printPos()
        if randVal == 2:
            print("Move to the up.")
            bob.moveU()
            bob.printPos()
        if randVal == 3:
            print("Move to the down.")
            bob.moveD()
            bob.printPos()

testPlayer(0,0,10)
