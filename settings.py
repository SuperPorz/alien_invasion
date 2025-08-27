class Settings:
    '''Una classe per contenere tutte le impostazioni di Alien Invasion'''
    
    def __init__(self):
        '''Inizializza le impostazioni del gioco'''
        
        # screen settings (16:9 netbooks)
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.bullets_allowed = 3 #max 3 proiettili nella schermata
        
        # impostazioni della nave
        self.ship_speed = 3.5 #oss: rect() lavora solo con numeri interi di pixel
        
        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_heigth = 15
        self.bullet_color = (60, 60, 60)