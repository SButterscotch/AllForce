import pygame
pygame.init()
from Windows.Windows import windows
from Buttons.Buttons import button

Resolution = windows()
Resolution.Native()

w = Resolution.winWidth
h = Resolution.winHeight
win = Resolution.win

start_button = button((150, 150, 150), w/2-w/14, h/4, w/7, h/9, "Start")
character_button = button((150, 150, 150), w/2-w/14, h/2, w/7, h/9, "Characters")
exit_button = button((150, 150, 150), w/2-w/14, h/1.3, w/7, h/9, "Exit")

def reDraw():
    bg = pygame.image.load('lib/darkbg.jpeg')
    win.blit(bg, (0, h/100))
    start_button.draw(win)
    character_button.draw(win)
    exit_button.draw(win)
    pygame.display.update()

def start():
    
    run = True

    while run:
        reDraw()

        for event in pygame.event.get():

            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.isOver(pos):
                    main()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if character_button.isOver(pos):
                    main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.isOver(pos):
                    pygame.quit()
                
            
            if event.type == pygame.MOUSEMOTION:
                if start_button.isOver(pos):
                    start_button.color = (80, 80, 80)
                else:
                    start_button.color = (150, 150, 150)

            if event.type == pygame.MOUSEMOTION:
                if character_button.isOver(pos):
                    character_button.color = (80, 80, 80)
                else:
                    character_button.color = (150, 150, 150)
            
            if event.type == pygame.MOUSEMOTION:
                if exit_button.isOver(pos):
                    exit_button.color = (80, 80, 80)
                else:
                    exit_button.color = (150, 150, 150)
        
        


def main():
    run = True
    
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        win.fill((255, 255, 255))
        pygame.display.update()

start()