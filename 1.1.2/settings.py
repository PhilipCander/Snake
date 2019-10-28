import pygame
import random

pygame.init()


# importing header
header = pygame.image.load("rec/header.png")
# importing and setting up font
font = pygame.font.SysFont("comicsansms", 20)
font2 = pygame.font.SysFont("comicsansms", 60)
font3 = pygame.font.SysFont("comicsansms", 40)

# cherry frames
cherry1 = pygame.image.load("rec/cherry.png")
cherry2 = pygame.image.load("rec/cherry2.png")
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

# point pictures
points1 = pygame.image.load("rec/points/points1.png")
points2 = pygame.image.load("rec/points/points2.png")
points3 = pygame.image.load("rec/points/points3.png")
points4 = pygame.image.load("rec/points/points4.png")
points5 = pygame.image.load("rec/points/points5.png")
points6 = pygame.image.load("rec/points/points6.png")
points7 = pygame.image.load("rec/points/points7.png")
animationpoints = [points1, points1, points2, points2, points3, points3, points4, points4, points5, points5, points6, points6, points7, points7, points7, points7, points6, points6, points5, points5, points4, points4, points3, points3, points2, points2, points1, points1]
ipoi = 0
points = False

# snake pictures
snake_body = pygame.image.load("rec/snake_body.png")
snake_head = pygame.image.load("rec/snake_head.png")
snake_tail = pygame.image.load("rec/snake_tail.png")


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
gameSpeed = 3

# highscorefile
try:
    highscoreFile = open("rec/highscore.txt", "r")
    highscore = int(highscoreFile.read())
    highscoreFile.close()
except:
    highscoreFile = open("rec/highscore.txt", "w+")
    highscoreFile.write("0")
    highscoreFile.close()
    highscoreFile = open("rec/highscore.txt", "r")
    highscore = int(highscoreFile.read())
    highscoreFile.close()

# setting running variables to basic
run = False
gameover = False

