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
		self.rect.center = (450, 525)

class World1A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world1(1).png")
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

#	def update(self):
		
	
	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.bottom = screen.get_height()
	
class World1B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world1(2).png")
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

#	def update(self):


	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.left = 1024
		self.rect.bottom = screen.get_height()
	
def main():
		screen = pygame.display.set_mode((1024, 672))
		pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")

		background = pygame.Surface(screen.get_size())
		background.fill((0, 0, 0))
		screen.blit(background, (0, 0))

		player = Alfonso()
		level1A = World1A()
		level1B = World1B()
	
		allSprites = pygame.sprite.OrderedUpdates(level1B, level1A, player)
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
				if level1A.rect.left != 0:
					level1A.moveLeft()
					if level1A.rect.right <= 1024:
						level1B.moveLeft()
			
			if key[pygame.K_RIGHT]:
				if level1B.rect.right > 1024:
					level1A.moveRight()
					if level1A.rect.right <= 1024:
						level1B.moveRight()

						

			allSprites.update()
			allSprites.draw(screen)

			pygame.display.flip()
		
		pygame.mouse.set_visible(True)
		
if __name__ == "__main__":
	main()