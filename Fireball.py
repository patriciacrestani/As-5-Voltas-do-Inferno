from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
import pygame
from Heroi import *
import random
random.seed()


class Fireball(object):
    def __init__(self, filename, x, y, direction):
        self.filename = filename
        self.img = GameImage(filename)
        self.x = x
        self.y = y
        self.speedX = 10
        self.speedY = 10
        self.orientacao = direction 

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

    def update(self):
        if self.orientacao == 1:
            self.x += self.speedX
            self.y += self.speedY
        elif self.orientacao == -1:
            self.x += self.speedX
            self.y -= self.speedY
        elif self.orientacao == 2:
            self.x -= self.speedX
            self.y -= self.speedY
        elif self.orientacao == -2:
            self.x -= self.speedX
            self.y += self.speedY

    def windowCollision(self, x, y, w, h):
        if (self.y < y):  #colidiu com teto
            self.speedY = -self.speedY
            self.y = y
        if (self.y + 48 > h):  #colidiu com chao
            self.speedY = -self.speedY
            self.y = h - 48
        if(self.x < 0): #colidiu com a parede esquerda
            self.speedX = 0
            self.x = -1000
            self.y = -1000
        if(self.x > 900): #colidiu com a parede direita
            self.speedX = 0
            self.x = -1000
            self.y = -1000
