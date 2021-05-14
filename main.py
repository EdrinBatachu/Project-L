import random, json, math, os, pygame

import characters as c
import specials as s
import render as r
import floor_generation as f
import movement

WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
HUD = (50, 50, 50)
MAGIC_BLUE = (50, 150, 255)
DAMAGE_ORANGE = (250, 50, 50)

pygame.init()


def main():

	player = c.get_champion(1)

	enemies = []

	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	running = True
	clock = pygame.time.Clock()
	while running:
		screen.fill(BLACK)
		dt = clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		movement.move(player, pygame.key.get_pressed(), dt / 25)
		r.draw_enemies(screen, enemies)
		r.draw_playermodel(screen, player)
		r.draw_hud(screen, player, int(clock.get_fps()))
		pygame.display.flip()

if __name__ == "__main__":
	main()
