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

def move_enemy(enemies, walls, dt):
	for enemy in enemies:
		speed = enemy.speed * dt
		if enemy.target != None:
			direction = get_direction(enemy.position, enemy.target)

			if check_wall_collisions(walls, enemy, (direction[0] * speed, direction[1] * speed)):
				enemy.position[0] += direction[0] * speed
				enemy.position[1] += direction[1] * speed


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

def get_direction(a, b):
	c = [0, 0]
	c[0] = a[0] - b[0]
	c[1] = a[1] - b[1]
	if c[0] < 0:
		c[0] = 1
	elif c[0] > 0:
		c[0] = -1
	if c[1] < 0:
		c[1] = -1
	elif c[1] > 0:
		c[1] = 1
	return c


if __name__ == "__main__":

	vec1 = [0, 0]
	vec2 = [-303, 1]
	print(get_direction(vec1, vec2))