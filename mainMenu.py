import pygame
pygame.init()
def menu():
    screenX=900
    screenY=620
    screen=pygame.display.set_mode([screenX,screenY])
    a=0
    running=True
    backmenu_file= 'Sprites/Backgrounds/backmenu.png'
    name_file= 'Sprites/Buttons/name.png'
    help_file= 'Sprites/Buttons/help.png'
    help2_file= 'Sprites/Buttons/help2.png'
    exit_file= 'Sprites/Buttons/exit.png'
    exit2_file= 'Sprites/Buttons/exit2.png'
    play1_file= 'Sprites/Player/play1.png'
    play_file= 'Sprites/Player/play.png'
    exit1=pygame.image.load(exit_file)
    help1=pygame.image.load(help_file)
    play=pygame.image.load(play_file)

    backmenu=pygame.image.load(backmenu_file)
    name=pygame.image.load(name_file)
    screen=pygame.display.set_mode([screenX,screenY])
    pygame.display.set_caption('Forest fight')
    
    while running:
        screen.blit(backmenu, (0,0))
        screen.blit(play,(310,200))
        screen.blit(name,(252,25))
        screen.blit(play, (310,200) )
        screen.blit(help1, (310,315) )
        screen.blit(exit1, (310,430) )
        pygame.display.flip()
        for event in pygame.event.get():
            (x,y)=pygame.mouse.get_pos()
            if event.type==pygame.MOUSEMOTION:
                if 350<=x<=566 and 209<=y<=313:
                    play=pygame.image.load(play1_file)
                else:
                    play=pygame.image.load(play_file)
                if 350<=x<=566 and 324<=y<=428:
                    help1=pygame.image.load(help2_file)
                else:
                    help1=pygame.image.load(help_file)
                if 350<=x<=566 and 439<=y<=543:
                    exit1=pygame.image.load(exit2_file)
                else:
                    exit1=pygame.image.load(exit_file)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if 350<=x<=566 and 200<=y<=300:
                    a='game'
                    running=False
                if 350<=x<=566 and 315<=y<=415:
                    a='help'
                    running=False
                if 350<=x<=566 and 430<=y<=530:
                    a='exit'
                    running=False
        pygame.display.flip()
    return(a)
