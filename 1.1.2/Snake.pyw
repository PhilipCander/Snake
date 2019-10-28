#   28.10.2019
#           Developed by
#   Léon Spohr and Philip Cander
#   Version number: 1.1
#   SNAKE game

from settings import *

pygame.init()

def groundanimation():
    global spriteground
    global igr
    igr += 1
    if igr == 12:
        igr = 0
    spriteground = animationground[igr]

def bganimation():
    global spritebg
    global ibg
    ibg += 1
    if ibg == 30:
        ibg = 0
    spritebg = animationbg[ibg]


# cherry animation
def cherryanimation():
    global spritecherry
    global ic
    ic += 1
    if ic == 14:
        ic = 0
    spritecherry = animationcherry[ic]


# points animation
def pointsanimation():
    global spritepoints
    global ipoi
    global pointsY
    global pointsX
    global points
    ipoi += 1
    if ipoi == 16:
        ipoi = 0
        points = False
        pointsX = -10
        pointsY = -10
    spritepoints = animationpoints[ipoi]


# timer animation
def timeranimation():
    global spritetimer
    global itm
    global timer_done
    global timer_count
    itm +=1
    timer_count += 1
    if itm == 16:
        itm = 0
    spritetimer = animationtimer[itm]
    if timer_count == 30:
        timer_done = True


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
    global timer_done
    global points

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
    points = False
    gameSpeed = 3
    moveY = 100
    moveX = 20
    playerChangeY = False
    playerChangeX = True
    y = False
    cherryY = random.randint(2, 24) * 20
    cherryX = random.randint(1, 29) * 20
    timer_done = True
    window.fill(black)
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
            looking_down = True
            looking_up = False
            looking_left = False
            looking_right = False

        #   snake moving up
        elif not playerChangeY and moveYupdate >= (height/2)-(screenheight/2)+10:
            moveY -= 20
            looking_down = False
            looking_up = True
            looking_left = False
            looking_right = False

    #   checking  if snake should move on X
    elif not y:
        #   snake moving right
        if playerChangeX and moveXupdate <= ((width/2)+(screenwidth/2) - snakeSize):
            moveX += 20
            looking_down = False
            looking_up = False
            looking_left = False
            looking_right = True

        #   snake moving left
        elif not playerChangeX and moveXupdate >= (width/2)-(screenwidth/2):
            moveX -= 20
            looking_down = False
            looking_up = False
            looking_left = True
            looking_right = False

    # updates X / Y after moving
    moveXupdate = moveX + (width / 2) - (screenwidth / 2)
    moveYupdate = moveY + (height / 2) - (screenheight / 2)

    # coordinates of the snakes head
    print(" X", moveXupdate, "  Y", moveYupdate)

    # checking for looking direction
    if looking_up:
        snake_head = pygame.image.load("rec/snake/snake_head.png")
        snake_head = pygame.transform.rotate(snake_head, 90)
    if looking_down:
        snake_head = pygame.image.load("rec/snake/snake_head.png")
        snake_head = pygame.transform.rotate(snake_head, 270)
    if looking_left:
        snake_head = pygame.image.load("rec/snake/snake_head.png")
        snake_head = pygame.transform.rotate(snake_head, 180)
    if looking_right:
        snake_head = pygame.image.load("rec/snake/snake_head.png")

    # creating within random value random spawn for timer
    if timer_done and gameSpeed >= 5:
        spawn_chance = random.randint(0, 25)
        if spawn_chance == 25:
            timerX = random.randint(1, 29) * 20
            timerY = random.randint(2, 24) * 20
            timer_done = False

    # checking if snake hits the timer
    if timerX == moveX and timerY == moveY:
        gameSpeed -= 1
        timer_done = True
        timer_count = 0

    # checking if snake hits cherry
    if cherryY == moveY and cherryX == moveX:
        score += 10
        gameSpeed += 0.25
        snakeLength += 1
        points = True
        pointsX = moveXupdate
        pointsY = moveYupdate
        # spawning cherry again random
        cherryX = random.randint(1, 29) * 20
        cherryY = random.randint(2, 24) * 20


    # checking if snake is hitting the border
    if moveYupdate <= (height/2)-(screenheight/2)+20 or moveXupdate == (width/2)-(screenwidth/2)-20 or moveYupdate >= \
            (height/2)+(screenheight/2) or moveXupdate >= (width/2)+(screenwidth/2):
        print("game over")
        # if true = game over
        gameover = True

    # defining score text
    scoreText = font.render(f"SCORE: {score}   HIGHSCORE: {highscorefile.read()}  SPEED:  {gameSpeed}", True, (250, 250, 250))

    # fill window black
    window.blit(animationbg[1], (0, 0))
    pygame.draw.rect(window, black,
                     ((width / 2) - (screenwidth / 2), (height / 2) - (screenheight / 2), screenwidth, screenheight))
    # blit ground
    groundX = (width / 2) - (screenwidth / 2)
    groundY = (height / 2) - (screenheight / 2) + 40
    groundanimation()
    window.blit(spriteground, (groundX, groundY))
    # adding bodyparts if cherry was eaten
    if snakeLength >= 1:
        # [-snakelength] gets snakelenght-amounts of lists from the latelist
        window.blit(snake_tail, (lateList[-snakeLength:][0][0], lateList[-snakeLength:][0][1]))
        # iterates over all lists following (for the bodyparts)
        if snakeLength >= 2:
            snakeLength -= 1
            for LIST in lateList[-snakeLength:]:
                # extracts cord x and y out of the list
                window.blit(snake_body, (LIST[0], LIST[1]))

                # checks if head runs into body
                if [LIST[0], LIST[1]] == [moveXupdate, moveYupdate]:
                    # death
                    gameover = True
            snakeLength += 1

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
    # blit points
    if points:
        pointsanimation()
        window.blit(spritepoints, (pointsX, pointsY))
    # blit timer
    if not timer_done:
        timerXupdate = timerX + (width/2) - (screenwidth/2)
        timerYupdate = timerY + (height/2) - (screenheight/2)
        timeranimation()
        window.blit(spritetimer, (timerXupdate, timerYupdate))
    # blit snake
    moveXupdate = moveX + (width/2) - (screenwidth/2)
    moveYupdate = moveY + (height/2) - (screenheight/2)
    window.blit(snake_head, (moveXupdate, moveYupdate))
    pygame.display.update()
    # movement of last frame gets saved in latelist
    lateList.append([moveXupdate, moveYupdate])

highscorefile.close()
pygame.quit()
