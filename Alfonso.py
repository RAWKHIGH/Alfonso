import pygame
from pygame import *
pygame.init()


black    = (  0,  0,  0)
white    = (255,255,255)
green    = (  0,255,  0)
red      = (255,  0,  0)

screen = pygame.display.set_mode((1024, 672))

class Alfonso(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("alfonso.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		
		
	def update(self):
		self.rect.center = (100, 525)

class World1A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world1(1).png")
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def update(self):
		if self.rect.top >= 0:
			self.reset() 
	
	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.bottom = screen.get_height()
	
def main():
		screen = pygame.display.set_mode((1024, 672))
		pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")

		background = pygame.Surface(screen.get_size())
		background.fill((0, 0, 0))
		screen.blit(background, (0, 0))

		player = Alfonso()
		level1A = World1A()
	
		allSprites = pygame.sprite.OrderedUpdates(level1A, player)
		clock = pygame.time.Clock()
		keepGoing = True
		while keepGoing:
			clock.tick(30)
			key = pygame.key.get_pressed()
			pygame.mouse.set_visible(False)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					keepGoing = False
					
					
					
			if key[pygame.K_LEFT]:
						level1A.moveLeft()
			if key[pygame.K_RIGHT]:
						level1A.moveRight()

			#allSprites.clear(screen, background)
			allSprites.update()
			allSprites.draw(screen)

			pygame.display.flip()
		
		#return mouse cursor
		pygame.mouse.set_visible(True)
		
if __name__ == "__main__":
	main()