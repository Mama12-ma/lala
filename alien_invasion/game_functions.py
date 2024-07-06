import pygame
import sys
from bullet import Bullet

def chek_keydown_events(event, ai_settings, screen, ship, bullets):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = True
  elif event.key == pygame.K_LEFT:
    ship.moving_left = True
  elif event.key == pygame.K_SPACE:
    # создание пули и включение её в группу
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)
  

def chek_keyup_events(event, ship):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  elif event.key == pygame.K_LEFT:
    ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
  """Обробатываем нажатие клавиш и событие мыши"""
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        chek_keydown_events(event, ai_settings, screen, ship, bullets)
      elif event.type == pygame.KEYUP:
        chek_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
  """Обновляет изоброжение на экране и отоброжает новый экран"""
  screen.fill(ai_settings.bg_color)

  for bullet in bullets.sprites():
    bullet.draw_bullet()
  ship.blitme()

  # отоброжение последнего прорисовонного экрана
  pygame.display.flip()