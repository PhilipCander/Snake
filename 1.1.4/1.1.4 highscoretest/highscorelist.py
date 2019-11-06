import pickle
import random

with open("rec/highscorelist.data", "rb") as file:
    highscorelist = pickle.load(file)

#highscorelist = [['Léon', 16], ['PHILIP', 3], ['---', 0], ['---', 0], ['---', 0], ['---', 0], ['---', 0]]
print(highscorelist)

with open("rec/highscorelist.data", "wb")as file:
    pickle.dump(highscorelist, file)