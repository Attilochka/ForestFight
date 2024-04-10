import pygame, random,sys
from pygame import *
from pygame.color import THECOLORS
from pygame import font
pygame.font.init()
pygame.init()
def mygame():
    global running,mouseclick1
    screenX=900
    screenY=620
    rep=True
    f1=pygame.font.Font(None,60)
    f100=pygame.font.Font(None,20)
    running=True
    screen=pygame.display.set_mode([screenX, screenY])
    screen1=pygame.display.set_mode([screenX, screenY])
    pole=[[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]
    destroy=False
    knife_file= 'Sprites/knife.png'
    star_file= 'Sprites/star.png'
    heal_file= 'Sprites/heal.png'
    shild_file= 'Sprites/shild.png'
    background_file= 'Sprites/Backgrounds/background.png'
    goblin_file= 'Sprites/Enemy/goblin.png'
    heart_goblin1=pygame.image.load('Sprites/Enemy/heart_gob.png')
    heart_goblin2=pygame.image.load('Sprites/Enemy/heart_gob1.png')
    heart_hero1=pygame.image.load('Sprites/Player/heart_hero1.png')
    heart_hero2=pygame.image.load('Sprites/Player/heart_hero2.png')
    wiin=pygame.image.load('Sprites/Backgrounds/defeat.png')
    win1=pygame.image.load('Sprites/Backgrounds/win1.png')
    end=pygame.image.load('Sprites/Backgrounds/end.png')
    hero1=pygame.image.load('Sprites/Player/hero1.png')
    hero2=pygame.image.load('Sprites/Player/hero2.png')
    hero3=pygame.image.load('Sprites/Player/hero3.png')
    hero4=pygame.image.load('Sprites/Player/hero4.png')
    defeatt=pygame.image.load('Sprites/Backgrounds/win.png')
    goblin=pygame.image.load(goblin_file)
    background=pygame.image.load(background_file)
    star=pygame.image.load(star_file)
    knife=pygame.image.load(knife_file)
    heal=pygame.image.load(heal_file)
    shild=pygame.image.load(shild_file)
    random.seed(version=2)
    goblin_kill=0
    atack_gob=0
    move=0
    move_enemy=False
    heart=0
    hero_end=0
    hpg=1000
    shield=0
    shield_gob=0
    SHIELD=30
    hpe=1800
    DAMAGE=50
    HEAL=30
    size=75
    mouseclick1=False
    mousex=0
    mousey=0
    dx=0
    dy=0
    step=5
    v=570 #x гоблина
    b=275 #y гоблина
    xc=0 #нажатый индекс
    yc=0 #нажатый индекс
    #xh,yh - отпущенный индекс.
    ##---------------------------------------------------------------------------------------------------
    def test(xh,yh,num,xc,yc):
        xcombo=0
        ycombo=0
        pole[xc][yc]=pole[xh][yh]
        #для x
        if xh>0:
            if pole[xh-1][yh]==num:
                xcombo+=1
                if xh>1:
                    if pole[xh-2][yh]==num:
                        xcombo+=1
        if xh<6:
            if pole[xh+1][yh]==num:
                xcombo+=1
                if xh<5:
                    if pole[xh+2][yh]==num:
                        xcombo+=1
        #для y
        if yh>0:
            if pole[xh][yh-1]==num:
                ycombo+=1
                if yh>1:
                    if pole[xh][yh-2]==num:
                        ycombo+=1
        if yh<6:
            if pole[xh][yh+1]==num:
                ycombo+=1
                if yh<5:
                    if pole[xh][yh+2]==num:
                        ycombo+=1
        pole[xc][yc]=num
        if xcombo>1 or ycombo>1:
            return True
        else:
            return False
    ##---------------------------------------------------------------------------------------------------
    def newgen():#оптимизация,юху 
        a=1
        while a!=0:
            pygame.time.delay(60)
            a=0
            i=6;
            while i>=0:
                j=6;
                while j>=0:
                    if pole[i][j]==0:
                        a+=1
                        if j>0:
                            pole[i][j]=pole[i][j-1]
                            pole[i][j-1]=0
                        else:
                            pole[i][j]=random.randint(1,4)
                    j-=1
                i-=1
            if a>0:
                draw()
                pygame.display.flip()
    ##---------------------------------------------------------------------------------------------------

    def goblin_shield():
        nonlocal hpe,shield_gob,goblin,goblin_kill
        print('hjikjf')
        hpe=1500
        goblin=pygame.image.load('Sprites/Enemy/goblin_shield.png')
        shield_gob=30
        goblin_kill=1
            
    ##---------------------------------------------------------------------------------------------------
            
    def goblin_atack():
        nonlocal hpe,hpg,goblin,goblin_kill,atack_gob
        hpe=1300
        goblin=pygame.image.load('Sprites/Enemy/goblin_atack.png')
        atack_gob=random.randint(30,60)
        goblin_kill=2
            
            
        

    ##---------------------------------------------------------------------------------------------------    
    def fiveandseven():
        nonlocal hpe,hpg,DAMAGE,shield,rep
        for i in range(0,7):
            for j in range(0,7):
                left=False
                right=False
                up=False
                down=False
                if i<=4:
                    if pole[i][j]==pole[i+1][j]==pole[i+2][j]:
                        right=True
                if i>=2:
                    if pole[i][j]==pole[i-1][j]==pole[i-2][j]:
                        left=True
                if j<=4:
                    if pole[i][j]==pole[i][j+1]==pole[i][j+2]:
                        down=True
                if j>=2:
                    if pole[i][j]==pole[i][j-1]==pole[i][j-2]:
                        up=True
                if right+left+down+up>=2:
                    rep=True
                    destroy=True
                    if pole[i][j]==1:
                        hpe-=DAMAGE*2-shield_gob
                        goblin_animation_gamage(0)
                    if pole[i][j]==2:
                        hpe-=DAMAGE*2-shield_gob
                        goblin_animation_gamage(1)
                    if pole[i][j]==3:
                        hpg+=HEAL*2.5
                    if pole[i][j]==4:
                        shield+=SHIELD*2.5
                    pole[i][j]=0
                    if right:
                        pole[i+1][j]=0
                        pole[i+2][j]=0
                    if left:
                        pole[i-1][j]=0
                        pole[i-2][j]=0
                    if up:
                        pole[i][j-1]=0
                        pole[i][j-2]=0
                    if down:
                        pole[i][j+1]=0
                        pole[i][j+2]=0
    ##---------------------------------------------------------------------------------------------------
    def four():
        nonlocal hpe,hpg,DAMAGE,shield,rep
        for i in range(0,7):
            for j in range(0,7):
                if i<=3:
                    if pole[i][j]==pole[i+1][j] and pole[i][j]==pole[i+2][j] and pole[i][j]==pole[i+3][j]:
                        destroy=True
                        rep=True
                        print(pole[i][j])
                        if pole[i][j]==1:
                            hpe-=DAMAGE*1.5-shield_gob
                            goblin_animation_gamage(0)
                        if pole[i][j]==2:
                            hpe-=DAMAGE*1.5-shield_gob
                            goblin_animation_gamage(1)
                        if pole[i][j]==3:
                            hpg+=HEAL*2
                        if pole[i][j]==4:
                            shield+=SHIELD*2
                            
                        pole[i][j]=0
                        pole[i+1][j]=0
                        pole[i+2][j]=0
                        pole[i+3][j]=0
                        
                if j<=3:
                    if pole[i][j]==pole[i][j+1] and pole[i][j]==pole[i][j+2] and pole[i][j]==pole[i][j+3]:
                        destroy=True
                        rep=True
                        print(pole[i][j])
                        if pole[i][j]==1:
                            hpe-=DAMAGE*1.5-shield_gob
                            goblin_animation_gamage(0)
                        if pole[i][j]==2:
                            hpe-=DAMAGE*1.5-shield_gob
                        if pole[i][j]==3:
                            hpg+=HEAL*2
                        if pole[i][j]==4:
                            shield+=SHIELD*2
                        pole[i][j]=0
                        pole[i][j+1]=0
                        pole[i][j+2]=0
                        pole[i][j+3]=0
                    
    ##---------------------------------------------------------------------------------------------------
    def tri(mode):#здесь происходит удаление всех три в ряд.
        nonlocal hpe,hpg,DAMAGE,shield,destroy,rep
        for i in range(0,7):
            for j in range(0,7):
                if i<=4:
                    if pole[i][j]==pole[i+1][j] and pole[i][j]==pole[i+2][j]:
                        destroy=True
                        if mode==0:
                            rep=True
                            print(pole[i][j])
                            if pole[i][j]==1:
                                hpe-=DAMAGE-shield_gob
                                goblin_animation_gamage(0)
                            if pole[i][j]==2:
                                hpe-=DAMAGE-shield_gob
                                goblin_animation_gamage(1)
                            if pole[i][j]==3:
                                hpg+=HEAL
                            if pole[i][j]==4:
                                shield+=SHIELD
                        print(hpg,' - hero',hpe,' - enemy')
                        pole[i][j]=0
                        pole[i+1][j]=0
                        pole[i+2][j]=0
                if j<=4:
                    if pole[i][j]==pole[i][j+1] and pole[i][j]==pole[i][j+2]:
                        destroy=True
                        if mode==0:
                            rep=True
                            print(pole[i][j])
                            if pole[i][j]==1:
                                hpe-=DAMAGE-shield_gob
                                goblin_animation_gamage(0)
                            if pole[i][j]==2:
                                hpe-=DAMAGE-shield_gob
                                goblin_animation_gamage(1)
                            if pole[i][j]==3:
                                hpg+=HEAL
                            if pole[i][j]==4:
                                shield+=SHIELD
                        print(hpg,' - hero',hpe,' - enemy')
                        pole[i][j]=0
                        pole[i][j+1]=0
                        pole[i][j+2]=0
            
    ##---------------------------------------------------------------------------------------------------
    def win():
        nonlocal hpe,hpg,hero_end
        if hpe<=0:
            if goblin_kill==0:
                screen.blit(wiin,(0,0))
            if goblin_kill==1:
                screen.blit(win1,(0,0))
            if goblin_kill==2:
                screen.blit(end,(0,0))
                cat_move()
                keyboard()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        gen();
                        shield=0
                        hpg=1000;
                        if goblin_kill==0:
                            goblin_shield()
                        elif goblin_kill==1:
                            goblin_atack()

    def cat_move():
        nonlocal hero_end
        if 0<=hero_end<=3:
            screen.blit(hero1,(420,300))
        elif 4<=hero_end<=7:
            screen.blit(hero3, (420,300))
        elif 8<=hero_end<=11:
            screen.blit(hero4,(420,300))
        elif 12<=hero_end<=15:
            screen.blit(hero2, (420,300))
        hero_end+=1
        if hero_end>15:
            hero_end=0
                    
                    
    ##---------------------------------------------------------------------------------------------------
    def defeat():
        nonlocal hpg
        if hpg<=0:
            hpg=0
        if hpg==0:
            screen.blit(defeatt,(0,0))
            keyboard()
            
    ##--------------------------------------------------------------------------------------------------- 
    def monster():
        nonlocal hpg, shield
        hpm=0
        htx=random.randint(100,400)
        hty=random.randint(100,300)
        shm=0
        stx=random.randint(100,400)
        sty=random.randint(100,300)
        
        print('DAMAGED')
        monster_damage=random.randint(100,180)+atack_gob
        if shield>=monster_damage:
            shield-=monster_damage
            shm=monster_damage
        elif shield>0:
            monster_damage-=shield
            shm=shield
            shield=0
            hpm=monster_damage
            hpg-=monster_damage
        else:
            hpg-=monster_damage
            hpm=monster_damage
        ht=f1.render(str(hpm),True,THECOLORS['red'])
        st=f1.render(str(shm),True,THECOLORS['yellow'])
        atack=[pygame.image.load('Sprites/Enemy/Animation/at1.png'),pygame.image.load('Sprites/Enemy/Animation/at2.png'),
               pygame.image.load('Sprites/Enemy/Animation/at3.png'),pygame.image.load('Sprites/Enemy/Animation/at4.png'),pygame.image.load('Sprites/Enemy/Animation/at5.png')]
        for i in range(5):
            draw()
            screen1.blit(atack[i],(0,0))
            pygame.time.delay(50)
            if hpm>0:
                screen.blit(ht,(htx,hty))
                hty+=20
            if shm>0:
                screen.blit(st,(stx,sty))
                sty+=20
                
            pygame.display.flip()
        shield=0
    
    ##---------------------------------------------------------------------------------------------------
    def gen():#генерация поля.
        a=1
        for i in range(0,7):
            for j in range(0,7):
                pole[i][j]=random.randint(1,4)
        while a!=0:
            tri(1)
            a=0
            for i in range(0,7):
                for j in range(0,7):
                    if pole[i][j]==0:
                        a+=1
                        pole[i][j]=random.randint(1,4)
    ##---------------------------------------------------------------------------------------------------
    def draw():#рисуем поле.
        global xc,yc,mousex,mousey,dx,dy,mouseclick1
        nonlocal v,step,goblin,heart
        bord()
        defeat()
        screen.blit(background,[0,0])        
        for i in range(0,7):
            for j in range(0,7):
                if mouseclick1!=True or i!=xc or j!=yc:
                    if pole[i][j]==1:
                        screen.blit(knife,(i*size+25,j*size+37.5,size,size))
                    if pole[i][j]==2:
                        screen.blit(star,(i*size+25,j*size+37.5,size,size))
                    if pole[i][j]==3:
                        screen.blit(heal, (i*size+25,j*size+37.5,size,size))
                    if pole[i][j]==4:
                        screen.blit(shild,(i*size+25,j*size+37.5,size,size))
        
        if mouseclick1==True:
            if pole[xc][yc]==1:
                screen.blit(knife,(mousex-dx,mousey-dy,size,size))          
            if pole[xc][yc]==2:
                screen.blit(star,(mousex-dx,mousey-dy,size,size))
            if pole[xc][yc]==3:
                screen.blit(heal, (mousex-dx,mousey-dy,size,size))
            if pole[xc][yc]==4:
                screen.blit(shild,(mousex-dx,mousey-dy,size,size))

        herobary=588
        herobarx=20
        
        pygame.draw.rect(screen, (61+177*hpe/2000, 0, 0),(575,20,250*hpe/2000,20),0)
        f0=f100.render(str(hpe),True,THECOLORS["white"])
        screen.blit(f0,[580,22])
        pygame.draw.rect(screen, (61+177*hpg/1000,0, 0), (herobarx,herobary,400*hpg/1000,20),0)
        f0=f100.render(str(hpg),True,THECOLORS["white"])
        screen.blit(f0,[herobarx,herobary+2])

        if shield!=0:
            pygame.draw.rect(screen, (255,204, 0), (herobarx+400*hpg/1000-402*shield/1000,herobary-2,404*shield/1000,24),4)
        v+=step
        screen.blit(goblin,(v,b))
        if (v>=627) or (v<=550):
            step=-step
        if 0<=heart<=3:
            screen.blit(heart_goblin1,(810,8))
            screen.blit(heart_hero1, (440,573))
        elif 4<=heart<=7:
            screen.blit(heart_goblin2,(810,8))
            screen.blit(heart_hero2, (440,573))
        heart+=1
        if heart>7:
            heart=0
        
    ##---------------------------------------------------------------------------------------------------
    def goblin_animation_gamage(mode):
        if mode==0:
            atack_gob=[pygame.image.load('Sprites/Player/Animation/atf1.png'),
                       pygame.image.load('Sprites/Player/Animation/atf2.png'),
                       pygame.image.load('Sprites/Player/Animation/atf3.png'),
                       pygame.image.load('Sprites/Player/Animation/atf4.png'),
                       pygame.image.load('Sprites/Player/Animation/atf5.png')]
            for i in range(5):
                screen1.blit(atack_gob[i],(v,b))
                pygame.time.delay(50)
                pygame.display.flip()
        if mode==1:
            atack_gob_star=[pygame.image.load('Sprites/Player/Animation/ats1.png'),
                            pygame.image.load('Sprites/Player/Animation/ats2.png'),
                            pygame.image.load('Sprites/Player/Animation/ats3.png'),
                            pygame.image.load('Sprites/Player/Animation/ats4.png'),
                            pygame.image.load('Sprites/Player/Animation/ats5.png'),
                            pygame.image.load('Sprites/Player/Animation/ats6.png'),
                            pygame.image.load('Sprites/Player/Animation/ats7.png'),
                            pygame.image.load('Sprites/Player/Animation/ats8.png')]
            for i in range(8):
                draw()
                screen1.blit(atack_gob_star[i],(v,b))
                pygame.time.delay(40)
                pygame.display.flip()
    ##---------------------------------------------------------------------------------------------------
        
    def keyboard():
        global mouseclick1,xc,yc,running,mousex,mousey,dx,dy
        nonlocal move,move_enemy
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                (x,y)=pygame.mouse.get_pos()
                for i in range(0,7):
                    for j in range(0,7):
                        if i*size+25 < x < i*size+size+25 and j*size+37.5 < y < j*size+size+37.5:
                            xc=i
                            yc=j
                            dx=x-xc*size-25
                            dy=y-yc*size-37.5
                            mouseclick1=True
            if event.type==pygame.MOUSEBUTTONUP:
                (x,y)=pygame.mouse.get_pos()
                if mouseclick1==True:
                    mouseclick1=False
                    for i in range(0,7):
                        for j in range(0,7):
                            if i*size+25 < x < i*size+size+25 and j*size+37.5 < y < j*size+size+37.5:
                                xh=i
                                yh=j
                                if abs(xc-xh)+abs(yc-yh)==1:
                                    if test(xh,yh,pole[xc][yc],xc,yc)or test(xc,yc,pole[xh][yh],xh,yh):                                                                                                                                       
                                        a=pole[xc][yc]
                                        pole[xc][yc]=pole[xh][yh]
                                        pole[xh][yh]=a
                                        move+=1
                                        move_enemy=True
            if event.type==pygame.MOUSEMOTION:
                (x,y)=pygame.mouse.get_pos()
                mousex=x
                mousey=y
    ##---------------------------------------------------------------------------------------------------
    def bord():
        nonlocal hpg
        if hpg>1000:
            hpg=1000
    ##---------------------------------------------------------------------------------------------------
    gen()
    while running:
        pygame.time.delay(30)
        if hpe>0 and hpg>0:
            draw()
            keyboard()
            rep=True
            while rep:
                rep=False
                fiveandseven()
                four()
                tri(0)
                if destroy==True:
                    newgen()
                    destroy=False
            if move%2==0 and move_enemy==True:
                monster()
                move_enemy=False
        win()
        defeat()
        pygame.display.flip()

