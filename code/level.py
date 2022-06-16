import pygame

class Level:
    def __init__(self):

        # display surface
        self.display_surface = pygame.display.get_surface()
        
        #sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        # update and draw
        pass