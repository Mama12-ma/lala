import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def game_run():
  # инициализирует pygame, settings и объекты экрана 
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
  pygame.display.set_caption('Alien Invasion')
  # создание коробля
  ship = Ship(ai_settings, screen)
  # Создание группы для хранения пуль
  bullets = Group()

  # запуск основного цикла
  while True:
      gf.check_events(ai_settings, screen, ship, bullets)
      ship.update()
      bullets.update()
      gf.update_screen(ai_settings, screen, ship, bullets)
      bull(ai_settings, screen, ship)
      

game_run()