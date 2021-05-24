import json, pygame, random
import movement

with open("data/enemies.json") as file:
	enemies = json.load(file)

def get_enemy(identify, player):
	try:
		enemy = enemies[identify]
	except:
		print("No enemy with that ID")
		return

	return Enemy(enemy["name"], enemy["attack"], enemy["armour"], enemy["magic"], enemy["magic_resist"], enemy["speed"], enemy["health"], (player.position[0] + random.randint(-500, 500), player.position[1] + random.randint(-500, 500)), enemy["x"], enemy["y"] )

class Enemy:
	def __init__(self, name, attack, armour, magic, magic_resist, speed, health, position, x, y):
		self.name = name
		self.attack = attack
		self.armour = armour
		self.magic = magic
		self.magic_resist = magic_resist
		self.speed = speed
		self.max_health = health
		self.health = health

		self.attack_mod = 1
		self.armour_mod = 1
		self.magic_mod = 1
		self.magic_resist_mod = 1
		self.speed_mod = 1

		self.accuracy = 100
		self.evasion = 0
		self.ricochet_chance = 0
		self.crit_chance = 0
		self.crit_damage = 2
		self.lifesteal = 0

		self.armor_pen = 0
		self.magic_pen = 0

		self.charge = 100

		self.position = list(position)

		self.up_images = []
		self.down_images = []
		self.right_images = []
		self.left_images = []

		if self.name == "Biter":

			for i in range(0, 2):
				self.up_images.append(pygame.transform.scale(pygame.image.load("data/sprites/%s/%s_up_%s.png" % (self.name, self.name.lower(), i)).convert_alpha(), (x, y)))
			for i in range(0, 2):
				self.down_images.append(pygame.transform.scale(pygame.image.load("data/sprites/%s/%s_down_%s.png" % (self.name, self.name.lower(), i)).convert_alpha(), (x, y)))
			for i in range(0, 2):
				self.left_images.append(pygame.transform.scale(pygame.image.load("data/sprites/%s/%s_left_%s.png" % (self.name, self.name.lower(), i)).convert_alpha(), (x, y)))
			for i in range(0, 2):
				self.right_images.append(pygame.transform.scale(pygame.image.load("data/sprites/%s/%s_right_%s.png" % (self.name, self.name.lower(), i)).convert_alpha(), (x, y)))


		self.x = x
		self.y = y

		self.surf = pygame.Surface((x, y))
		self.rect = self.surf.get_rect()
		self.sight_rect = pygame.Rect(self.position, (700, 700))

		self.target = None
		self.cooldown = 180
		self.index = len(self.up_images) - 1

	def __repr__(self):
		return "%s, on %s health." % (self.name, self.health)

	def update(self, player):
		self.rect.top = self.position[1]
		self.rect.left = self.position[0]
		self.sight_rect.center = self.rect.center

		if player.rect.colliderect(self.sight_rect) and self.cooldown >= 180:
			self.target = player.position
		else:
			self.target = player.position

		if self.rect.colliderect(player.rect) and self.cooldown >= 180:
			self._attack(player)
			self.cooldown = 0

		self.direction = movement.get_direction(self.rect.center, self.target)
		self.cooldown += 1
		
		if self.direction[0] == -1:
			try:
				self.surf = (self.right_images[int(self.index)])
				self.index += 0.2
			except:
				self.index = 0
				self.surf = (self.right_images[int(self.index)])

		elif self.direction[0] == 1:
			try:
				self.surf = (self.left_images[int(self.index)])
				self.index += 0.2
			except:
				self.index = 0
				self.surf = (self.left_images[int(self.index)])

		elif self.direction[1] == -1:
			try:
				self.surf = (self.up_images[int(self.index)])
				self.index += 0.2
			except:
				self.index = 0
				self.surf = (self.up_images[int(self.index)])

		elif self.direction[1] == 1:
			try:
				self.surf = (self.down_images[int(self.index)])
				self.index += 0.2
			except:
				self.index = 0
				self.surf = (self.down_images[int(self.index)])

		self.surf.convert_alpha()


	def _attack(self, target):
		import random
		from main import calculate_damage_mod
		if self.magic > self.attack:
			damage = self.magic * self.magic_mod
			if random.randint(0, 100) < crit_chance:
				damage *= crit_damage

			damage *= calculate_damage_mod(self, target, "magic")

		else:
			damage = self.attack * self.attack_mod
			if random.randint(0, 100) < self.crit_chance:
				damage *= self.crit_damage

			damage *= calculate_damage_mod(self, target, "armour")
			
		self.health += damage * self.lifesteal
		target.health -= damage
		if target.health < 0:
			target.health = 0

