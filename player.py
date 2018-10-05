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
        self.x=-1
    def moveR(self):
        self.x=+1
    def moveU(self):
        self.y=+1
    def moveD(self):
        self.y=-1

def testPlayer(x,y):
    bob = Player(x,y)
    print("Start from the point ("+bob.getX()+","+bob.getY()+") let's move.")
    bob.moveR()
    bob.moveU()
    bob.moveR()
    bob.moveL()
    bob.moveD()
    bob.moveD()
    print("End up at ("+bob.getX()+","+bob.getY()+").")

testPlayer(0,0)
