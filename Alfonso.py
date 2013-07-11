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
		self.image = pygame.image.load("alfonso_pause.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
	
	def update(self):
		self.rect.centerx = 450
		
	def jump(self):
		jump = 35
		self.rect.centery -= jump

			
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

class FloorW1A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world1(1)_1stFloor.png")
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
		screen.blit(background, (0, 0))

		player = Alfonso()
		level1A = World1A()
		level1B = World1B()
		floorw1A = FloorW1A()
	
		backgroundSprites = pygame.sprite.OrderedUpdates(level1B, level1A)
		floorSprites = pygame.sprite.OrderedUpdates(floorw1A)
		playerSprites = pygame.sprite.OrderedUpdates(player)
		
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
				if not level1A.rect.left == 0:
					level1A.moveLeft()
					floorw1A.moveLeft()
					if level1A.rect.right <= 1024:
						level1B.moveLeft()
			
			if key[pygame.K_RIGHT]:
				if level1B.rect.right > 1024:
					level1A.moveRight()
					floorw1A.moveRight()
					if level1A.rect.right <= 1024:
						level1B.moveRight()
						
			if key[pygame.K_SPACE]:
				player.jump()
				
				
			if not pygame.sprite.spritecollideany(player, floorSprites):
				fall = 15
				player.rect.centery += fall
					
					
					
			playerSprites.update()
			backgroundSprites.update()
			floorSprites.update()

			
			backgroundSprites.draw(screen)
			floorSprites.draw(screen)
			playerSprites.draw(screen)
			
			pygame.display.flip()
		
		pygame.mouse.set_visible(True)
		
if __name__ == "__main__":
	main()