import pygame

def check_wall_collisions(walls, player, change):
	checks = []
	temp = player.position[:]
	temp[0] += change[0]
	temp[1] += change[1]
	temprect = pygame.Rect(temp, (120, 160))

	for wall in walls:
		if wall.colliderect(temprect):
			return False
	return True

# 2/3
def move(player, keys, dt, walls):
	speed = player.speed * dt

	if keys[pygame.K_w]:
		if check_wall_collisions(walls, player, (0, -speed)):
			player.position[1] -= speed
		player.direction[1] = -1

	elif keys[pygame.K_s]:
		if check_wall_collisions(walls, player, (0, speed)):
			player.position[1] += speed
		player.direction[1] = 1
	else:
		player.direction[1] = 0

	if keys[pygame.K_a]:
		if check_wall_collisions(walls, player, (-speed, 0)):
			player.position[0] -= speed
		player.direction[0] = -1
	elif keys[pygame.K_d]:
		if check_wall_collisions(walls, player, (speed, 0)):
			player.position[0] += speed
		player.direction[0] = 1
	else:
		player.direction[0] = 0