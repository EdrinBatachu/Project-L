import json

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

		self.position = [10, 10]

	def __repr__(self):
		return "%s, on %s health." % (self.name, self.health)