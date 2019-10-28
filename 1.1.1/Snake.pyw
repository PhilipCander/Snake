#   28.10.2019
#           Developed by
#   Léon Spohr and Philip Cander
#   Version number: 1.1
#   SNAKE game

from settings import *

pygame.init()


def bganimation():
    global spritebg
    global ibg
    ibg += 1
    if ibg == 30:
        ibg = 0
    spritebg = animationbg[ibg]

def cherryanimation():
    global spritecherry
    global ic
    ic += 1
    if ic == 14:
        ic = 0
    spritecherry = animationcherry[ic]


# defining the start method
def startgame():
    global animation
    global sprite
    global run
    global window
    global width
    global height

    startgamerun = True
    while startgamerun:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.QUIT:
                run = False
                startgamerun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = True
                    startgamerun = False

        width = window.get_width()
        height = window.get_height()

        bganimation()
        window.blit(spritebg, (0, 0))
        startText = font3.render("PRESS SPACE TO START", True, white)
        window.blit(startText, ((width/2)- 250, (height/2)-60))
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
        highscorefile = open("rec/highscore.txt", "w")
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
    window.fill(blue)
    pygame.display.update()



# starting intro
startgame()

#   setting text up for drawing in main
scoreText = font.render(f"{score}      SPEED {gameSpeed}", True, (250, 250, 250))
highscorefile = open("rec/highscore.txt", "r")
while run:
    highscorefile = open("rec/highscore.txt", "r")
    clock.tick(gameSpeed)
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            run = False

        # getting size of the window
        width = window.get_width()
        height = window.get_height()

        #   request for key movement
        if event.type == pygame.KEYDOWN:
            # KEY UP = Move up
            if event.key == pygame.K_UP:
                y = True
                playerChangeY = False
                print("hoch")
            # KEY DOWN = Move down
            elif event.key == pygame.K_DOWN:
                y = True
                playerChangeY = True
                print("runter")
            # KEY LEFT = Move left
            elif event.key == pygame.K_LEFT:
                y = False
                playerChangeX = False
                print("links")
            # KEY RIGHT = Move right
            elif event.key == pygame.K_RIGHT:
                y = False
                playerChangeX = True
                print("rechts")

    moveXupdate = moveX + (width / 2) - (screenwidth / 2)
    moveYupdate = moveY + (height / 2) - (screenheight / 2)

    #   checking  if snake should move on Y
    if y:
        #   snake moving down
        if playerChangeY and moveYupdate <= ((height/2)+(screenheight/2) - snakeSize):
            moveY += 20

        #   snake moving up
        elif not playerChangeY and moveYupdate >= (height/2)-(screenheight/2)+10:
            moveY -= 20

    #   checking  if snake should move on X
    elif not y:
        #   snake moving right
        if playerChangeX and moveXupdate <= ((width/2)+(screenwidth/2) - snakeSize):
            moveX += 20

        #   snake moving left
        elif not playerChangeX and moveXupdate >= (width/2)-(screenwidth/2):
            moveX -= 20

    # updates X / Y after moving
    moveXupdate = moveX + (width / 2) - (screenwidth / 2)
    moveYupdate = moveY + (height / 2) - (screenheight / 2)

    # coordinates of the snakes head
    print(" X", moveXupdate, "  Y", moveYupdate)
    print(width, height)
    print(screenwidth, screenheight)

    # checking if snake hits cherry
    if cherryY == moveY and cherryX == moveX:
        score += 10
        gameSpeed += 0.25
        snakeLength += 1
        points = True
        # spawning cherry again random
        cherryX = random.randint(1, 29) * 20
        cherryY = random.randint(2, 24) * 20


    # checking if snake is hitting the border
    if moveYupdate <= (height/2)-(screenheight/2)+20 or moveXupdate == (width/2)-(screenwidth/2)-20 or moveYupdate >= (height/2)+(screenheight/2)\
            or moveXupdate >= (width/2)+(screenwidth/2):
        print("game over")
        # if true = game over
        gameover = True

    # defining score text
    scoreText = font.render(f"SCORE: {score}   HIGHSCORE: {highscorefile.read()}  SPEED:  {gameSpeed}", True, (250, 250, 250))

    # fill window black
    window.blit(animationbg[1], (0, 0))
    pygame.draw.rect(window, black,
                     ((width / 2) - (screenwidth / 2), (height / 2) - (screenheight / 2), screenwidth, screenheight))
    # adding bodyparts if cherry was eaten
    if snakeLength >= 1:
        # [-snakelength] gets snakelenght-amounts of lists from the latelist
        window.blit(snake_body, (lateList[-snakeLength:][0][0], lateList[-snakeLength:][0][1]))
        # iterates over all lists following (for the bodyparts)
        for LIST in lateList[-snakeLength:]:
            # extracts cord x and y out of the list
            window.blit(snake_body, (LIST[0], LIST[1]))

            # checks if head runs into body
            if [LIST[0], LIST[1]] == [moveXupdate, moveYupdate]:
                # death
                gameover = True

    # gameover function
    if gameover:
        rungameover()

    window.blit(header, ((width/2)-(screenwidth/2), (height/2)-(screenheight/2)))
    # blit score
    window.blit(scoreText, ((width/2)-290, (height/2)-244))
    # blit cherry
    cherryXupdate = cherryX + (width/2) - (screenwidth/2)
    cherryYupdate = cherryY + (height/2) - (screenheight/2)
    cherryanimation()
    window.blit(spritecherry, (cherryXupdate, cherryYupdate))
    # blit snake
    moveXupdate = moveX + (width/2) - (screenwidth/2)
    moveYupdate = moveY + (height/2) - (screenheight/2)
    window.blit(snake_body, (moveXupdate, moveYupdate))
    pygame.display.update()
    # movement of last frame gets saved in latelist
    lateList.append([moveXupdate, moveYupdate])

highscorefile.close()
pygame.quit()
