# Name: Stephen McArthur
# Purpose: Final Project. Create game with 3 levels (Easy, Medium, Hard) and a Boss level
# GitHub: https://github.com/RAWKHIGH/Alfonso.git

import pygame, random
from pygame import *
from pygame.sprite import *

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
		self.rect.bottom = 320
		self.jump_ready = False
		self.floor = 513
		self.mask = pygame.mask.from_surface(self.image)
		
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
	
	def reset(self):
		self.rect.bottom = 320
	
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
		self.rect.left = 0

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
		self.rect.left = 6658

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
		
class Star(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.dx = 10
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.x = self.x
		self.rect.y = self.y
		
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
		self.mask = pygame.mask.from_surface(self.image)
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
		
class Block(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.dx = 10
		self.mask = pygame.mask.from_surface(self.image)
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.x = self.x
		self.rect.y = self.y
		
class Qbox(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.dx = 10
		self.mask = pygame.mask.from_surface(self.image)
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.x = self.x
		self.rect.y = self.y	
		
def startScreen(score):
	screen = pygame.display.set_mode((1024, 672))
	pygame.display.set_caption("Cousin Alfonso Start Screen")
 
	keepGoing = True
	clock = pygame.time.Clock()
	pygame.mouse.set_visible(True)
	while keepGoing:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				keepGoing = False
				donePlaying = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				keepGoing = False
				donePlaying = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					keepGoing = False
					donePlaying = True

		pygame.display.flip()
  
	pygame.mouse.set_visible(True)
	return donePlaying

		
def level_1():
		screen = pygame.display.set_mode((1024, 672))
		pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")

		background = pygame.Surface(screen.get_size())
		background.fill((0, 0, 0))
		screen.blit(background, (0, 0))

		score = 0
		
		player = Alfonso()
		level1A = World1A()
		level1B = World1B()
		stars = []
		goombas = []
		blocks = []
		qboxs = []
		
		scoreboard = Scoreboard()
      
   
		
		for goomba in range(100):
			goombax = random.randint(level1A.rect.left, level1B.rect.right)
			goombas.append(Goomba(goombax))	
		
		BLpos = 0
		for block in range(44):
		    # XY POS   0     1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26     27     28     29   30    31   32    33    34    35    36    37    38    39     40     41     42     43 
			blockx = [1278, 1406, 1534, 4927, 5056, 5120, 5184, 5248, 5312, 5376, 5440, 5504, 5568, 5824, 5888, 5952, 6016, 6400, 6464, 7556, 7747, 7811, 7875, 8196, 8387, 8260, 8324, 10755, 10819, 10948, 450, 844, 2176, 2692, 3104, 3902, 4168, 9190, 9394, 9955, 10586, 11230, 11575, 12130]
			blocky = [ 320,  320,  320,  320,  320,   63,   63,   63,   63,   63,   63,   63,   63,   63,   63,   63,  320,  320,  320,  320,   63,   63,   63,   63,   63,  320,  320,   320,   320,   320, 320,  63,  320,  320,   63,  320,   63,  320,   63,   63,   320,    63,    63,    63]
			blocks.append(Block(blockx[BLpos], blocky[BLpos]))
			BLpos += 1
			
		QLpos = 0
		for qbox in range(13):
			# XY POS  0     1     2     3     4     5     6     7     8     9     10    11    12
			qboxx = [1023, 1342, 1471, 1406, 4991, 6016, 6787, 6979, 7171, 6979, 8260, 8324, 10884]
			qboxy = [ 320,  320,  320,   63,  320,   63,  320,  320,  320,   63,   63,   63,   320]
			qboxs.append(Qbox(qboxx[QLpos], qboxy[QLpos]))
			QLpos += 1
		
		SLpos = 0
		for star in range(13):
			# XY POS  0     1     2     3     4     5     6     7     8     9     10    11    12
			starx = [1040, 1359, 1488, 1423, 5008, 6033, 6804, 6996, 7188, 6996, 8277, 8341, 10901]
			stary = [ 270,  270,  270,   13,  270,   13,  270,  270,  270,   13,   13,   13,   270]
			stars.append(Star(starx[SLpos], stary[SLpos]))
			SLpos += 1
			
		backgroundSprites = pygame.sprite.OrderedUpdates(level1B, level1A)
		QboxSprites = pygame.sprite.OrderedUpdates(qboxs)
		blockSprites = pygame.sprite.Group(blocks)
		starSprites = pygame.sprite.OrderedUpdates(stars)
		badSprites = pygame.sprite.Group(goombas)
		playerSprites = pygame.sprite.OrderedUpdates(player)
		scoreSprite = pygame.sprite.Group(scoreboard)

		level1B.rect.left = (level1A.rect.right)
		
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
						for index in range(13):
							stars[index].moveLeft()
						for index in range(100):
							goombas[index].moveLeft()
						for index in range(44):
							blocks[index].moveLeft()
						for index in range(13):
							qboxs[index].moveLeft()


			if key[pygame.K_RIGHT]:
				player.turn = 1
				player.image = pygame.image.load("walk R000.png")
				if collideRight == False:
					if level1B.rect.right > 1024:
						level1A.moveRight()
						level1B.moveRight()
						for index in range(13):
							stars[index].moveRight()
						for index in range(100):
							goombas[index].moveRight()
						for index in range(44):
							blocks[index].moveRight()
						for index in range(13):
							qboxs[index].moveRight()


						
			blockCollide = pygame.sprite.spritecollide(player, blockSprites, False, pygame.sprite.collide_mask)
			qboxCollide = pygame.sprite.spritecollide(player, QboxSprites, False, pygame.sprite.collide_mask)	
			starCollide = pygame.sprite.spritecollide(player, starSprites, True, pygame.sprite.collide_mask)
			goombaCollide = pygame.sprite.spritecollide(player, badSprites, False, pygame.sprite.collide_mask)
			
			if blockCollide:	
				for theBlock in blockCollide:
					if collide_mask(player, theBlock):
						player.floor = (theBlock.rect.top - 64)
			elif qboxCollide:	
				for theQbox in qboxCollide:
					if collide_mask(player, theQbox):
						player.floor = (theQbox.rect.top - 64)
			else:
				player.floor = 513
			
			if starCollide:
				scoreboard.score += 100

			
			for goomba in goombas:
				if goomba.rect.left >= level1A.rect.left:
					goomba.speed *= -1
				if goomba.rect.left <= level1B.rect.right:
					goomba.speed *= -1
					
			if goombaCollide:	
				for theGoomba in goombaCollide:
					if collide_mask(player, theGoomba):
						print ("dead")
						scoreboard.score = 0
						scoreboard.lives -= 1
						for index in range(13):
							stars[index].reset()
						for index in range(100):
							goombas[index].reset()
						for index in range(44):
							blocks[index].reset()
						for index in range(13):
							qboxs[index].reset()
						player.reset()
						level1A.reset()
						level1B.reset()
			
		
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

def main():
	donePlaying = False
	score = 0
	while not donePlaying:
		donePlaying = startScreen(score)
		if not donePlaying:
			score = level_1()
			#donePlaying = gameOver(score)
if __name__ == "__main__":
    main()