import json, pygame
import enemies as E
import render
from render import width, height
from math import degrees, radians
from movement import get_deg_direction


class Entity:
	def __init__(self, position, speed, direction, surface, damage=0, lifetime=0):
		self.position = position
		self.surf = surface
		self.lifetime = lifetime
		self.speed = speed
		self.direction = direction
		self.rect = pygame.Rect(self.position, (self.surf.get_width(), self.surf.get_height()))
		self.damage = damage

		if self.direction[0] == 0 and self.direction[1] == 0:
			self.direction[1] = 1

		self.counter = 0



with open("data/specials.json") as file:
	specials = json.load(file)


def get_special(champ_name):
	if champ_name == "Knight":
		return Judgement
	elif champ_name == "Mage":
		return ArcaneBarrage
	elif champ_name == "Juggernaut":
		return Retaliate
	elif champ_name == "Assassin":
		return Backstab
	elif champ_name == "Tank":
		return Fortify

def get_passive(champ_name):
	if champ_name == "Juggernaut":
		return None
	else:
		return None

class Judgement(Entity):
	id = 0
	name = "Judgement"
	description = "The god of the kingdom is called upon, smiting the enemy."
	effect = "If the enemy is below 10% + (caster.attack / 2) health, they are executed and the cost is refunded. Else, this attack deals 1.5x basic attack damage."

	def __init__(self, caster):
		if caster.charge == 100:
			for i in caster.enemies:
				if (abs(i.rect.center[0] - caster.rect.center[0]) < 200) and (abs(i.rect.center[1] - caster.rect.center[1] < 200)):
					enemy = i
					print(((enemy.max_health / 10) + caster.attack * caster.attack_mod / 2 ))
					if enemy.health < (enemy.max_health / 10) + caster.attack * caster.attack_mod / 2:
						enemy.health = 0
					else:
						caster.charge = 0
						enemy.health -= caster.attack * caster.attack_mod * 1.5 / enemy.armour * enemy.armour_mod
				else:
					print("No one close enough!")

		else:
			print("Not enough charge!")


class ArcaneBarrage(Entity):
	id = 1
	name = "Arcane Barrage"
	description = "An unstoppable barrage of pure magic is hurled at the enemy."
	effect = "Deals 1.5x the caster's magic, and buffs all the caster's magic attacks from now."
	speed = 50
	surf = pygame.Surface((120, 120))
	surf.fill((0, 183, 255))

	def __init__(self, caster):
		if caster.charge > 20:
			caster.magic_mod += 0.1
			caster.charge -= 20
			damage = caster.magic * 1.5 * caster.magic_mod
			super().__init__((caster.position[:]), ArcaneBarrage.speed, caster.direction[:], ArcaneBarrage.surf, damage=damage,lifetime=3)
			self.hit = []
			self.target = caster.mousepos
			self.direction = get_deg_direction(self.rect.center, self.target)
			caster.entities.append(self)
		else:
			print("Not enough charge!")


	def update(self, dt, enemies):
		speed = self.speed * dt / 60
		
		self.position[0] += self.direction[0] * speed
		self.position[1] += self.direction[1] * speed
		self.rect.top = self.position[1]
		self.rect.left = self.position[0]

		for e in enemies:
			if not (e in self.hit):
				if e.rect.colliderect(self.rect):
					print(e.position, self.position)
					self.hit.append(e)
					e.health -= (self.damage / e.magic_resist * e.magic_resist_mod)
					if e.health < 0:
						e.health = 0

class Retaliate:
	id = 2
	name = "Retaliate"
	description = "Juggernaut throws out a massive punch that deals more damage the more he's been hurt."
	effect = "Deals 50 damage per 10% missing caster health."

	def use(caster, enemy):
		damage = caster.attack + (50 * (caster.max_health - caster.health) / 50)
		enemy.health -= damage
		print(damage)

class Backstab:
	id = 3
	name = "Backstab"
	description = "The Assassin runs behind the enemy, dealing massive damage with their dagger."
	effect = "Deals 3x the attackers attack, and causes the enemy to have a 50% chance to miss next attack."

	def use(caster, enemy):
		damage = caster.attack * 3
		caster.evasion = 0.5
		enemy.health -= damage

class Fortify:
	id = 4
	name = "Fortify"
	description = "The Tank braces for impact, raising their defence to unparalleled levels."
	effect = "For the next 2 turns, resistence is 3x, enemy attacks have 10% chance to ricochet off."

	def use(caster, enemy):
		caster.armour_mod = 3
		caster.magic_resist_mod = 3
		caster.ricochet_chance = 0.1
