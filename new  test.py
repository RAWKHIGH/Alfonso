import pygame
from pygame import *

pygame.init()

black    = (  0,  0,  0)
white    = (255,255,255)
green    = (  0,255,  0)
red      = (255,  0,  0)

screen = pygame.display.set_mode((1024, 672))

class GoombaW1A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("goomba1.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.speed = 1
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.bottom = screen.get_height() - 95
		self.rect.centerx = 500
	
	def update(self):
		self.rect.centerx += self.speed
		
class FloorW1A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world1(1)_ground1.png")
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
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
	
		floorw1A = FloorW1A()
		goombaW1A = GoombaW1A()
		
		floorSprites = pygame.sprite.OrderedUpdates(floorw1A)
		badSprites = pygame.sprite.Group(goombaW1A)
		
		clock = pygame.time.Clock()
		keepGoing = True
		while keepGoing:
			clock.tick(30)
			key = pygame.key.get_pressed()
			jumping = False
			collideLeft = False
			collideRight = False
			pygame.mouse.set_visible(False)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					keepGoing = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						player.jump()
	
	
			floorSprites.update()
			badSprites.update()
			
			badSprites.draw(screen)
			floorSprites.draw(screen)

		
if __name__ == "__main__":
	main()