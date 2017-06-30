from Ball import Ball
from Paddle import Paddle, Player, SimpleBot

ball_ = Ball()
player_ = Player(400, 50)
opponent_ = SimpleBot(400, 750)
playerScore_ = 0
opponentScore_ = 0

def drawObjects():
    fill(200)
    rect(0, 0, width, height)
    fill(0)
    ball_.drawBall()
    player_.drawPaddle()
    opponent_.drawPaddle()
    text(playerScore_, 750, 300)
    text(opponentScore_, 750, 500)
    
    
def moveBall():
    ball_.xPos -= ball_.xVel
    ball_.yPos -= ball_.yVel
    
def detectWallCollisions():
    if (ball_.xPos < 0):
        ball_.xVel *= -1
    elif (ball_.xPos + ball_.Len > width):
        ball_.xVel *= -1
    
    if (ball_.yPos < 0):
        ball_.resetPosition()
        global opponentScore_
        opponentScore_ += 1
    elif (ball_.yPos + ball_.Len > height):
        ball_.resetPosition()
        global playerScore_
        playerScore_ += 1

def detectPlayerPaddleCollisions():
    if (ball_.xPos > player_.xPos and ball_.xPos < player_.xPos + player_.xLen):
        ball_.yVel *= -1

def detectBotPaddleCollisions():
    if (ball_.xPos > opponent_.xPos and ball_.xPos < opponent_.xPos + opponent_.xLen):
        ball_.yVel *= -1

def setup():
    size(800, 800)
    noStroke()

def draw():
    drawObjects()
  
    moveBall()
    player_.movePaddle()
    opponent_.movePaddle(ball_.xPos)
    detectWallCollisions()
    if (ball_.yPos <= player_.yPos + player_.yLen and ball_.yPos >= player_.yPos):
        detectPlayerPaddleCollisions()
    elif (ball_.yPos >= opponent_.yPos and ball_.yPos <= opponent_.yPos + opponent_.yLen):
        detectBotPaddleCollisions()