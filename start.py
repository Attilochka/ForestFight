import pygame,mainMenu,game,helpMenu
import myhead
from pygame.color import THECOLORS
pygame.init()

myhead.head1()
pygame.display.set_caption('Forest fight')
open_m=True
running=True
a=0
while running:
    if open_m==True:
        a=mainMenu.menu()
    if a=='game':
        open_m=False
        game.mygame()
        open_m=True
    if a=='exit':
        running=False
    if a=='help':
        open_m=False
        helpMenu.myhelp()
        open_m=True
        
pygame.quit()
