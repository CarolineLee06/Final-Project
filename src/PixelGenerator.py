import random
import pygame

class particle():
    pass 


class pixelart():
    pass 



def main():
    print('In Main')
    pygame.init()
    pygame.display.set_caption("Digital Rain")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    display_info = pygame.display.Info()
    screen_resolution = (display_info.current_w, display_info.current_h)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE, pygame.FULLSCREEN)
    rain = Rain(screen_resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        rain.update(dt)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        rain.draw(screen)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()

if __name__ == "__main__":
   main()