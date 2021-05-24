import pygame

class Animation:
	def __init__(self, colors, lifetime, position, size, name):
		self.name = name
		self.surf = pygame.Surface((size))
		self.index = 0
		self.colors = colors
		self.surf.fill(self.colors[self.index])
		self.lifetime = lifetime * 60
		self.life = 0
		self.position = position[:]
		self.size = size
		self.rect = pygame.Rect(position, size)

	def update(self, animations):
		self.surf.fill(self.colors[int(self.index)])
		self.index += 0.2
		if self.index > len(self.colors) - 1:
			self.index = 0

		self.life += 1
		if self.life > self.lifetime:
			animations.remove(self)
