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
    print("Start from the point ("+str(bob.getX())+","+str(bob.getY())+") let's move.")
    bob.moveR()
    print("Move right.")
    bob.moveU()
    print("Move up.")
    bob.moveR()
    print("Move right.")
    bob.moveL()
    print("Move left.")
    bob.moveD()
    print("Move down.")
    bob.moveD()
    print("Move down.")
    print("End up at ("+str(bob.getX())+","+str(bob.getY())+").")

testPlayer(0,0)
