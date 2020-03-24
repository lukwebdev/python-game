import pygame
from random import randint

BLACK = (0,0,0)

# class represents a ball  from the "Sprite" class in Pygame
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__() # Call the parent class (Sprite) constructor

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-9, 8)] #vector: x=...,  y=... remove 0 ???!!!!!!!!!!!!!!!!

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0] #move ball x
        self.rect.y += self.velocity[1] #move ball y
        if self.rect.y == 0:            #remove 0 from y moving ball 
            self.rect.y = randint(-8, -2)

    def bounce(self):
        self.velocity[0] = -self.velocity[0]        #if bounce change vector x for -x
        self.velocity[1] = randint(-9, 8)           #if bounce change vector y for y

        if self.velocity[1] == 0:                   #remove 0 from y moving ball 
            self.velocity[1] = randint(-8, -2)

# remove 0 from colision ball paddle
    def bounce2(self):
        self.velocity[0] = -self.velocity[0]        #if bounce change vector x for -x
        self.velocity[1] = randint(-8, -2)          #if bounce change vector y for y