import pygame

class button():
    def __init__(self, color, x,y,w,h, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

    def draw(self,win):
        #Call this method to draw the button on the screen
        
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.w,self.h))
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', int(self.w/6))
            text = font.render(self.text, 1,  (0,0,0))
            win.blit(text, (self.x + (self.w/2 - text.get_width()/2), self.y + (self.h/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.w:
            if pos[1] > self.y and pos[1] < self.y + self.h:
                return True
            
        return False
    
