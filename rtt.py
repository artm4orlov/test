import pygame

clock=pygame.time.Clock()

pygame.init()
screen=pygame.display.set_mode((1000,580))
pygame.display.set_caption("Game_over")
#icon= pygame.image.load("")

bg= pygame.image.load("1641212733_53-damion-club-p-foni-dlya-platformerov-56.png").convert_alpha()

walk=[
    pygame.image.load("hj/1670754038.png").convert_alpha(),
    pygame.image.load("hj/1670754040.png").convert_alpha(),
    pygame.image.load("hj/1670754060.png").convert_alpha(),
    pygame.image.load("hj/1670754063.png").convert_alpha(),
]
walk2=[
       pygame.image.load("Новая папка (2)/1670754087.png").convert_alpha(),
       pygame.image.load("Новая папка (2)/1670754090.png").convert_alpha(),
       pygame.image.load("Новая папка (2)/1670754092.png").convert_alpha(),
       pygame.image.load("Новая папка (2)/1670754094.png").convert_alpha(),
]

ghost = pygame.image.load("ghost.png")

ghost_list=[]

anim=0
bt=0


play1=5
play2=150
play3=510

is_jump = False
jump_count = 8


hf=pygame.mixer.Sound("звук/Неизвестен - Веселая музыка для игр и конкурсов.mp3")
hf.play()

ghost_timet=pygame.USEREVENT +1
pygame.time.set_timer(ghost_timet,2500)

label=pygame.font.Font("impact.ttf",40)
lose= label.render("Вы проиграли", False, (193,196,199))
lose1= label.render("Начать сначала", False, (115,132,148))
lose_restart=lose1.get_rect(topleft=(180,200))

bul_left=6
bullet= pygame.image.load("снаряд/bullet (3).png").convert_alpha()
bul=[]

gameplay= True

running= True
while running:

    screen.blit(bg,(bt, 0))
    screen.blit(bg,(bt+1200,0))

    if gameplay:
         player_rect= walk[0].get_rect(topleft=(play2,play3))

         if ghost_list:
             for (i,el) in enumerate(ghost_list):
                 screen.blit(ghost,el)
                 el.x -=10

                 if el.x < - 10:
                     ghost_list.pop(i)


                 if player_rect.colliderect(el):
                     gameplay=False
         ks= pygame.key.get_pressed()
         if ks[pygame.K_LEFT]:
             screen.blit(walk[anim], (play2, play3))
         else:
             screen.blit(walk2[anim], (play2, play3))

         ks=pygame.key.get_pressed()
         if ks[pygame.K_LEFT] and play2 > 50:
             play2 -=play1
         elif ks[pygame.K_RIGHT] and play2 < 200:
             play2 += play1

         if not is_jump:
             if ks[pygame.K_SPACE]:
                 is_jump= True
         else:
             if jump_count >= -8:
                 if jump_count > 0:
                     play3 -=(jump_count **2) / 2
                 else: play3 +=(jump_count **2) / 2
                 jump_count -=1
             else:
                 is_jump = False
                 jump_count = 8


         if bul:
             for (i,el) in  enumerate(bul):
                 screen.blit(bullet, (el.x, el.y))
                 el.x += 4

                 if el.x > 1222:
                     bul.pop(i)

                 if ghost_list:
                     for(index,ghost_el)in enumerate(ghost_list):
                         if el.colliderect(ghost_el):
                             ghost_list.pop(index)
                             bul.pop(i)





         if anim==3:
             anim=0
         else:
             anim+=1
         bt-=2
         if bt == -1200:
             bt=0


    else:
        screen.fill((87,88,89))
        screen.blit(lose,(180,100))

        screen.blit(lose1,lose_restart)

        mouse=pygame.mouse.get_pos()
        if lose_restart.collidepoint(mouse) and pygame.mouse.get_pressed():
            gameplay=True
            play2=150
            ghost_list.clear()
            bul.clear()
            bul_left=6


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
        if event.type== ghost_timet:
            ghost_list.append(ghost.get_rect(topleft=(1002,510)))

        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_w and bul_left>0:
            bul.append(bullet.get_rect(topleft=(play2 +30, play3 +10)))
            bul_left -= 1

    clock.tick(15)






