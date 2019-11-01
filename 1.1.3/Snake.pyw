#   29.10.2019
#           Developed by
#   Léon Spohr and Philip Cander
#   Version number: 1.3
#   SNAKE game

from settings import *

pygame.init()


def ground_animation():
    global spriteground
    global igr
    igr += 1
    if igr == 12:
        igr = 0
    spriteground = animationground[igr]


def bg_animation():
    global spritebg
    global ibg
    ibg += 1
    if ibg == 30:
        ibg = 0
    spritebg = animationbg[ibg]


# cherry animation
def cherry_animation():
    global spritecherry
    global ic
    ic += 1
    if ic == 14:
        ic = 0
    spritecherry = animationcherry[ic]


# points animation
def points_animation():
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
def timer_animation():
    global spritetimer
    global itm
    global timer_done
    global timer_count
    itm += 1
    timer_count += 1
    if itm == 16:
        itm = 0
    spritetimer = animationtimer[itm]
    if timer_count == 30:
        timer_done = True


def ask_for_quit():
    global run
    global gameover
    global width
    global height
    global window
    asking = True
    askingwidth = 350
    askingheight = 200
    askingText = font.render("ARE YOU SURE TO LEAVE ?", True, (0, 0, 0))
    while asking:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.QUIT:
                asking = False
        width = window.get_width()
        height = window.get_height()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(window, red, (
        (width/2)-(askingwidth/2), (height/2)-(askingheight/2), askingwidth, askingheight))
        window.blit(askingText, ((width/2)-(askingwidth/2), (height/2)-(askingheight/2)))

        if (width/2)-(askingwidth/2)+25 <= mouse[0] <= (width/2)-(askingwidth/2)+150 and (height/2)-(askingheight/2)+150 >= mouse[1] >= (height/2)-(askingheight/2)+75:
            window.blit(yes2, ((width/2)-(askingwidth/2)+25, (height/2)-(askingheight/2)+75))
            if click[0] == 1:
                run = False
                gameover = False
                highscoreFile.close()
                pygame.quit()
        else:
            window.blit(yes1, ((width/2)-(askingwidth/2)+25, (height/2)-(askingheight/2)+75))

        if (width/2)-(askingwidth/2)+200 <= mouse[0] <= (width/2)-(askingwidth/2)+325 and (height/2)-(askingheight/2)+150 >= mouse[1] >= (height/2)-(askingheight/2)+75:
            window.blit(no2, ((width/2)-(askingwidth/2)+200, (height/2)-(askingheight/2)+75))
            if click[0] == 1:
                break
        else:
            window.blit(no1, ((width/2)-(askingwidth/2)+200, (height/2)-(askingheight/2)+75))

        pygame.display.update()

# defining the start method
def start_game():
    global animation
    global sprite
    global run
    global window
    global width
    global height

    start_game_run = True
    while start_game_run:
        clock.tick(30)
        width = window.get_width()
        height = window.get_height()
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.QUIT:
                ask_for_quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                if event.key == pygame.K_SPACE:
                    run = True
                    start_game_run = False

        width = window.get_width()
        height = window.get_height()

        bg_animation()
        window.blit(spritebg, (0, 0))
        startText = font3.render("PRESS SPACE TO START", True, white)
        window.blit(startText, ((width / 2) - 250, (height / 2) - 60))
        pygame.display.update()


