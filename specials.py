import json

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

class Judgement:
	id = 0
	name = "Judgement"
	description = "The god of the kingdom is called upon, smiting the enemy."
	effect = "If the enemy is below 10% + caster.attack // 10 health, they are executed. Else, this attack deals 1.5x basic attack damage."

	def use(caster, enemy):
		if enemy.health < (enemy.health / 10) + caster.attack / 10:
			enemy.health = 0
		else:
			enemy.health -= caster.attack

class ArcaneBarrage:
	id = 1
	name = "Arcane Barrage"
	description = "An unstoppable barrage of pure magic is hurled at the enemy."
	effect = "Deals 2.5x the caster's magic, and buffs all the caster's magic attacks from now."

	def use(caster, enemy):
		caster.magic_mod += 0.2
		enemy.health -= caster.magic * 2

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
