import pygame
pygame.init()
from pygame.color import THECOLORS

#------------------------------------------------------
def head1():
    global knopka
    screenX=900
    screenY=620
    backmenu_file= 'Sprites/Backgrounds/backmenu.png'
    name_file= 'Sprites/Buttons/name.png'
    name1_file= 'Sprites/Buttons/name1.png'
    backmenu=pygame.image.load(backmenu_file)
    knopka=pygame.image.load(name_file)
    screen=pygame.display.set_mode([screenX,screenY])
    screen.blit(backmenu, (0,0))
    pygame.display.set_caption('Forest fight')
    run=True
    while run:
        screen.blit(backmenu, (0,0))
        screen.blit(knopka,(252,100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEMOTION:
                (x,y)=pygame.mouse.get_pos()
                if 246<=x<=651 and 110<=y<=274:
                    knopka=pygame.image.load(name1_file)
                else:
                    knopka=pygame.image.load(name_file)
            if event.type==pygame.MOUSEBUTTONDOWN:
                (x1,y1)=pygame.mouse.get_pos()
                if 252<=x1<=648 and 100<=y1<=350:
                    run=False
                    

