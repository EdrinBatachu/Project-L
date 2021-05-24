import random, json, math, os, pygame

import characters as c
import enemies as e
import specials as s
import render as r
import floor_generation as f
import main_menu
import movement
import math
import sys

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

def calculate_damage_mod(caster, receiver, typee):
	if typee == "armour":
		mod = 100 / (100 + (receiver.armour * receiver.armour_mod))
	elif typee == "magic":
		mod = 100 / (100 + (receiver.magic_resist * receiver.magic_resist_mod))
	else:
		mod = 1
	return mod


def update_entities(entities, player, dt):
	for i in entities:
		i.update(player)
		if i.health <= 0:
			entities.remove(i)

	for i in player.entities:
		i.update(dt, entities)

def update_animations(player):
	for i in player.animations:
		i.update(player.animations)


def main():
	running = True
	clock = pygame.time.Clock()

	champ_index = main_menu.main_menu(screen)
	entities = []
	player = c.get_champion(champ_index)
	num = 0
	for i in range(10):
		if i == 10:
			num += 1
		entities.append(e.get_enemy(num, player))

	r.init(screen, player)

	width = (screen.get_width() / 2) - (player.surf.get_width() / 2) 
	height = (screen.get_height() / 2) - (player.surf.get_height() / 2) - (75)

	room = f.gen_dungeon()
	f.get_wall_rects(walls, room, TILESIZE)

	pygame.time.set_timer(pygame.USEREVENT, 100)
	millisecond = 0

	while running:
		screen.fill(BLACK)
		dt = clock.tick(60)
		mousepos = list(pygame.mouse.get_pos())
		mousepos[0] += player.position[0] - width
		mousepos[1] += player.position[1] - height

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.USEREVENT:
				player.charge += 1
				if player.charge > 100:
					player.charge = 100

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					player.special(player)
				if event.key == pygame.K_e:
					player.health -= 10
				if event.key == pygame.K_SPACE:
					player.auto()

				if millisecond >= 10000:
					millisecond = 0
					for i in player.entities:
						i.counter += 1

						if i.counter > i.lifetime:
							player.entities.remove(i)

		update_animations(player)
		update_entities(entities, player, dt)
		player.update(entities, mousepos)
		movement.move(player, pygame.key.get_pressed(), dt / 60, walls)
		movement.move_enemy(entities, walls, dt / 60)
		r.draw_room(room, player, screen)
		r.draw_entities(screen, entities, player)
		r.draw_animations(screen, player)
		r.draw_hud(screen, player, int(clock.get_fps()), mousepos)

		pygame.display.flip()

		millisecond += dt

if __name__ == "__main__":
	main()
	pygame.quit()
	sys.exit()