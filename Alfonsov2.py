# Name: Stephen McArthur
# Purpose: Final Project. Create game with 3 levels (Easy, Medium, Hard) and a Boss level
# GitHub: https://github.com/RAWKHIGH/Alfonso.git

import pygame, random
from pygame import *

pygame.init()

black    = (  0,  0,  0)
white    = (255,255,255)
green    = (  0,255,  0)
red      = (255,  0,  0)

screen = pygame.display.set_mode((1024, 672))
class Alfonso(pygame.sprite.Sprite):

	# -- Attributes 
	# Set speed vector of player
	change_x=0
	change_y=0

	# Count of frames since the player hit 'jump' and we
	# collided against something. Used to prevent jumping
	# when we haven't hit anything.
	frame_since_collision = 0
	frame_since_jump = 0
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("walk R000.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.turn = 1
		self.rect.bottom = 577
		self.jump_ready = False
		self.floor = 513
		
		self.imgList = []
		self.loadPics()
		


	def loadPics(self):
		fileBase = [
			"walk R00",
			"walk L00"
		]
 
		for dir in range(2):
			tempList = []
			tempFile = fileBase[dir]
			for frame in range(2):
				imgName = "{0}{1}.png".format(tempFile, frame)
				tmpImg = pygame.image.load(imgName)
				tmpImg.convert()
				tranColor = tmpImg.get_at((0, 0))
				tmpImg.set_colorkey(tranColor)
				tempList.append(tmpImg)
			self.imgList.append(tempList)
		
		# Change the speed of the player 
	def changespeed_x(self,x):
		self.change_x = x
 
	def changespeed_y(self,y):
		self.change_y = y
           
		# Find a new position for the player 
	def update(self): 
		self.rect.centerx = 450
		
		# Save the old y position, update, and see if we collided.
		old_y = self.rect.y 
		new_y = old_y + self.change_y 
		self.rect.y = new_y
         
        # If the player recently asked to jump, and we have recently
        # had ground under our feet, go ahead and change the velocity
        # to send us upwards
		if self.jump_ready == True:
			if self.frame_since_collision < 6 and self.frame_since_jump < 6:
				self.frame_since_jump = 100
				self.change_y -= 16.5
 
		# Increment frame counters
		self.frame_since_collision+=1
		self.frame_since_jump+=1
		
		# Calculate effect of gravity.
	def calc_grav(self):
		self.change_y += .50

		# See if we are on the ground.
		if self.rect.y >= self.floor and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = self.floor
			self.frame_since_collision = 0
 
	# Called when user hits 'jump' button
	def jump(self):
		self.jump_ready = True
		self.frame_since_jump = 0	
		
	
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
		self.rect.bottom = screen.get_height()

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("None", 30)
        
    def update(self):
        self.text = " lives: %d     Super Mario BROS. Cousin Alfonso     score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
		
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
		self.rect.left = 6787

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
		self.rect.left = 6979

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
		self.rect.left = 7171

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
		self.rect.left = 6979

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
		self.rect.left = 8260

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
		self.rect.left = 8324

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
		self.rect.left = 10884


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
		self.rect.left = 7556

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
		self.rect.left = 7747

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
		self.rect.left = 7811

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
		self.rect.left = 7875

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
		self.rect.left = 8196

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
		self.rect.left = 8387

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
		self.rect.left = 8260

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
		self.rect.left = 8324

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
		self.rect.left = 10755

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
		self.rect.left = 10819

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
		self.rect.left = 10948

class StarW1A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 270
		self.rect.left = 1040

class StarW1B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 270
		self.rect.left = 1359

class StarW1C(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 270
		self.rect.left = 1488

class StarW1D(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 13
		self.rect.left = 1423

class StarW1E(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 270
		self.rect.left = 5008

class StarW1F(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 13
		self.rect.left = 6033

class StarW1G(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 270
		self.rect.left = 6804

class StarW1H(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 270
		self.rect.left = 6996

class StarW1I(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 270
		self.rect.left = 7188

class StarW1J(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 13
		self.rect.left = 6996

class StarW1K(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 13
		self.rect.left = 8277

class StarW1L(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 13
		self.rect.left = 8341

class StarW1M(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
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
		self.rect.top = 270
		self.rect.left = 10901
		
class Goomba(pygame.sprite.Sprite):
	def __init__(self, centerx):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("goomba1.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.calcMove()
		self.centerx = centerx
		self.reset()
	
	def calcMove(self):
		self.speed = random.randint(1,5)
		self.dir = random.randint(0,1)
		if self.dir	== 0:
			self.dir = -1
		self.speed *= self.dir
	
	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.bottom = screen.get_height() - 95
		self.rect.centerx = self.centerx
	
	def update(self):
		self.rect.centerx += self.speed
		

class GoombaW1B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("goomba1.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.speed = -1
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.bottom = screen.get_height() - 95
		self.rect.centerx = 2109
	
	def update(self):
		self.rect.centerx += self.speed
		
class GoombaW1C(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("goomba1.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.speed = -1
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.bottom = screen.get_height() - 95
		self.rect.centerx = 2725
	
	def update(self):
		self.rect.centerx += self.speed
		
class GoombaW1D(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("goomba1.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.speed = -1
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.bottom = screen.get_height() - 95
		self.rect.centerx = 3266
	
	def update(self):
		self.rect.centerx += self.speed
		
class GoombaW1E(pygame.sprite.Sprite):
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
		self.rect.centerx = 3329
	
	def update(self):
		self.rect.centerx += self.speed	
		
class GoombaW1F(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("goomba1.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.speed = -1
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.bottom = screen.get_height() - 95
		self.rect.centerx = 4442
	
	def update(self):
		self.rect.centerx += self.speed	
		
class GoombaW1G(pygame.sprite.Sprite):
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
		self.rect.centerx = 5121
	
	def update(self):
		self.rect.centerx += self.speed	
		
class GoombaW1H(pygame.sprite.Sprite):
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
		self.rect.centerx = 5121
	
	def update(self):
		self.rect.centerx += self.speed	
		
class GoombaW1I(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("goomba1.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.speed = -1
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.bottom = screen.get_height() - 95
		self.rect.centerx = 5121
	
	def update(self):
		self.rect.centerx += self.speed	
		
class GoombaW1J(pygame.sprite.Sprite):
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
		self.rect.centerx = 5121
	
	def update(self):
		self.rect.centerx += self.speed	
		
class GoombaW1K(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("goomba1.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.speed = -1
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.bottom = screen.get_height() - 95
		self.rect.centerx = 5121
	
	def update(self):
		self.rect.centerx += self.speed	
		
class GoombaW1L(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("goomba1.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.speed = -1
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.bottom = screen.get_height() - 95
		self.rect.centerx = 5121
	
	def update(self):
		self.rect.centerx += self.speed

def intro():
	screen = pygame.display.set_mode((1024, 672))
	pygame.display.set_caption("Cousin Alfonso Start Screen")

		
def main():
		screen = pygame.display.set_mode((1024, 672))
		pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")

		background = pygame.Surface(screen.get_size())
		background.fill((0, 0, 0))
		screen.blit(background, (0, 0))

		score = 0
		
		player = Alfonso()
		level1A = World1A()
		level1B = World1B()
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
		starW1A = StarW1A()
		starW1B = StarW1B()
		starW1C = StarW1C()
		starW1D = StarW1D()
		starW1E = StarW1E()
		starW1F = StarW1F()
		starW1G = StarW1G()
		starW1H = StarW1H()
		starW1I = StarW1I()
		starW1J = StarW1J()
		starW1K = StarW1K()
		starW1L = StarW1L()
		starW1M = StarW1M()

		scoreboard = Scoreboard()

		goombas = []
		
		for goomba in range(50):
			goombax = random.randint(level1A.rect.left, level1B.rect.right)
			goombas.append(Goomba(goombax))
		
		backgroundSprites = pygame.sprite.OrderedUpdates(level1B, level1A)
		QboxSprites = pygame.sprite.OrderedUpdates(qboxw1A, qboxw1B, qboxw1C, qboxw1D, qboxw1E, qboxw1F, qboxw1G, qboxw1H, qboxw1I, qboxw1J, qboxw1K, qboxw1L, qboxw1M)
		blockSprites = pygame.sprite.OrderedUpdates(blockw1A, blockw1B, blockw1C, blockw1D, blockw1E, blockw1F, blockw1G, blockw1H, blockw1I, blockw1J, blockw1K, blockw1L, blockw1M, blockw1N, blockw1O, blockw1P, blockw1Q, blockw1R, blockw1S, blockw1T, blockw1U, blockw1V, blockw1W, blockw1X, blockw1Y, blockw1Z, blockw1AA, blockw1AB, blockw1AC, blockw1AD)
		starSprites = pygame.sprite.OrderedUpdates(starW1A, starW1B, starW1C, starW1D, starW1E, starW1F, starW1G, starW1H, starW1I, starW1J, starW1K, starW1L, starW1M)
		badSprites = pygame.sprite.Group(goombas)
		playerSprites = pygame.sprite.OrderedUpdates(player)
		scoreSprite = pygame.sprite.Group(scoreboard)

		level1B.rect.left = (level1A.rect.right - 1)
		
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

				
			if key[pygame.K_LEFT]:
				player.turn = 0
				player.image = pygame.image.load("walk L000.png")
				if collideLeft == False:
					if not level1A.rect.left == 0:
						level1A.moveLeft()
						level1B.moveLeft()
						qboxw1A.moveLeft()
						qboxw1B.moveLeft()
						qboxw1C.moveLeft()
						qboxw1D.moveLeft()
						qboxw1E.moveLeft()
						qboxw1F.moveLeft()
						qboxw1G.moveLeft()
						qboxw1H.moveLeft()
						qboxw1I.moveLeft()
						qboxw1J.moveLeft()
						qboxw1K.moveLeft()
						qboxw1L.moveLeft()
						qboxw1M.moveLeft()
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
						starW1A.moveLeft()
						starW1B.moveLeft()
						starW1C.moveLeft()
						starW1D.moveLeft()
						starW1E.moveLeft()
						starW1F.moveLeft()
						starW1G.moveLeft()
						starW1H.moveLeft()
						starW1I.moveLeft()
						starW1J.moveLeft()
						starW1K.moveLeft()
						starW1L.moveLeft()
						starW1M.moveLeft()
						for index in range(50):
							goombas[index].moveLeft()


			if key[pygame.K_RIGHT]:
				player.turn = 1
				player.image = pygame.image.load("walk R000.png")
				if collideRight == False:
					if level1B.rect.right > 1024:
						level1A.moveRight()
						level1B.moveRight()
						qboxw1A.moveRight()
						qboxw1B.moveRight()
						qboxw1C.moveRight()
						qboxw1D.moveRight()
						qboxw1E.moveRight()
						qboxw1F.moveRight()
						qboxw1G.moveRight()
						qboxw1H.moveRight()
						qboxw1I.moveRight()
						qboxw1J.moveRight()
						qboxw1K.moveRight()
						qboxw1L.moveRight()
						qboxw1M.moveRight()
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
						starW1A.moveRight()
						starW1B.moveRight()
						starW1C.moveRight()
						starW1D.moveRight()
						starW1E.moveRight()
						starW1F.moveRight()
						starW1G.moveRight()
						starW1H.moveRight()
						starW1I.moveRight()
						starW1J.moveRight()
						starW1K.moveRight()
						starW1L.moveRight()
						starW1M.moveRight()
						for index in range(50):
							goombas[index].moveRight()


						
			blockCollide = pygame.sprite.spritecollide(player, blockSprites, False)
			qboxCollide = pygame.sprite.spritecollide(player, QboxSprites, False)	
			starCollide = pygame.sprite.spritecollide(player, starSprites, True)
			
			if blockCollide:	
				for theBlock in blockCollide:
					if player.rect.bottom == (theBlock.rect.top + 1):
						player.floor = (theBlock.rect.top - 64)
			elif qboxCollide:	
				for theQbox in qboxCollide:
					if player.rect.bottom == (theQbox.rect.top + 1):
						player.floor = (theQbox.rect.top - 64)
			else:
				player.floor = 513

				
			ScoreMessage = "Your Score is: "
			
			if starCollide:
				scoreboard.score += 100
				print (ScoreMessage, score)
		
		
			player.calc_grav()
			
			playerSprites.update()
			badSprites.update()
			scoreSprite.update()
			backgroundSprites.update()
			QboxSprites.update()
			blockSprites.update()
			starSprites.update()

			backgroundSprites.draw(screen)
			QboxSprites.draw(screen)
			blockSprites.draw(screen)
			starSprites.draw(screen)
			scoreSprite.draw(screen)
			badSprites.draw(screen)
			playerSprites.draw(screen)


			pygame.display.flip()

		pygame.mouse.set_visible(True)

if __name__ == "__main__":
	main()