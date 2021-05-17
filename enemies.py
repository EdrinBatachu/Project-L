import json, pygame

with open("data/enemies.json") as file:
	enemies = json.load(file)

def get_enemy(identify):
	try:
		enemy = enemies[identify]
	except:
		print("No enemy with that ID")
		return

	return Enemy(enemy["name"], enemy["attack"], enemy["armour"], enemy["magic"], enemy["magic_resist"], enemy["speed"], enemy["health"])

class Enemy:
	def __init__(self, name, attack, armour, magic, magic_resist, speed, health):
		self.name = name
		self.attack = attack
		self.armour = armour
		self.magic = magic
		self.magic_resist = magic_resist
		self.speed = speed
		self.max_health = health
		self.health = 60

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

		self.position = [400, 400]

		self.surf = pygame.Surface((120, 160))
		self.surf.fill((255, 0, 0))
		self.rect = self.surf.get_rect()

	def __repr__(self):
		return "%s, on %s health." % (self.name, self.health)

	def update(self):
		self.rect.top = self.position[1]
		self.rect.left = self.position[0]

	def attack(self, target):
		if self.magic > self.attack:
			damage = self.magic * self.magic_mod
			if random.randint(0, 100) < crit_chance:
				damage *= crit_damage

			damage /= target.magic_resist

		else:
			damage = self.attack * self.attack_mod
			if random.randint(0, 100) < crit_chance:
				damage *= crit_damage

			damage /= target.armour
			
		self.health += damage * self.lifesteal
		target.health -= damage
		if target.health < 0:
			target.health = 0

