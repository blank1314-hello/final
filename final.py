def complete():
    import pygame
    import random
    
    pygame.init()
    window_width = 800
    window_height = 600
    score = 5
    add = 0
    running = True
    mouse_speed = 5
    cat_speed = 10
    GREEN = (0,255,0)
    BLACK = (0,0,0)
    cat_dx = cat_speed
    cat_dy = cat_speed
    display_surface = pygame.display.set_mode((window_width,window_height))
    title = pygame.display.set_caption("restart")

    clock = pygame.time.Clock()
    
    mouse_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\mouse.png")
    mouse_rect = mouse_image.get_rect()
    mouse_rect.centerx = (window_width//2)
    mouse_rect.bottom = (window_height//1)
    
    cat_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\cat.png")
    cat_rect = cat_image.get_rect()
    cat_rect.centerx = (window_width//2)
    cat_rect.bottom = (window_height//3)

    banana_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\banana.png")
    banana_rect = banana_image.get_rect()
    banana_rect.centerx = (window_width//2)
    banana_rect.bottom = (window_height//2)

    system_font = pygame.font.SysFont('verdanai',30)
    game_score = system_font.render("Live:"+str(score),True,GREEN,BLACK)
    game_score_rect = game_score.get_rect()
    game_score_rect.topleft = (10,10)

    system_font2 = pygame.font.SysFont('verdanai',30)
    game_live = system_font2.render("Score:"+str(add),True,GREEN,BLACK)
    game_live_rect = game_live.get_rect()
    game_live_rect.topleft = (10,40)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and mouse_rect.top > 0:
            mouse_rect.y -=mouse_speed
        if keys[pygame.K_s] and mouse_rect.bottom < window_height:
            mouse_rect.y +=mouse_speed
        if keys[pygame.K_a] and mouse_rect.left > 0:
            mouse_rect.x -=mouse_speed
        if keys[pygame.K_d] and mouse_rect.right < window_width:
            mouse_rect.x +=mouse_speed
        if mouse_rect.colliderect(cat_rect):
            print("충돌")
            score = score - 1
            cat_rect.x = random.randint(0,window_width-50)
            cat_rect.y = random.randint(0,window_height -50)
        if mouse_rect.colliderect(banana_rect):
            print("득점")
            add = add + 1
            banana_rect.x = random.randint(0,window_width  -50)
            banana_rect.y = random.randint(0,window_height -50)
        cat_rect.x = cat_rect.x + cat_dx
        cat_rect.y = cat_rect.y + cat_dy
        if (cat_rect.x) > window_width or cat_rect.x < 0 :
            cat_dx = cat_dx * -1
        if (cat_rect.y) > window_height or cat_rect.y < 0 :
            cat_dy = cat_dy * -1
        if score != 0:
            game_score = system_font.render("Live:"+str(score),True,GREEN,BLACK)
        if score == 0:
            game_score = system_font.render("GAME OVER",True,GREEN,BLACK)
            print("GAME OVER")
            h = input("enter키를 눌러서 게임을 종료하세요")
            if h == 'continue':
                complete()
            if h == "":
                restart()
        if add != 15:
            game_live = system_font2.render("Score:"+str(add),True,GREEN,BLACK)
        if add == 15:
            game_live = system_font2.render("GAME WIN",True,GREEN,BLACK)
            print("GAME WIN")
            h = input("enter키를 눌러서 게임을 종료하세요")
            if h == "":
                restart
        display_surface.fill((0,0,0))

        display_surface.blit(mouse_image,mouse_rect)
        display_surface.blit(cat_image,cat_rect)
        display_surface.blit(banana_image,banana_rect)
        #텍스트 표시
        display_surface.blit(game_score,game_score_rect)
        display_surface.blit(game_live,game_live_rect)
        pygame.display.update()
        clock.tick(60)
    restart()

def gun():
    import pygame
    import random

    pygame.init()

    windows_width = 900
    windows_height = 600

    mouse_speed = 7
    fire_speed = 50
    fire2_speed = 75
    fire3_speed = 100
    cat_speed = 13
    banana_speed = 10

    count = 1

    LIVE = 10
    SCORE = 0
    GREEN = (0, 255, 0)
    WHITE = (200, 200, 200)

    fire_visible = False
    running = True
    moving = False
    last_move_time = 0
    move_interval = 100

    display_surface = pygame.display.set_mode((windows_width, windows_height))
    pygame.display.set_caption("Throw fire")

    clock = pygame.time.Clock()

    mouse_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\gun.png")
    mouse_rect = mouse_image.get_rect(center=(25, 300))

    fire_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\fire.png")
    fire_rect = fire_image.get_rect()
    fire_rect.centerx = 1000
    fire_rect.bottom = 1000

    fire2_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\fire2.png")
    fire2_rect = fire2_image.get_rect()
    fire2_rect.centerx = 1000
    fire2_rect.bottom = 1000

    fire3_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\fire3.png")
    fire3_rect = fire3_image.get_rect()
    fire3_rect.centerx = 1000
    fire3_rect.bottom = 1000

    cat_image = pygame.image.load("C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\cat.png")
    cat_rect = cat_image.get_rect(center=(850, random.randint(0, windows_height)))

    banana_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\banana.png")
    banana_rect = banana_image.get_rect(center=(850, random.randint(0, windows_height)))

    system_font = pygame.font.SysFont('verdanai', 30)
    game_live = system_font.render("LIVE:" + str(LIVE), True, GREEN, WHITE)
    game_live_rect = game_live.get_rect(topleft=(10, 10))

    system_font2 = pygame.font.SysFont('verdanai', 30)
    game_score = system_font2.render("SCORE:" + str(SCORE), True, GREEN, WHITE)
    game_score_rect = game_score.get_rect(topleft=(10, 40))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and mouse_rect.top > 0:
            mouse_rect.y -= mouse_speed
        if keys[pygame.K_s] and mouse_rect.bottom < windows_height:
            mouse_rect.y += mouse_speed

        if keys[pygame.K_SPACE]:
            if not moving:
                moving = True
                fire_rect.centerx = mouse_rect.centerx
                fire_rect.bottom = mouse_rect.bottom

                fire2_rect.centerx = mouse_rect.centerx
                fire2_rect.bottom = mouse_rect.bottom

                fire3_rect.centerx = mouse_rect.centerx
                fire3_rect.bottom = mouse_rect.bottom

                last_move_time = pygame.time.get_ticks()

        cat_rect.x -= cat_speed
        banana_rect.x -= banana_speed
        if count < 0:
            count = 1

        if moving:
            fire_visible = True
            current_time = pygame.time.get_ticks()

            if current_time - last_move_time >= move_interval and count == 1:
                fire_rect.x += fire_speed 
                last_move_time = current_time 

                if fire_rect.x > windows_width:
                    moving = False
                    fire_visible = False
                    fire_rect.centerx = 1000
                    fire_rect.bottom = 1000

            if current_time - last_move_time >= move_interval and count == 2:
                fire2_rect.x += fire2_speed
                last_move_time = current_time

                if fire2_rect.x > windows_width:
                    moving = False
                    fire_visible = False
                    fire2_rect.centerx = 1000
                    fire2_rect.bottom = 1000

            if current_time - last_move_time >= move_interval and count >= 3:
                fire3_rect.x += fire3_speed
                last_move_time = current_time

                if fire3_rect.x > windows_width:
                    moving = False
                    fire_visible = False
                    fire3_rect.centerx = 1000
                    fire3_rect.bottom = 1000

        if SCORE == 15:
            game_score = system_font2.render("GAME WIN", True, GREEN, WHITE)
            print("GAME WIN")
            h = input("Do you want to play more? if you want press 'y' or not want press 'n'")
            if h == 'y':
                gun()
            else:
                restart()
        else:
            game_score = system_font2.render("SCORE:" + str(SCORE), True, GREEN, WHITE)
        
        if LIVE == 0:
            game_live = system_font.render("GAME LOSE", True, GREEN, WHITE)
            print("GAME LOSE")
            h = input("Do you want to play more? if you want press 'y' or not want press 'n'")
            if h == 'y':
                gun()
            else:
                restart()
        else:
            game_live = system_font.render("LIVE:" + str(LIVE), True, GREEN, WHITE)

        if cat_rect.colliderect(mouse_rect) or cat_rect.x < 0:
            LIVE -= 1
            print("실점:"+str(LIVE))
            cat_rect.x = 850
            cat_rect.y = random.randint(0, windows_height)
        
        if mouse_rect.colliderect(banana_rect):
            print("아이템:"+str(count))
            count = count + 1
            banana_rect.x = 850
            banana_rect.y = random.randint(0, windows_height)


        if cat_rect.colliderect(fire_rect):
            SCORE += 1
            print("score:"+str(SCORE))
            moving = False
            fire_visible = False
            cat_rect.x = 850
            cat_rect.y = random.randint(0, windows_height)
            fire_rect.centerx = 1000
            fire_rect.bottom = 1000

        if cat_rect.colliderect(fire2_rect):
            SCORE += 1
            print("score:"+str(SCORE))
            moving = False
            fire_visible = False
            cat_rect.x = 850
            cat_rect.y = random.randint(0, windows_height)
            fire2_rect.centerx = 1000
            fire2_rect.bottom = 1000

        if cat_rect.colliderect(fire3_rect):
            SCORE += 1
            print("score:"+str(SCORE))
            moving = False
            fire_visible = False
            cat_rect.x = 850
            cat_rect.y = random.randint(0, windows_height)
            fire3_rect.centerx = 1000
            fire3_rect.bottom = 1000

        if banana_rect.x < 0:
            count = count - 1
            print("아이템:"+str(count))
            banana_rect.x = 850
            banana_rect.y = random.randint(0, windows_height)
            fire_rect.centerx = 1000
            fire_rect.bottom = 1000

            fire2_rect.centerx = 1000
            fire2_rect.bottom = 1000
            
            fire3_rect.centerx = 1000
            fire3_rect.bottom = 1000        

        display_surface.fill(WHITE)
        if fire_visible and count == 1:
            display_surface.blit(fire_image, fire_rect)
            fire2_rect.centerx = 1000
            fire2_rect.bottom = 1000
            fire3_rect.centerx = 1000
            fire3_rect.bottom = 1000
        if fire_visible and count == 2:
            display_surface.blit(fire2_image,fire2_rect)
            fire_rect.centerx = 1000
            fire_rect.bottom = 1000
            fire3_rect.centerx = 1000
            fire3_rect.bottom = 1000
        if fire_visible and count >=  3:
            display_surface.blit(fire3_image,fire3_rect)
            fire_rect.centerx = 1000
            fire_rect.bottom = 1000
            fire2_rect.centerx = 1000
            fire2_rect.bottom = 1000
        display_surface.blit(mouse_image, mouse_rect)
        display_surface.blit(cat_image, cat_rect)
        display_surface.blit(banana_image,banana_rect)

        game_score = system_font2.render("SCORE:" + str(SCORE), True, GREEN, WHITE)
        game_live = system_font.render("LIVE:" + str(LIVE), True, GREEN, WHITE)
        display_surface.blit(game_score, game_score_rect)
        display_surface.blit(game_live, game_live_rect)

        pygame.display.update()
        clock.tick(60)

def hello():
    import pygame
    import random
    
    pygame.init()
    windows_width = 600
    windows_height = 700
    score = 0
    live = 5
    cat_dy = 10
    banana_dy = 10
    GREEN = (0,255,0)
    BLACK = (0,0,0)
    display_surface = pygame.display.set_mode((windows_width,windows_height))
    pygame.display.set_caption("newgoal")
    clock = pygame.time.Clock()

    mouse_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\mouse.png")
    mouse_rect = mouse_image.get_rect()
    mouse_rect.centerx = (windows_width//2)
    mouse_rect.bottom = (windows_height//1)

    cat_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\cat.png")
    cat_rect = cat_image.get_rect()
    cat_rect.centerx = (windows_width//2)
    cat_rect.bottom = (windows_height//1)

    banana_image = pygame.image.load(r"C:\Users\Administrator\Downloads\shooting-game-main\shooting-game-main\image\banana.png")
    banana_rect = banana_image.get_rect()
    banana_rect.centerx = (windows_width//2)
    banana_rect.bottom = (windows_height//5)

    system_font = pygame.font.SysFont('verdanai',30)
    game_score = system_font.render("Score:"+str(score),True,GREEN,BLACK)
    game_score_rect = game_score.get_rect()
    game_score_rect.topleft = (10,10)

    system_font2 = pygame.font.SysFont('verdanai',30)
    game_live = system_font2.render("Live:"+str(live),True,GREEN,BLACK)
    game_live_rect = game_live.get_rect()
    game_live_rect.topleft = (10,40)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and mouse_rect.left > 0:
            mouse_rect.x -=5
        if keys[pygame.K_d] and mouse_rect.right < windows_width:
            mouse_rect.x +=5
        cat_rect.y = cat_rect.y + cat_dy
        banana_rect.y = banana_rect.y + banana_dy
        if mouse_rect.colliderect(cat_rect):
            live = live - 1
            cat_rect.bottom = (windows_height//6)
            cat_rect.centerx = random.randint(0,windows_width-50)

        if mouse_rect.colliderect(banana_rect):
            score = score + 1
            banana_rect.bottom = (windows_height//6)
            banana_rect.centerx = random.randint(0,windows_width-50)
            
        if cat_rect.bottom > 700:
            cat_rect.bottom = (windows_height//6)
            cat_rect.centerx = random.randint(0,windows_width-50)

        if banana_rect.bottom > 700:
            score = score - 1
            banana_rect.bottom = (windows_height//6)
            banana_rect.centerx = random.randint(0,windows_width-50)

        if score == 15:
            game_score = system_font.render("GAME WIN",True,GREEN,BLACK)
            print("GAME WIN")
            h = input("enter키를 눌러서 종료하십시오")
            if h == "":
                restart()
            if h == 'continue':
                hello()
        else:
            game_score = system_font.render("Scores:"+str(score),True,GREEN,BLACK)
        if live == 0:
            game_live =  system_font2.render("GAME LOSE",True,GREEN,BLACK)
            print("GAME LOSE")
            h = input("enter키를 눌러서 종료하십시오")
            if h == "":
                restart()
            if h == 'continue':
                hello()
        else:
            game_live = system_font2.render("Lives:"+str(live),True,GREEN,BLACK)
        pygame.display.update()
        
        display_surface.fill((0,0,0))
        display_surface.blit(mouse_image,mouse_rect)
        display_surface.blit(cat_image,cat_rect)
        display_surface.blit(game_score,game_score_rect)
        display_surface.blit(game_live,game_live_rect)
        display_surface.blit(banana_image,banana_rect)
        clock.tick(60)
    pygame.quit()
def restart():
    import pygame
    pygame.init()
    clock = pygame.time.Clock()
    windows_width = 600
    windows_height = 700
    display_surface = pygame.display.set_mode((windows_width,windows_height))
    pygame.display.set_caption("start space")
    running = True
    print("press the 'a'and click then the first game will start")
    print("press the 'b'and click then the secend game will start")
    print("press the 'c'and click then the third game will start")
    print("if you want to close the game press the 'q' and click")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and event.type == pygame.MOUSEBUTTONDOWN:
                hello()
            if keys[pygame.K_b] and event.type == pygame.MOUSEBUTTONDOWN:
                complete()
            if keys[pygame.K_c] and event.type == pygame.MOUSEBUTTONDOWN:
                gun()
            if keys[pygame.K_q] and event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        display_surface.fill((0,0,0))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
restart()
