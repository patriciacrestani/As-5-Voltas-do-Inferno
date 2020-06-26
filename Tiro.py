from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
import pygame

from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
import pygame

class Tiro():
    def __init__(self, filename, x, y, posX, posY):
        self.filename = filename
        self.img = GameImage(filename)
        self.x = x
        self.y = y
        self.posX = posX
        self.posY = posY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getImg(self):
        return self.img

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.img.set_position(self.x, self.y)
        self.img.draw()

    def update(self, dt):
        self.x = self.x + self.posX*6
        self.y = self.y + self.posY*6

    def windowCollision(self, x, y, w, h):
        if (self.y < y):  #colidiu com teto
            self.y = -50
            self.visible = False
        if (self.y + 16 > h):  #colidiu com chao
            self.y = -50
            self.visible = False
        if(self.x < x): #colidiu com a parede esquerda
            self.x = -50
            self.visible = False
        if(self.x + 16 > w): #colidiu com a parede direita
            self.x = -50
            self.visible = False
