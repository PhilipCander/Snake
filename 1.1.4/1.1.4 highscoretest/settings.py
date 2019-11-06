import pygame
import random
import pickle

pygame.init()


# importing header
header = pygame.image.load("rec/window/header.png")

# importing textfield
textfield = pygame.image.load("rec/text_field.png")
scoretextfield = pygame.image.load("rec/scoretextfield.png")

# importing start and stop button
start1 = pygame.image.load("rec/window/start.png")
start2 = pygame.image.load("rec/window/start2.png")
stop1 = pygame.image.load("rec/window/stop.png")
stop2 = pygame.image.load("rec/window/stop2.png")

# importing yes and no button
yes1 = pygame.image.load("rec/window/yes.png")
yes2 = pygame.image.load("rec/window/yes2.png")
no1 = pygame.image.load("rec/window/no.png")
no2 = pygame.image.load("rec/window/no2.png")

# importing and setting up font
font = pygame.font.SysFont("comicsansms", 20)
font2 = pygame.font.SysFont("comicsansms", 60)
font3 = pygame.font.SysFont("comicsansms", 40)

# cherry frames
cherry1 = pygame.image.load("rec/cherry/cherry.png")
cherry2 = pygame.image.load("rec/cherry/cherry2.png")
animationcherry = [cherry1, cherry1, cherry1, cherry1, cherry1, cherry1, cherry1, cherry2, cherry2, cherry2, cherry2, cherry2, cherry2, cherry2]
ic = 0

# frames for startgame
bg1 = pygame.image.load("rec/bg/bg.png")
bg2 = pygame.image.load("rec/bg/bg2.png")
bg3 = pygame.image.load("rec/bg/bg3.png")
bg4 = pygame.image.load("rec/bg/bg4.png")
bg5 = pygame.image.load("rec/bg/bg5.png")
bg6 = pygame.image.load("rec/bg/bg6.png")
animationbg = [bg1, bg1, bg1, bg2, bg2, bg2, bg3, bg3, bg3, bg4, bg4, bg4, bg5, bg5, bg5, bg6, bg6, bg6, bg5, bg5, bg5, bg4, bg4, bg4, bg3, bg3, bg3, bg2, bg2, bg2]
ibg = 0

# frames for the ground
ground1 = pygame.image.load("rec/window/ground1.png")
ground2 = pygame.image.load("rec/window/ground2.png")
ground3 = pygame.image.load("rec/window/ground3.png")
animationground = [ground1, ground1, ground1, ground1, ground1, ground1, ground2, ground2, ground2, ground2, ground2, ground2]
igr = 0

# point pictures
points1 = pygame.image.load("rec/points/points1.png")
points2 = pygame.image.load("rec/points/points2.png")
points3 = pygame.image.load("rec/points/points3.png")
points4 = pygame.image.load("rec/points/points4.png")
points5 = pygame.image.load("rec/points/points5.png")
points6 = pygame.image.load("rec/points/points6.png")
points7 = pygame.image.load("rec/points/points7.png")
animationpoints = [points1, points1, points2, points2, points3, points3, points4, points4, points5, points5, points6, points6, points7, points7, points7, points7]
ipoi = 0
pointsX = 0
pointsY = 0
points = False

# timer pictures
timer1 = pygame.image.load("rec/timer/timer1.png")
timer2 = pygame.image.load("rec/timer/timer2.png")
timer3 = pygame.image.load("rec/timer/timer3.png")
timer4 = pygame.image.load("rec/timer/timer4.png")
timer5 = pygame.image.load("rec/timer/timer5.png")
timer6 = pygame.image.load("rec/timer/timer6.png")
timer7 = pygame.image.load("rec/timer/timer7.png")
timer8 = pygame.image.load("rec/timer/timer8.png")
animationtimer = [timer1, timer1, timer2, timer2, timer3, timer3, timer4, timer4, timer5, timer5, timer6, timer6, timer7, timer7, timer8, timer8]
itm = 0
timer_done = True
timer_count = 0
timerX = random.randint(0, 0)
timerY = random.randint(0, 0)


# snake pictures
snake_body = pygame.image.load("rec/snake/snake_body.png")
snake_head = pygame.image.load("rec/snake/snake_head.png")
snake_tail = pygame.image.load("rec/snake/snake_tail.png")
looking_left = True
looking_right = False
looking_up = False
looking_down = False


# window settings
screenwidth = 600
screenheight = 500
window = pygame.display.set_mode((screenwidth, screenheight), pygame.RESIZABLE)
width = window.get_width()
height = window.get_height()


# some colors
black = (0, 0, 0)
white = (250, 250, 250)
red = (250, 0, 0)
blue = (0, 0, 250)

# Score
score = 0

# size
snakeSize = 20

# speed and movement
moveY = 100 + (height/2) - (screenheight/2)
moveX = 100 + (width/2) - (screenwidth/2)
playerChangeY = True
playerChangeX = True
y = False

# random starting value for cherry
cherryX = random.randint(1, 29) * 20 + (width/2) - (screenwidth/2)
cherryY = random.randint(2, 24) * 20 + (height/2) - (screenheight/2)

# snake body
snakeLength = 0
lateList = []

# clock and speed
clock = pygame.time.Clock()
gameSpeed = 5


# setting running variables to basic
run = False
gameover = False
