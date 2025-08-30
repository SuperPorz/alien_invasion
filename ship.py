import pygame

class Ship:
    '''Una classe per gestire l'astronava'''
    
    def __init__(self, ai_game):
        '''Inizializza la nave e ne imposta la posizione iniziale'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # carica l'immagine della nave e ne ottiene il rettangolo
        self.image = pygame.image.load('images/spaceships/bgbattleship.png')
        self.image = pygame.transform.scale(self.image, self.settings.ship_size)
        self.rect = self.image.get_rect()
        
        # avvia ogni nuova nave in fondo allo schermo, al centro (posizione iniziale)
        self.rect.midbottom = self.screen_rect.midbottom
        
        # memorizza un float per la posizione orizzontale esatta della nave
        self.x = float(self.rect.x)
        
        # flag del movimento; inizia con una nave che non si muove
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        '''Aggiorna la posizione della nave in base al flag del movimento'''
        # aggiorna il valore x della nave, non il rect()
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # aggiorna l'oggetto rect() da self.x
        self.rect.x = self.x
    
    def blitme(self):
        '''Disegna la nave nella sua posizione corrente'''
        self.screen.blit(self.image, self.rect)