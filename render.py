import pygame
from main import HUD, BLACK, RED, GREEN, MAGIC_BLUE, DAMAGE_ORANGE, WHITE

def get_sprites(name):
	images = []
	sprite_types = ("icon", "up", "down", "left", "right")
	for i in sprite_types:
		img = pygame.image.load("data/sprites/%s/idle/%s_%s" % (name, name, i))
		images.append(img)
	return images


enemy_surf = pygame.Surface((120, 160))
def draw_enemies(screen, enemies):
	enemy_surf.fill(RED)
	for enemy in enemies:
		screen.blit(enemy_surf, (enemy.position))

player_surf = pygame.Surface((120, 160))
def draw_playermodel(screen, player):
	player_surf.fill(MAGIC_BLUE)
	width = (screen.get_width() / 2) - (player_surf.get_width() / 2) 
	height = (screen.get_height() / 2) - (player_surf.get_height() / 2) - (75)
	screen.blit(player_surf, (width, height))

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
		screen.blit(hud, (150, 720 - 150))