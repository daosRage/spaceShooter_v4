import pygame
from data import *
from shooter import *
from random import randint

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("Shooter")

def run():
    game = True
    time_start = 0
    time_end = 0
    which_window = 0

    hero = Hero(700, 100, 176, 128, speed= 5, color= (23,114, 9), image= hero_images)
    bg = BackGround(bg_image, 0.5)
    boss = None
    font_kill = pygame.font.Font(None, 40)
    #bot = Bot(500, 0 - 48, 50,50, speed= 1, image= bot_images)
    clock = pygame.time.Clock()

    while game:
        events = pygame.event.get()
        bg.move(window)
        
        if which_window == 0:

            x = 10
            for hp in range(hero.HP):
                window.blit(HP_image, (x, 10))
                x += 47

            #HERO
            hero.move(window)
            hero.move_bullet(window, boss)
            window.blit(font_kill.render(
                f"SCORE: {hero.KILL}", True, (0, 0, 0)), (setting_win["WIDTH"] - 180, 10))


            #BOT
            time_end = pygame.time.get_ticks()
            if time_end - time_start > 2000 and hero.KILL_BOT_LVL < 3:
                bot_list.append(Bot(randint(0, setting_win["WIDTH"] - setting_bot["WIDTH"]), 
                                    0 - setting_bot["HEIGHT"], 
                                    setting_bot["WIDTH"], 
                                    setting_bot["HEIGHT"], 
                                    speed= 1, image= bot_images))
                time_start = time_end

            for bot in bot_list:
                bot.move(window)
                bot.move_bullet(window, hero)

            #BOSS
            if hero.KILL_BOT_LVL >= 3:
                if not boss:
                    boss = Boss(setting_win["WIDTH"] // 2 - setting_boss["WIDTH"] // 2,
                                - setting_boss["HEIGHT"],
                                setting_boss["WIDTH"],
                                setting_boss["HEIGHT"],
                                image= boss_images,
                                speed= 1)
                if boss.HP > 0:  
                    boss.move(window)
                else:
                    hero.KILL_BOT_LVL = 0
                    boss = None
                    hero.KILL_BOSS += 1
                    if hero.KILL_BOSS == 2:
                        hero.KILL_BOSS = 0
                        lvl.LVL += 1
                        lvl.next_level(window)
                        which_window = 1
                        time_start = pygame.time.get_ticks()

            for bullet in bullet_boss_list:
                bullet.move_boss(window, hero= hero, bullet= bullet)

            #EVENT
            for event in events:
               
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        hero.MOVE["UP"] = True
                    if event.key == pygame.K_s:
                        hero.MOVE["DOWN"] = True
                    if event.key == pygame.K_a:
                        hero.MOVE["LEFT"] = True
                    if event.key == pygame.K_d:
                        hero.MOVE["RIGHT"] = True
                    if event.key == pygame.K_SPACE:
                        hero.BULLETS.append(Bullet(bullet_image, 8, x= hero.x + hero.width // 2 - 27, y= hero.y, width= 10, height= 20))
                        hero.BULLETS.append(Bullet(bullet_image, 8, x= hero.x + hero.width // 2 + 18, y= hero.y, width= 10, height= 20))
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        hero.MOVE["UP"] = False
                    if event.key == pygame.K_s:
                        hero.MOVE["DOWN"] = False
                    if event.key == pygame.K_a:
                        hero.MOVE["LEFT"] = False
                    if event.key == pygame.K_d:
                        hero.MOVE["RIGHT"] = False
        
        elif which_window == 1:
            pass



        for event in events:
            if event.type == pygame.QUIT:
                game = False
        clock.tick(60)
        pygame.display.flip()

run()