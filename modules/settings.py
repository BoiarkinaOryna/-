import pygame
import modules.path_to_file as m_file

pygame.init()

class Figure:
    def __init__(self,  width, height, x, y, name_file):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.NAME_FILE = name_file
        self.IMAGE = None
        
    def load_image(self, flip = False):
        image_load = pygame.image.load(m_file.path_to_file(self.NAME_FILE))
       
        image_transform = pygame.transform.scale(image_load, (self.WIDTH, self.HEIGHT))
       
        image_flip = image_transform
        if flip == True:
            image_flip = pygame.transform.rotate(image_transform, 90)
        return image_flip

    def blit_sprite(self, screen_game, flip = False):
        screen_game.blit(self.load_image(flip= flip), (self.X, self.Y))

class My_Board(Figure):
    def __init__(self, width1 = 400, height1 = 400, x1 = 75, y1 = 50, name_file1 = 'images/game-board.png'):
        Figure.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)
board = My_Board()

class Bot_Board(Figure):
    def __init__(self, width1 = 400, height1 = 400, x1 = 535, y1 = 50, name_file1 = 'images/game-board.png'):
        Figure.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)
bot_board = Bot_Board()

class Ship1(Figure):
    def __init__(self, width1 = 35, height1 = 35, x1 = 0, y1 = 0, name_file1 = 'images/1.png'):
        Figure.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)

class Ship2(Figure):
    def __init__(self, width1 = 35, height1 = 65, x1 = 0, y1 = 0, name_file1 = 'images/2.png'):
        Figure.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)
        
class Ship3(Figure):
    def __init__(self, width1 = 35, height1 = 100, x1 = 0, y1 = 0, name_file1 = 'images/3.png'):
        Figure.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)
        
class Ship4(Figure):
    def __init__(self, width1 = 40, height1 = 140, x1 = 0, y1 = 0, name_file1 = 'images/4.png'):
        Figure.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)
class Cross(Figure):
    def __init__(self, width1 = 25, height1 = 25, x1 = 0, y1 = 0, name_file1 = 'images/cross.png'):
        Figure.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)
class Mark(Figure):
    def __init__(self, width1 = 50, height1 = 50, x1 = 250, y1 = 600, name_file1 = 'images/arrow.png'):
        Figure.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)
class Plain(Figure):
    def __init__(self, width1 = 250, height1 = 200, x1 = 0, y1 = 500, name_file1 = 'images/plain.jpg'):
        Figure.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)
class Explosion(Figure):
    def __init__(self, width1 = 25, height1 = 25, x1 = 0, y1 = 0, name_file1 = 'images/explosion.png'):
        Figure.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)

mark = Mark()
plain = Plain()