class Ball(object):
    def __init__(self):
        self.Len = 10
        self.xPos = 400 - self.Len / 2
        self.yPos = 400 - self.Len / 2
        self.xVel = 5
        self.yVel = 3
    
    def drawBall(self):
        rect(self.xPos, self.yPos, 10, 10)
    
    def resetPosition(self):
        self.xPos = 400 - self.Len / 2
        self.yPos = 400 - self.Len / 2