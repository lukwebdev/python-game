import pygame

BLACK = (0, 0, 0)

# create object sprite named Paddle
class Paddle(pygame.sprite.Sprite):                                        # spirit simple visible game(graphic) object

    def __init__(self, color, width, height):                              # constructor
        super().__init__()                                                 # parent class (Sprite) constructor

        self.image = pygame.Surface([width, height])                       # create image of the block on width and height
        self.image.fill(BLACK)                                             # bg color
        self.image.set_colorkey(BLACK)                                     # alpha color

        pygame.draw.rect(self.image, color, [0, 0, width, height])         # draw rectangle

        self.rect = self.image.get_rect()                                  # take the rectangle object that has the dimensions of the image

    def moveLeft(self, pixels):
        self.rect.x -= pixels                                              # move object to left by ...pixels
        if self.rect.x <= 0:                                               # or self.rect.x = 0
            self.rect.x = 0                                                # off the screen

    def moveRight(self, pixels):
        self.rect.x += pixels                                              # move object to right by ...pixels
        if self.rect.x >= 700:                                             # or self.rect.x = 700
            self.rect.x = 700
