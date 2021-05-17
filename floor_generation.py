import pygame

bottom_open_room = [
"#" * 10,
"#" + "." * 8 + '#',
"X" + "." * 8 + "#",
"#" + "." * 8 + "#",
"#" + "." * 8 + "#",
"#" + "." * 8 + "#",
"#" + "." * 8 + "#",
"#" + "." * 8 + "#",
"#" + "." * 8 + "#",
"#" + "." * 8 + "#",
"#" * 10
]

def gen_dungeon():
	return bottom_open_room

def get_wall_rects(walls, room, TILESIZE):
	x = 0
	for i in room:
		y = 0
		for j in i:
			if room[x][y] == "#":
				rectangle = pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
				walls.append(rectangle)
			y += 1
		x += 1