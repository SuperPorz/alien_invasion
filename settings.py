class Settings:
    '''Una classe per contenere tutte le impostazioni di Alien Invasion'''
    
    def __init__(self):
        '''Inizializza le impostazioni del gioco'''
        
        # screen settings (16:9 netbooks)
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # impostazioni della nave
        self.ship_speed = 1.5 #oss: rect() lavora solo con numeri interi di pixel