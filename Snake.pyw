#   19.10.2019
#           Developed by
#   Léon Spohr and Philip Cander
#   Version number: 1.0
#   SNAKE game

import pygame
import random

pygame.init()

# importing image
header = pygame.image.load("header.png")

# importing and setting up font
font = pygame.font.SysFont("comicsansms", 20)
font2 = pygame.font.SysFont("comicsansms", 60)
font3 = pygame.font.SysFont("comicsansms", 40)


# Score
score = 0

# window settings
screenwidth = 600
screenheight = 500
window = pygame.display.set_mode((screenwidth, screenheight))

# some colors
black = (0, 0, 0)
white = (250, 250, 250)
red = (250, 0, 0)

# size
snakeSize = 20

# speed and movement
moveY = 100
moveX = 20
playerChangeY = True
playerChangeX = True
y = False

# random starting value for cherry
cherryY = random.randint(2, 24) * 20
cherryX = random.randint(1, 29) * 20

# snake body
snakeLength = 0
lateList = []

# clock and speed
clock = pygame.time.Clock()
gameSpeed = 4

# highscorefile
try:
    highscoreFile = open("highscore.txt", "r")
    highscore = int(highscoreFile.read())
    highscoreFile.close()
except:
    highscoreFile = open("highscore.txt", "w+")
    highscoreFile.write("0")
    highscoreFile.close()
    highscoreFile = open("highscore.txt", "r")
    highscore = int(highscoreFile.read())
    highscoreFile.close()


# defining the start method
def startgame():
    global run
    startgamerun = True
    while startgamerun:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                startgamerun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = True
                    startgamerun = False

        window.fill(black)
        startText = font3.render("PRESS SPACE TO START", True, white)
        window.blit(startText, (50, 200))
        pygame.display.update()

# defining the gameover method
def rungameover():
    # globals
    global highscore
    global lateList
    global snakeLength
    global cherryY
    global cherryX
    global playerChangeX
    global playerChangeY
    global score
    global gameover
    global gameSpeed
    global moveY
    global moveX
    global y

    # checking for new highscore
    if score >= highscore:
        highscore = score
        # writing new highscore
        highscorefile = open("highscore.txt", "w")
        highscorefile.write(f"{highscore}")
        highscorefile.close()

    gameOverText = font2.render(" GAME OVER ", True, (250, 0, 0))
    window.fill(black)
    window.blit(gameOverText, (100, 200))
    pygame.display.update()
    pygame.time.delay(1000)
    gameover = False
    lateList = []
    snakeLength = 0
    score = 0
    gameSpeed = 4
    moveY = 100
    moveX = 20
    playerChangeY = False
    playerChangeX = True
    y = False
    cherryY = random.randint(2, 24) * 20
    cherryX = random.randint(1, 29) * 20
    window.fill(black)
    pygame.display.update()


# setting running variables to basic
run = False
gameover = False

# starting intro
startgame()

#   setting text up for drawing in main
scoreText = font.render(f"{score}      SPEED {gameSpeed}", True, (250, 250, 250))
highscorefile = open("highscore.txt", "r")
while run:
    highscorefile = open("highscore.txt", "r")
    clock.tick(gameSpeed)
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT:
            run = False

        #   request for key movement
        if event.type == pygame.KEYDOWN:
            # KEY UP = Move up
            if event.key == pygame.K_UP:
                y = True
                playerChangeY = False
                print("hoch")
            # KEY DOWN = Move down
            if event.key == pygame.K_DOWN:
                y = True
                playerChangeY = True
                print("runter")
            # KEY LEFT = Move left
            if event.key == pygame.K_LEFT:
                y = False
                playerChangeX = False
                print("links")
            # KEY RIGHT = Move right
            if event.key == pygame.K_RIGHT:
                y = False
                playerChangeX = True
                print("rechts")

    #   checking  if snake should move on Y
    if y:
        #   snake moving down
        if playerChangeY and moveY <= (screenheight - snakeSize):
            moveY += 20

        #   snake moving down
        elif not playerChangeY and moveY >= 20:
            moveY -= 20

    #   checking  if snake should move on X
    elif not y:
        #   snake moving right
        if playerChangeX and moveX <= (screenwidth - snakeSize):
            moveX += 20

        #   snake moving left
        elif not playerChangeX and moveX >= 0:
            moveX -= 20

    # coordinates of the snakes head
    print(" X", moveX, "  Y", moveY)

    # checking if snake hits cherry
    if cherryY == moveY and cherryX == moveX:
        score += 10
        gameSpeed += 0.25
        snakeLength += 1
        # spawning cherry again random
        cherryY = random.randint(2, 24) * 20
        cherryX = random.randint(1, 29) * 20

    # checking if snake is hitting the border
    if moveY == 20 or moveX == -20 or moveY >= screenheight or moveX >= screenwidth:
        print("game over")
        # if true = game over
        gameover = True

    # defining score text
    scoreText = font.render(f"SCORE: {score}   HIGHSCORE: {highscorefile.read()}  SPEED:  {gameSpeed}", True, (250, 250, 250))

    # fill window black
    window.fill(black)

    # adding bodyparts if cherry was eaten
    if snakeLength >= 1:
        # [-snakelength] gets snakelenght-amounts of lists from the latelist
        pygame.draw.rect(window, white,
                         (lateList[-snakeLength:][0][0], lateList[-snakeLength:][0][1], snakeSize, snakeSize))
        # iterates over all lists following (for the bodyparts)
        for LIST in lateList[-snakeLength:]:
            # extracts cord x and y out of the list
            pygame.draw.rect(window, white, (LIST[0], LIST[1], snakeSize, snakeSize))

            # checks if head runs into body
            if [LIST[0], LIST[1]] == [moveX, moveY]:
                # death
                gameover = True

    # gameover funktion
    if gameover:
        rungameover()
    window.blit(header, (0, 0))
    # blit score
    window.blit(scoreText, (10, 10))
    # blit cherry
    pygame.draw.rect(window, red, (cherryX, cherryY, 20, 20))
    # blit snake
    pygame.draw.rect(window, white, (moveX, moveY, snakeSize, snakeSize))
    pygame.display.update()
    # movement of last frame gets saved in latelist
    lateList.append([moveX, moveY])

highscorefile.close()
pygame.quit()