# defining the gameover method
def run_gameover():
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
    global run
    global width
    global height
    global window

    # checking for new highscore
    if score >= highscore:
        highscore = score
        # writing new highscore
        highscorefile = open("rec/highscore.txt", "w")
        highscorefile.write(f"{highscore}")
        highscorefile.close()

    gameOverText = font2.render(" GAME OVER ", True, (250, 0, 0))
    gameover = True
    while gameover:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.QUIT:
                ask_for_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    gameover = False
                    run = False
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        window.blit(ground3, ((width/2)-(screenwidth/2), (height/2)-(screenheight/2)+40))

        width = window.get_width()
        height = window.get_height()

        # start Button
        if (width/2)-(screenwidth/2)+50 <= mouse[0] <= (width/2)-(screenwidth/2)+290 and \
                (height/2)-(screenheight/2)+340 >= mouse[1] >= (height/2)-(screenheight/2)+200:
            window.blit(start2, ((width/2)-(screenwidth/2)+50, (height/2)-(screenheight/2)+200))
            if click[0] == 1:
                gameover = False
                run = True
        else:
            window.blit(start1, ((width/2)-(screenwidth/2)+50, (height/2)-(screenheight/2)+200))

        # stop Button
        if (width/2)-(screenwidth/2)+310 <= mouse[0] <= (width/2)-(screenwidth/2)+550 and \
                (height/2)-(screenheight/2)+340 >= mouse[1] >= (height/2)-(screenheight/2)+200:
            window.blit(stop2, ((width/2)-(screenwidth/2)+310, (height/2)-(screenheight/2)+200))
            if click[0] == 1:
                ask_for_quit()
        else:
            window.blit(stop1, ((width/2)-(screenwidth/2)+310, (height/2)-(screenheight/2)+200))

        pygame.display.update()

    # setting variables to basic
    gameover = False
    lateList = []
    snakeLength = 0
    score = 0
    points = False
    gameSpeed = 5
    moveY = 100
    moveX = 20
    playerChangeY = False
    playerChangeX = True
    y = False
    cherryY = random.randint(2, 24) * 20
    cherryX = random.randint(1, 29) * 20
    timer_done = True
    window.blit(ground3, ((width/2)-(screenwidth/2), (height/2)-(screenheight/2)+40))
    pygame.display.update()


# starting intro
start_game()

