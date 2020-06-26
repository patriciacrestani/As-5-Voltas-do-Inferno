from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
import pygame
from Heroi import *
import random
random.seed()


class Inimigo(object):
    def __init__(self, filename, x, y, speedX, speedY):
        self.filename = filename
        self.img = GameImage(filename)
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY

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

    def update(self, dt):
        self.x += self.speedX*dt
        self.y += self.speedY*dt

    def windowCollision(self, x, y, w, h):
        if (self.y < y):  #colidiu com teto
            self.speedY = -self.speedY
            self.y = y
        if (self.y + 48 > h):  #colidiu com chao
            self.speedY = -self.speedY
            self.y = h - 48
        if(self.x < x): #colidiu com a parede esquerda
            self.speedX = -self.speedX
            self.x = x
        if(self.x+39 > w): #colidiu com a parede direita
            self.speedX = -self.speedX
            self.x = w-39