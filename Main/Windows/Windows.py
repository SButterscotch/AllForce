import pygame

class windows():
    winWidth = 0
    winHeight = 0
    win = None

    def Large(self):
        self.winWidth = 1360
        self.winHeight = 700
        self.win = pygame.display.set_mode((self.winWidth, self.winHeight))
        pygame.display.set_caption("AllForce")
    
    def Native(self):
        self.winWidth = 800
        self.winHeight = 600
        self.win = pygame.display.set_mode((self.winWidth, self.winHeight))
        pygame.display.set_caption("AllForce")
    
    def Small(self):
        self.winWidth = 400
        self.winHeight = 300
        self.win = pygame.display.set_mode((self.winWidth, self.winHeight))
        pygame.display.set_caption("AllForce")