#   setting text up for drawing in main
scoreText = font.render(f"{score}      SPEED {gameSpeed-4}", True, (250, 250, 250))
highscorefile = open("rec/highscore.txt", "r")
while run:
    highscorefile = open("rec/highscore.txt", "r")
    clock.tick(gameSpeed)
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            ask_for_quit()

        # getting size of the window
        width = window.get_width()
        height = window.get_height()

        #   request for key movement
        if event.type == pygame.KEYDOWN:
            # KEY UP = Move up
            if event.key == pygame.K_ESCAPE:
                pygame.display.toggle_fullscreen()
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
        if playerChangeY and moveYupdate <= ((height / 2) + (screenheight / 2) - snakeSize):
            moveY += 20
            looking_down = True
            looking_up = False
            looking_left = False
            looking_right = False

        #   snake moving up
        elif not playerChangeY and moveYupdate >= (height / 2) - (screenheight / 2) + 10:
            moveY -= 20
            looking_down = False
            looking_up = True
            looking_left = False
            looking_right = False

    #   checking  if snake should move on X
    elif not y:
        #   snake moving right
        if playerChangeX and moveXupdate <= ((width / 2) + (screenwidth / 2) - snakeSize):
            moveX += 20
            looking_down = False
            looking_up = False
            looking_left = False
            looking_right = True

        #   snake moving left
        elif not playerChangeX and moveXupdate >= (width / 2) - (screenwidth / 2):
            moveX -= 20
            looking_down = False
            looking_up = False
            looking_left = True
            looking_right = False

    # updates X / Y after moving
    moveXupdate = moveX + (width / 2) - (screenwidth / 2)
    moveYupdate = moveY + (height / 2) - (screenheight / 2)

    lateList.append([moveXupdate, moveYupdate, looking_down, looking_up, looking_left, looking_right])

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
    if timer_done and gameSpeed >= 10:
        spawn_chance = random.randint(0, 30)
        if spawn_chance == 1:
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
    if moveYupdate <= (height / 2) - (screenheight / 2) + 20 or moveXupdate == (width / 2) - (
            screenwidth / 2) - 20 or moveYupdate >= \
            (height / 2) + (screenheight / 2) or moveXupdate >= (width / 2) + (screenwidth / 2):
        print("game over")
        # if true = game over
        gameover = True

    # defining score text
    scoreText = font.render(f"SCORE: {score}   HIGHSCORE: {highscorefile.read()}  SPEED:  {gameSpeed}", True,
                            (250, 250, 250))

    # fill window black
    window.blit(animationbg[1], (0, 0))
    pygame.draw.rect(window, black,
                     ((width / 2) - (screenwidth / 2), (height / 2) - (screenheight / 2), screenwidth, screenheight))
    # blit ground
    groundX = (width / 2) - (screenwidth / 2)
    groundY = (height / 2) - (screenheight / 2) + 40
    ground_animation()
    window.blit(ground3, (groundX, groundY))

    # adding bodyparts if cherry was eaten
    if snakeLength >= 1:
        print(lateList[-snakeLength])
        # extracts direction out of latelist
        # rotates up
        if lateList[-snakeLength][2] == True:
            snake_tail = pygame.image.load("rec/snake/snake_tail.png")
            snake_tail = pygame.transform.rotate(snake_tail, 270)
            print("up")
        # rotates down
        elif lateList[-snakeLength][3] == True:
            snake_tail = pygame.image.load("rec/snake/snake_tail.png")
            snake_tail = pygame.transform.rotate(snake_tail, 90)
            print("down")
        # rotates left
        elif lateList[-snakeLength][4] == True:
            snake_tail = pygame.image.load("rec/snake/snake_tail.png")
            snake_tail = pygame.transform.rotate(snake_tail, 180)
            print("left")
        # rotates right
        elif lateList[-snakeLength][5] == True:
            snake_tail = pygame.image.load("rec/snake/snake_tail.png")
            print("right")
        # iterates over all lists following (for the bodyparts)
        if snakeLength >= 2:
            print("latelist")
            print(lateList)
            print("lateList[(-snakeLength):]")
            print(lateList[(-snakeLength) - 1:])
            print("lateList[(-snakeLength):-1]")
            print(lateList[(-snakeLength):-1])
            for LIST in lateList[-snakeLength:-1]:
                print(LIST)
                # extracts cord x and y out of the list
                window.blit(snake_body, (LIST[0], LIST[1]))

                # checks if head runs into body
                print(f"move:{[moveXupdate, moveYupdate]}")
                if [LIST[0], LIST[1]] == [moveXupdate, moveYupdate]:
                    # death
                    gameover = True
        # displays tail
        snakeLength += 1
        window.blit(snake_tail, (lateList[-snakeLength][0], lateList[-snakeLength][1]))
        snakeLength -= 1

    # gameover function
    if gameover:
        run_gameover()

    window.blit(header, ((width / 2) - (screenwidth / 2), (height / 2) - (screenheight / 2)))
    # blit score
    window.blit(scoreText, ((width / 2) - 290, (height / 2) - 244))

    # blit cherry
    cherryXupdate = cherryX + (width / 2) - (screenwidth / 2)
    cherryYupdate = cherryY + (height / 2) - (screenheight / 2)
    cherry_animation()
    window.blit(spritecherry, (cherryXupdate, cherryYupdate))
    # blit points
    if points:
        points_animation()
        window.blit(spritepoints, (pointsX, pointsY))
    # blit timer
    if not timer_done:
        timerXupdate = timerX + (width / 2) - (screenwidth / 2)
        timerYupdate = timerY + (height / 2) - (screenheight / 2)
        timer_animation()
        window.blit(spritetimer, (timerXupdate, timerYupdate))
    # blit snake
    moveXupdate = moveX + (width / 2) - (screenwidth / 2)
    moveYupdate = moveY + (height / 2) - (screenheight / 2)
    window.blit(snake_head, (moveXupdate, moveYupdate))
    pygame.display.update()

highscorefile.close()
pygame.quit()
