import json
import specials as s
import pygame

with open("data/characters.json") as file:
	champions = json.load(file)


def get_champion(identify):
	try:
		champ = champions[identify]
	except:
		print("No champion with that ID")
		return

	return Fighter(champ["name"], champ["attack"], champ["armour"], champ["magic"], champ["magic_resist"], champ["speed"], champ["health"])

class Fighter:
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

		self.charge = 80

		self.position = [200, 200]
		self.direction = [1, -1]

		self.special = s.get_special(self.name)
		self.passive = s.get_passive(self.name)

		self.entities = []
		self.enemies = []

		self.surf = pygame.Surface((120, 160))
		self.surf.fill((0, 255, 0))
		self.rect = pygame.Rect((self.position), (120, 160))

	def __repr__(self):
		return "%s, on %s health." % (self.name, self.health)

	def update(self, enemies):
		self.rect.top = self.position[1]
		self.rect.left = self.position[0]
		self.enemies = enemies

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

def main():
	pass


if __name__ == "__main__":

	main()