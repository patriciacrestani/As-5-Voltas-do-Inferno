from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
import pygame
from Heroi import *
import random
random.seed()


class Demon(object):
    def __init__(self, filename, x, y):
        self.filename = filename
        self.img = GameImage(filename)
        self.x = x
        self.y = y
        self.tempo = 0

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getImg(self):
        return self.img

    def setSpeedX(self, sx):
        self.speedX = sx

    def setSpeedY(self, sy):
        self.speedY = sy

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        
        self.img.set_position(self.x, self.y)
        self.img.draw()
        if (self.tempo % 50) == 0:
            print("yes")
            self.x = -1000
            self.y = -1000
        

    def update(self):
        
        self.tempo += 1
        self.x += 0
        self.y += 0

       
            

    def windowCollision(self, x, y, w, h):
        if (self.y < 0):  #colidiu com teto
            self.x = -1000
            self.y = -1000
        if (self.y > 700):  #colidiu com chao
            self.x = -1000
            self.y = -1000
        if(self.x < 0): #colidiu com a parede esquerda
            self.speedX = 0
            self.x = -1000
            self.y = -1000
        if(self.x > 900): #colidiu com a parede direita
            self.speedX = 0
            self.x = -1000
