import pygame
import random
import sys
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (255,0,0)

#bit.ly/2k6F6zL
ball_image = pygame.image.load("ball-6x6 (1).png")
ball_image = pygame.transform.smoothscale(ball_image, (30, 30))
ball_rect = ball_image.get_rect()
ball_rect.center = (width//2, height//2)
speed = pygame.math.Vector2(0, 5)
speed.rotate_ip(random.randint(0, 360))


def move_ball():
    ball_rect.move_ip(speed)
    screen_info = pygame.display.Info()
    if ball_rect.left < 0 or ball_rect.right > screen_info.current_w:
        speed[0] *= -1
        ball_rect.move_ip(speed[0], 0)
    if ball_rect.top < 0 or ball_rect.bottom > screen_info.current_h:
        speed[1] *= -1
        ball_rect.move_ip(0, speed[1])


#at the very top write --> import sys
def main():

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        move_ball()
        screen.fill(color)
        screen.blit(ball_image, ball_rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()


