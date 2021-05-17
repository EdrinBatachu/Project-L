import random, json, math, os, pygame

import characters as c
import enemies as e
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

FLOOR = (130, 53, 12)

TILESIZE = 160

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

walls = []

def update_entities(entities, player, dt):
	for i in entities:
		i.update()
		if i.health <= 0:
			entities.remove(i)

	for i in player.entities:
		i.update(dt, entities)

def main():
	player = c.get_champion(0)
	enemy = e.get_enemy(0)
	entities = [enemy]

	r.init(screen, player)

	running = True
	clock = pygame.time.Clock()

	room = f.gen_dungeon()
	f.get_wall_rects(walls, room, TILESIZE)

	pygame.time.set_timer(pygame.USEREVENT, 100)
	millisecond = 0
	while running:
		screen.fill(BLACK)
		dt = clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.USEREVENT:
				player.charge += 1
				if player.charge > 100:
					player.charge = 100

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player.special(player)

				if millisecond >= 10000:
					millisecond = 0
					for i in player.entities:
						i.counter += 1

						if i.counter > i.lifetime:
							player.entities.remove(i)

		update_entities(entities, player, dt)

		player.update(entities)
		movement.move(player, pygame.key.get_pressed(), dt / 60, walls)

		r.draw_room(room, player, screen)
		r.draw_entities(screen, entities, player)
		r.draw_hud(screen, player, int(clock.get_fps()))

		pygame.display.flip()

		millisecond += dt

if __name__ == "__main__":
	main()
