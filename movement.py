import pygame

def move(player, keys, dt):
	speed = player.speed * dt
	if keys[pygame.K_w]:
		player.position[1] -= speed
	elif keys[pygame.K_s]:
		player.position[1] += speed
	if keys[pygame.K_a]:
		player.position[0] -= speed
	elif keys[pygame.K_d]:
		player.position[0] += speed