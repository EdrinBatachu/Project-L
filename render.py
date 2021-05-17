import pygame
from main import HUD, BLACK, RED, GREEN, MAGIC_BLUE, DAMAGE_ORANGE, WHITE, TILESIZE, FLOOR

def get_sprites(name):
	images = []
	sprite_types = ("icon", "up", "down", "left", "right")
	for i in sprite_types:
		img = pygame.image.load("data/sprites/%s/idle/%s_%s" % (name, name, i))
		images.append(img)
	return images


floor_surf = pygame.Surface((TILESIZE, TILESIZE))
floor_surf.fill(FLOOR)
wall_surf = pygame.Surface((TILESIZE, TILESIZE))
wall_surf.fill(HUD)
door_surf = pygame.Surface((TILESIZE, TILESIZE))
door_surf.fill(WHITE)

width, height = 0, 0
def init(screen, player):
	global width, height
	width = (screen.get_width() / 2) - (player.surf.get_width() / 2) 
	height = (screen.get_height() / 2) - (player.surf.get_height() / 2) - (75)


def draw_damage(damage, dmg_type, position):
	font = pygame.font.SysFont("Roboto Mono", 28)
	if dmg_type == "magic":
		text = font.render(str(int(damage)), True, MAGIC_BLUE)
	elif dmg_type == "attack":
		text = font.render(str(int(damage)), True, DAMAGE_ORANGE)

	return text



def draw_room(room, player, screen):
	x = 0
	for i in room:
		y = 0
		for j in i:
			if room[x][y] == ".":
				screen.blit(floor_surf, ((x * TILESIZE) -player.position[0] + width, (y * TILESIZE)- player.position[1]+ height))
			elif room[x][y] == "#":
				screen.blit(wall_surf, ((x * TILESIZE)- player.position[0]+ width, (y * TILESIZE)- player.position[1]+ height))
			elif room[x][y] == "X":
				screen.blit(door_surf, ((x * TILESIZE)- player.position[0]+ width, (y * TILESIZE)- player.position[1]+ height))
			y += 1
		x += 1 



def draw_entities(screen, entities, player):
	for enemy in entities:
		screen.blit(enemy.surf, (enemy.position[0] - player.position[0] + width, enemy.position[1] - player.position[1] + height))
		enemyhealthbar = pygame.Surface((120 * (enemy.health / enemy.max_health), 10))
		enemyhealthbar.fill(GREEN)
		screen.blit(enemyhealthbar, (enemy.position[0] - player.position[0] + width, enemy.position[1] - player.position[1] + height - 20))

	screen.blit(player.surf, (width, height))

	for entity in player.entities:
		screen.blit(entity.surf, (entity.position[0] - player.position[0] + width, entity.position[1] - player.position[1] + height))

bar_border = pygame.Surface((400, 40))
health_bar_back = pygame.Surface((390 , 30))

stat_border = pygame.Surface((300, 125))
stat_hud = pygame.Surface((290, 115))

hud = pygame.Surface((1280 - 300, 150))

empty = pygame.Surface((0,0))

def draw_hud(screen, player, fps):
		
		bar_border.fill(BLACK)
		stat_border.fill(BLACK)
		stat_hud.fill(HUD)
		hud.fill(HUD)
		health_bar_back.fill(RED)

		font = pygame.font.SysFont("Roboto Mono", 22)
		# HEALTH BAR BELOW

		if player.health > 0:
			surf = pygame.Surface((390 * ((player.health / player.max_health)), 30))
		else:
			surf = empty
		surf.fill(GREEN)
		health_bar_back.blit(surf, (0, 0))
		img = font.render("%s / %s" % (int(player.health), player.max_health), True, BLACK)
		health_bar_back.blit(img, (2, 10))
		bar_border.blit(health_bar_back, (5, 5))
		hud.blit(bar_border, (hud.get_width() - 400 - 12.5, 25))

		# SPECIAL CHARGE
		health_bar_back.fill(WHITE)
		if player.charge > 0:
			surf = pygame.Surface((390 * ((player.charge / 100)), 30))
		else:
			surf = empty
		surf.fill(MAGIC_BLUE)
		health_bar_back.blit(surf, (0, 0))
		img = font.render("%s / %s" % (player.charge, 100), True, BLACK)
		health_bar_back.blit(img, (2, 10))
		bar_border.blit(health_bar_back, (5, 5))
		hud.blit(bar_border, (hud.get_width() - 400 - 12.5, hud.get_height() - 25 - bar_border.get_height()))

		# STATS BELOW
		stat_hud.fill(HUD)
		stat_border.fill(BLACK)
		font = pygame.font.SysFont("Roboto Mono", 28)

		text = font.render("Attack: %s" %(player.attack * player.attack_mod), True, DAMAGE_ORANGE)
		stat_hud.blit(text, (5, 5))

		text = font.render("Armour: %s" %(player.armour * player.armour_mod), True, DAMAGE_ORANGE)
		stat_hud.blit(text, (5, 5 + 28))

		text = font.render("Magic: %s" %(player.magic * player.magic_mod), True, MAGIC_BLUE)
		stat_hud.blit(text, (5, 5 + 28 * 2))

		text = font.render("Magic resist: %s" %(player.magic_resist * player.magic_resist_mod), True, MAGIC_BLUE)
		stat_hud.blit(text, (5, 5 + 28 * 3))

		text = font.render("Speed: %s" %(player.speed * player.speed_mod), True, WHITE)
		stat_hud.blit(text, (-text.get_width() + 280, 5))

		stat_border.blit(stat_hud, (5, 5))
		hud.blit(stat_border, (12.5, 12.5))

		fps = font.render("FPS: %s" % fps, True, WHITE)
		screen.blit(fps, (screen.get_width() - fps.get_width(), 0))

		pos = font.render("(%s, %s)" % (int(player.position[0]), int(player.position[1])), True, WHITE)
		screen.blit(pos, (screen.get_width() - pos.get_width(), fps.get_height() + 5))

		screen.blit(hud, (150, 720 - 150))