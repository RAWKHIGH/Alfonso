import pygame
pygame.init()

class Alfonso(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("alfonso.png")
		self.image = self.image.convert()
		self.rect = self.image.get_rect()

	def update(self):
		mousex, mousey = pygame.mouse.get_pos()
		self.rect.center = (mousex, 430)

def main():
	screen = pygame.display.set_mode((1024, 672))
	pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")

	background = pygame.Surface(screen.get_size())
	background.fill((0, 0, 255))
	screen.blit(background, (0, 0))
	player = Alfonso()

	allSprites = pygame.sprite.Group(player)
	clock = pygame.time.Clock()
	keepGoing = True
	while keepGoing:
		clock.tick(30)
		pygame.mouse.set_visible(False)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				keepGoing = False

		allSprites.clear(screen, background)
		allSprites.update()
		allSprites.draw(screen)

		pygame.display.flip()

	#return mouse cursor
	pygame.mouse.set_visible(True) 
if __name__ == "__main__":
	main()