class Ball(object):
    def __init__(self):
        self.Len = 10
        self.xPos = 400 - self.Len / 2
        self.yPos = 400 - self.Len / 2
        self.xVel = 2
        self.yVel = 2
    
    def drawBall(self):
        rect(self.xPos, self.yPos, 10, 10)
    
    def resetPosition(self):
        self.xPos = 400 - self.Len / 2
        self.yPos = 400 - self.Len / 2


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

class Bot(Paddle):
    def movePaddle(self, ballx):
        if (ballx > self.xPos + self.xLen):
            if (self.xPos + self.xLen <= width):
                self.xPos += self.speed
        else:
            if (self.xPos >= 0):
                self.xPos -= self.speed
            

ball_ = Ball()
player_ = Player(400, 50)
opponent_ = Bot(400, 750)

def drawObjects():
    fill(200)
    rect(0, 0, width, height)
    fill(0)
    ball_.drawBall()
    player_.drawPaddle()
    opponent_.drawPaddle()
    
def moveBall():
    ball_.xPos -= ball_.xVel
    ball_.yPos -= ball_.yVel
    
def detectWallCollisions():
    if (ball_.xPos < 0):
        ball_.xVel *= -1
    elif (ball_.xPos + ball_.Len > width):
        ball_.xVel *= -1
    
    if (ball_.yPos < 0):
        ball_.yVel *= -1
    elif (ball_.yPos + ball_.Len > height):
        ball_.yVel *= -1

def setup():
    size(800, 800)
    noStroke()

def draw():
    drawObjects()
    player_.movePaddle()
    moveBall()
    detectWallCollisions()