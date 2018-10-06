class Player:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
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
        output = "("
        output += str(self.getX())
        output +=", "
        output += str(self.getY())
        output += ")"
        return output
    def printPos(self):
        output = "Your current position is "
        output += self.position()
        print(output)

def testPlayer(x,y):
    bob = Player(x,y)
    print("Start from the point ("+str(bob.getX())+","+str(bob.getY())+") let's move.")
    bob.moveR()
    bob.printPos()
    bob.moveU()
    print("Move up.")
    bob.printPos()
    bob.moveR()
    print("Move right.")
    bob.printPos()
    bob.moveL()
    print("Move left.")
    bob.printPos()
    bob.moveD()
    print("Move down.")
    bob.printPos()
    bob.moveD()
    print("Move down.")
    bob.printPos()
    print("End up at ("+str(bob.getX())+","+str(bob.getY())+").")

testPlayer(0,3)
