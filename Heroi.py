from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
import pygame


class Heroi(object):
    def __init__(self, filename, x, y):
        self.filename = filename
        self.img = GameImage(filename)
        self.x = x
        self.y = y
        self.delay = 0

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_img(self, filename):
        self.img = GameImage(filename)

    def draw(self):
        self.img.set_position(self.x, self.y)
        self.img.draw()

    def update(self, dt):
        # vazio
        nada = 1

    def windowCollision(self, x, y, w, h):
        if (self.y < y):  #colidiu com teto
            self.y = y
        if (self.y + 48 > h):  #colidiu com chao
            self.y = h - 48
        if(self.x < x): #colidiu com a parede esquerda
            self.x = x
        if(self.x+36 > w): #colidiu com a parede direita
            self.x = w - 36
