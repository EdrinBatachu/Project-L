def main_menu(screen):
	import pygame
	from main import WIDTH, HEIGHT, BLACK, WHITE
	import sys
	mainMenu = True

	panelX = 225
	panelY = 300

	x = 60
	y = 20
	champ_rects = []
	panel = pygame.Surface((panelX, panelY))
	from characters import champions
	for champ in champions:
		champ_rects.append(pygame.Rect(x, y, panelX, panelY))
		if x + panelX > WIDTH - panelX - 60:
			x = 60
			y += panelY + 20
			continue

		x += panelX + 60

	while mainMenu:
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainMenu = False
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mousepos = pygame.mouse.get_pos()
				for i in champ_rects:
					if i.collidepoint(mousepos):
						index = champ_rects.index(i)
						return index

		count = 0
		for champ in champions:
			panel.fill(champ["colour"])
			screen.blit(panel, (champ_rects[count].left, champ_rects[count].top))

			count += 1

		pygame.display.flip()

if __name__ == "__main__":
	print("Success")