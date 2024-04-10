import pygame
pygame.init()
screenX=900
screenY=620
def myhelp():
    screen=pygame.display.set_mode([screenX,screenY])
    helpmenu1=pygame.image.load('Sprites/Backgrounds/helpmenut1.png')
    helpmenu2=pygame.image.load('Sprites/Backgrounds/helpmenut2.png')
    helpmenu3=pygame.image.load('Sprites/Backgrounds/helpmenut3.png')
    helpmenu4=pygame.image.load('Sprites/Backgrounds/helpmenut4.png')
    knop1=pygame.image.load('Sprites/Buttons/helpknop1.png')
    knop2=pygame.image.load('Sprites/Buttons/helpknop2.png')
    knop3=pygame.image.load('Sprites/Buttons/helpknop3.png')
    knop4=pygame.image.load('Sprites/Buttons/helpknop4.png')
    escape=pygame.image.load('Sprites/Buttons/esc.png')
    main_help = helpmenu1
    xknop=770
    yknop=120
    running=True
    while running:
        screen.blit(main_help, (0, 0))
        screen.blit(escape,(10,10))
        screen.blit(knop1,(xknop,yknop))
        screen.blit(knop2,(xknop,yknop+110))
        screen.blit(knop3,(xknop,yknop+220))
        screen.blit(knop4,(xknop,yknop+330))
        for event in pygame.event.get():
            (x,y)=pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if xknop<=x<=xknop+50 and yknop<=y<=yknop+52:
                    main_help = helpmenu1
                elif xknop<=x<=xknop+50 and yknop+110<=y<=yknop+162:
                    main_help = helpmenu2
                elif xknop<=x<=xknop+50 and yknop+220<=y<=yknop+272:
                    main_help = helpmenu3
                elif xknop<=x<=xknop+50 and yknop+330<=y<=yknop+382:
                    main_help = helpmenu4
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
        pygame.display.flip()


