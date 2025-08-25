import pygame

class Ship:
    '''Una classe per gestire l'astronava'''
    
    def __init__(self, ai_game):
        '''Inizializza la nave e ne imposta la posizione iniziale'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # carica l'immagine della nave e ne ottiene il rettangolo
        self.image = pygame.image.load('images/spaceships/bgbattleship.bmp')
        self.rect = self.image.get_rect()
        
        # avvia ogni nuova nave in fondo allo schermo, al centro (posizione iniziale)
        self.rect.midbottom = self.screen_rect.midbottom
        
        # flag del movimento; inizia con una nave che non si muove
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        '''Aggiorna la posizione della nave in base al flag del movimento'''
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
    
    def blitme(self):
        '''Disegna la nave nella sua posizione corrente'''
        self.screen.blit(self.image, self.rect)