class Paddle(object):
    def __init__(self, x, y):
        self.xLen = 150
        self.yLen = 10
        self.xPos = x - self.xLen / 2
        self.yPos = y
        self.speed = 4
    
    def drawPaddle(self):
        rect(self.xPos, self.yPos, self.xLen, self.yLen)

class Player(Paddle):
    def movePaddle(self):
        if (keyPressed and keyCode == RIGHT):
            if (self.xPos + self.xLen <= width):
                self.xPos += self.speed
        elif (keyPressed and keyCode == LEFT):
            if (self.xPos >= 0):
                self.xPos -= self.speed

class SimpleBot(Paddle):

    def movePaddle(self, ballx):
        if (ballx > self.xPos + self.xLen / 2):
            if (self.xPos + self.xLen <= width):
                self.xPos += self.speed
        else:
            if (self.xPos >= 0):
                self.xPos -= self.speed