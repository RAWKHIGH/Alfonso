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

class FloorW1B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world1(1)_ground2.png")
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
		self.rect.left = 4544
		
class FloorW1C(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world1(1)_ground3.png")
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
		self.rect.left = 5695
		
class FloorW1D(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world1(2)_ground1.png")
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
		self.rect.left = 1024
		
class FloorW1E(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world1(2)_ground2.png")
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
		self.rect.left = 4289

class PipeW1A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("small_pipe.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 449
		self.rect.left = 1791
		
class PipeW1B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("large_pipe.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 383
		self.rect.left = 2431
		
class PipeW1C(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("large_pipe.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 319
		self.rect.left = 2943
		
class PipeW1D(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("large_pipe.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 319
		self.rect.left = 3648
		
class PipeW1E(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("large_pipe.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 449
		self.rect.left = 4803
		
class PipeW1F(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("large_pipe.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 449
		self.rect.left = 5827
		
class QboxW1A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 1023
		
class QboxW1B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 1342
		
class QboxW1C(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 1471
		
class QboxW1D(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 1406
		
class QboxW1E(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 4991
		
class QboxW1F(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 6016
		
class QboxW1G(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 1153
		
class QboxW1H(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 1345
		
class QboxW1I(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 1537
		
class QboxW1J(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 1345
		
class QboxW1K(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 2626
		
class QboxW1L(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 2690
		
class QboxW1M(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 5250
		
		
class BlockW1A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 1278
		
class BlockW1B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 1406
		
class BlockW1C(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 1534
		
class BlockW1D(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 4927
		
class BlockW1E(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 5056
		
class BlockW1F(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5120
		
class BlockW1G(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5184
		
class BlockW1H(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5248
		
class BlockW1I(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5312
		
class BlockW1J(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5376

class BlockW1K(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5440
		
class BlockW1L(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5504
		
class BlockW1M(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5568
		
class BlockW1N(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5824
		
class BlockW1O(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5888
		
class BlockW1P(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 5952
		
class BlockW1Q(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 6016
		
class BlockW1R(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 6400
		
class BlockW1S(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 6464
		
class BlockW1T(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 1922
		
class BlockW1U(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 2113
		
class BlockW1V(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 2177
		
class BlockW1W(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 2241
		
class BlockW1X(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 2562
		
class BlockW1Y(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 63
		self.rect.left = 2753
		
class BlockW1Z(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 2626
		
class BlockW1AA(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 2690
		
class BlockW1AB(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 5121
		
class BlockW1AC(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 5185
		
class BlockW1AD(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx
		
	def reset(self):
		self.rect.top = 320
		self.rect.left = 5314
		
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
		floorw1B = FloorW1B()
		floorw1C = FloorW1C()
		floorw1D = FloorW1D()
		floorw1E = FloorW1E()
		pipew1A = PipeW1A()
		pipew1B = PipeW1B()
		pipew1C = PipeW1C()
		pipew1D = PipeW1D()
		pipew1E = PipeW1E()
		pipew1F = PipeW1F()
		qboxw1A = QboxW1A()
		qboxw1B = QboxW1B()
		qboxw1C = QboxW1C()
		qboxw1D = QboxW1D()
		qboxw1E = QboxW1E()
		qboxw1F = QboxW1F()
		qboxw1G = QboxW1G()
		qboxw1H = QboxW1H()
		qboxw1I = QboxW1I()
		qboxw1J = QboxW1J()
		qboxw1K = QboxW1K()
		qboxw1L = QboxW1L()
		qboxw1M = QboxW1M()
		blockw1A = BlockW1A()
		blockw1B = BlockW1B()
		blockw1C = BlockW1C()
		blockw1D = BlockW1D()
		blockw1E = BlockW1E()
		blockw1F = BlockW1F()
		blockw1G = BlockW1G()
		blockw1H = BlockW1H()
		blockw1I = BlockW1I()
		blockw1J = BlockW1J()
		blockw1K = BlockW1K()
		blockw1L = BlockW1L()
		blockw1M = BlockW1M()
		blockw1N = BlockW1N()
		blockw1O = BlockW1O()
		blockw1P = BlockW1P()
		blockw1Q = BlockW1Q()
		blockw1R = BlockW1R()
		blockw1S = BlockW1S()
		blockw1T = BlockW1T()
		blockw1U = BlockW1U()
		blockw1V = BlockW1V()
		blockw1W = BlockW1W()
		blockw1X = BlockW1X()
		blockw1Y = BlockW1Y()
		blockw1Z = BlockW1Z()
		blockw1AA = BlockW1AA()
		blockw1AB = BlockW1AB()
		blockw1AC = BlockW1AC()
		blockw1AD = BlockW1AD()
	
		backgroundSprites = pygame.sprite.OrderedUpdates(level1B, level1A)
		floorSprites = pygame.sprite.OrderedUpdates(floorw1A, floorw1B, floorw1C, floorw1D, floorw1E)
		pipeSprites = pygame.sprite.OrderedUpdates(pipew1A, pipew1B, pipew1C, pipew1D, pipew1E, pipew1F)
		QboxSprites = pygame.sprite.OrderedUpdates(qboxw1A, qboxw1B, qboxw1C, qboxw1D, qboxw1E, qboxw1F, qboxw1G, qboxw1H, qboxw1I, qboxw1J, qboxw1K, qboxw1L, qboxw1M)
		blockSprites = pygame.sprite.OrderedUpdates(blockw1A, blockw1B, blockw1C, blockw1D, blockw1E, blockw1F, blockw1G, blockw1H, blockw1I, blockw1J, blockw1K, blockw1L, blockw1M, blockw1N, blockw1O, blockw1P, blockw1Q, blockw1R, blockw1S, blockw1T, blockw1U, blockw1V, blockw1W, blockw1X, blockw1Y, blockw1Z, blockw1AA, blockw1AB, blockw1AC, blockw1AD)
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
					floorw1B.moveLeft()
					floorw1C.moveLeft()
					pipew1A.moveLeft()
					pipew1B.moveLeft()
					pipew1C.moveLeft()
					pipew1D.moveLeft()
					qboxw1A.moveLeft()
					qboxw1B.moveLeft()
					qboxw1C.moveLeft()
					qboxw1D.moveLeft()
					qboxw1E.moveLeft()
					qboxw1F.moveLeft()
					blockw1A.moveLeft()
					blockw1B.moveLeft()
					blockw1C.moveLeft()
					blockw1D.moveLeft()
					blockw1E.moveLeft()
					blockw1F.moveLeft()
					blockw1G.moveLeft()
					blockw1H.moveLeft()
					blockw1I.moveLeft()
					blockw1J.moveLeft()
					blockw1K.moveLeft()
					blockw1L.moveLeft()
					blockw1M.moveLeft()
					blockw1N.moveLeft()
					blockw1O.moveLeft()
					blockw1P.moveLeft()
					blockw1Q.moveLeft()
					blockw1R.moveLeft()
					blockw1S.moveLeft()
					if level1A.rect.right <= 1024:
						level1B.moveLeft()
						floorw1D.moveLeft()
						floorw1E.moveLeft()
						pipew1E.moveLeft()
						pipew1F.moveLeft()
						qboxw1G.moveLeft()
						qboxw1H.moveLeft()
						qboxw1I.moveLeft()
						qboxw1J.moveLeft()
						qboxw1K.moveLeft()
						qboxw1L.moveLeft()
						qboxw1M.moveLeft()
						blockw1T.moveLeft()
						blockw1U.moveLeft()
						blockw1V.moveLeft()
						blockw1W.moveLeft()
						blockw1X.moveLeft()
						blockw1Y.moveLeft()
						blockw1Z.moveLeft()
						blockw1AA.moveLeft()
						blockw1AB.moveLeft()
						blockw1AC.moveLeft()
						blockw1AD.moveLeft()

			if key[pygame.K_RIGHT]:
				if level1B.rect.right > 1024:
					level1A.moveRight()
					floorw1A.moveRight()
					floorw1B.moveRight()
					floorw1C.moveRight()
					pipew1A.moveRight()
					pipew1B.moveRight()
					pipew1C.moveRight()
					pipew1D.moveRight()
					qboxw1A.moveRight()
					qboxw1B.moveRight()
					qboxw1C.moveRight()
					qboxw1D.moveRight()
					qboxw1E.moveRight()
					qboxw1F.moveRight()
					blockw1A.moveRight()
					blockw1B.moveRight()
					blockw1C.moveRight()
					blockw1D.moveRight()
					blockw1E.moveRight()
					blockw1F.moveRight()
					blockw1G.moveRight()
					blockw1H.moveRight()
					blockw1I.moveRight()
					blockw1J.moveRight()
					blockw1K.moveRight()
					blockw1L.moveRight()
					blockw1M.moveRight()
					blockw1N.moveRight()
					blockw1O.moveRight()
					blockw1P.moveRight()
					blockw1Q.moveRight()
					blockw1R.moveRight()
					blockw1S.moveRight()
					if level1A.rect.right <= 1024:
						level1B.moveRight()
						floorw1D.moveRight()
						floorw1E.moveRight()
						pipew1E.moveRight()
						pipew1F.moveRight()
						qboxw1G.moveRight()
						qboxw1H.moveRight()
						qboxw1I.moveRight()
						qboxw1J.moveRight()
						qboxw1K.moveRight()
						qboxw1L.moveRight()
						qboxw1M.moveRight()
						blockw1T.moveRight()
						blockw1U.moveRight()
						blockw1V.moveRight()
						blockw1W.moveRight()
						blockw1X.moveRight()
						blockw1Y.moveRight()
						blockw1Z.moveRight()
						blockw1AA.moveRight()
						blockw1AB.moveRight()
						blockw1AC.moveRight()
						blockw1AD.moveRight()

			if key[pygame.K_SPACE]:
				player.jump()
				
				
			if not pygame.sprite.spritecollideany(player, floorSprites):
				if not pygame.sprite.spritecollideany(player, QboxSprites):
					if not pygame.sprite.spritecollideany(player, blockSprites):
						fall = 15
						player.rect.centery += fall
			
				
			playerSprites.update()
			backgroundSprites.update()
			floorSprites.update()
			pipeSprites.update()
			QboxSprites.update()
			blockSprites.update()

			backgroundSprites.draw(screen)
			pipeSprites.draw(screen)
			QboxSprites.draw(screen)
			blockSprites.draw(screen)
			floorSprites.draw(screen)
			playerSprites.draw(screen)
			
			
			pygame.display.flip()
		
		pygame.mouse.set_visible(True)
		
if __name__ == "__main__":
	main()