import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''La classe che rappresenta un singolo alieno della flotta'''
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # carica l'immagine dell'alieno e ne imposta l'attributo rect
        self.image = pygame.image.load('images/aliens/alien4.png')
        self.image = pygame.transform.scale(self.image, self.settings.alien_size)
        self.image = pygame.transform.rotate(self.image, self.settings.alien_img_rotation)
        self.rect = self.image.get_rect()
        
        # avvia ogni nuovo alieno in alto a sinistra nella schermata
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # memorizza la posizione orizzontale precisa dell'alieno
        self.x = float(self.rect.x)