import pygame
import os

setting_win = {
    "WIDTH": 800,
    "HEIGHT": 600
}
setting_bot = {
    "WIDTH": 75,
    "HEIGHT": 85
}

bot_list = list()

abs_path = os.path.abspath(__file__ + "/..") + "\\image\\"
bot_images = [pygame.transform.scale(pygame.image.load(abs_path + "bot_1_1.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"])), 
              pygame.transform.scale(pygame.image.load(abs_path + "bot_1_2.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"]))]
hero_images = [pygame.transform.scale(pygame.image.load(abs_path + "hero_fly_1.png"), (176, 128)), 
              pygame.transform.scale(pygame.image.load(abs_path + "hero_fly_2.png"), (176, 128))]
bullet_image = pygame.image.load(abs_path + "bullet.png")
