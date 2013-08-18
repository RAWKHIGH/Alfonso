# Name: Stephen McArthur
# Purpose: Final Project. Create game with 3 levels (Easy, Medium, Hard) and a Boss level
# GitHub: https://github.com/RAWKHIGH/Alfonso.git

import pygame, random, sys
from pygame import *
from pygame.sprite import *

pygame.init()

black    = (  0,  0,  0)
white    = (255,255,255)
green    = (  0,255,  0)
red      = (255,  0,  0)

screen = pygame.display.set_mode((1024, 672))

SCORE = 0
globalLives = 5

class Alfonso(pygame.sprite.Sprite):

	change_x = 0
	change_y = 0

	frame_since_collision = 0
	frame_since_jump = 0
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("walk R000.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.turn = 1
		self.dx = 10
		self.rect.bottom = 320
		self.jump_ready = False
		self.floor = 513
		self.mask = pygame.mask.from_surface(self.image)
		
		self.rightImage = []
		self.leftImage = []
		self.loadPics()
		self.frame = 0
		self.delay = 4
		self.pause = self.delay
		self.moving = False

	def loadPics(self):
		for i in range(4):
			rightImgName = "walk R00{0}.png".format(i)
			leftImgName = "walk L00{0}.png".format(i)
			rightTmpImg = pygame.image.load(rightImgName)
			leftTmpImg = pygame.image.load(leftImgName)
			rightTmpImg.convert_alpha()
			leftTmpImg.convert_alpha()
			self.rightImage.append(rightTmpImg)
			self.leftImage.append(leftTmpImg)

	def changespeed_x(self,x):
		self.change_x = x

	def changespeed_y(self,y):
		self.change_y = y

	def update(self): 
		self.rect.centerx = 450

		old_y = self.rect.y 
		new_y = old_y + self.change_y 
		self.rect.y = new_y

		if self.jump_ready == True:
			if self.frame_since_collision < 6 and self.frame_since_jump < 6:
				self.frame_since_jump = 100
				self.change_y -= 16.5
				

		self.frame_since_collision+=1
		self.frame_since_jump+=1
		
		self.pause -= 1
		if self.pause <= 0:
			self.pause = self.delay
			
			self.frame += 1
			if self.frame > 3:
				self.frame = 0
			if self.moving:	
				if self.turn == 1:
					self.image = self.rightImage[self.frame]
				elif self.turn == 0:
					self.image = self.leftImage[self.frame]
				self.moving = False
			else:
				if self.turn == 1:
					self.image = pygame.image.load("walk R000.png")
				elif self.turn == 0:
					self.image = pygame.image.load("walk L000.png")
			#if self.jump_ready == True:
			#	if self.turn == 1:
			#		self.image = pygame.image.load("jump R000.png")
			#	elif self.turn == 0:
			#		self.image = pygame.image.load("jump L000.png")	
		
	def moveRight(self):
		self.rect.left -= self.dx
		
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

class World2A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world2(1).png")
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

class World2B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world2(2).png")
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
		
class World3A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world3(1).png")
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

class World3B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("world3(2).png")
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
		self.rect.left = 5200
		
class Scoreboard(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.lives = 5
		self.score = 0
		self.time = 180
		self.font = pygame.font.SysFont("None", 30)
		
	def update(self):
		minutes = self.time / 60
		seconds = self.time%60
		
		self.text = " Alfonso x%d              TIME: %d:%d               Score: %d " % (self.lives, minutes, seconds, self.score)
		self.image = self.font.render(self.text, 1, (red))
		self.rect = self.image.get_rect()
		self.rect.centerx = screen.get_rect().centerx
		self.rect.centery = 20
	
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
		
class Mushroom(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("mushroom.png")
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
		
class Flag(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("flag.png")
		self.image = self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.mask = pygame.mask.from_surface(self.image)
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.x = 12642
		self.rect.y = 96
		
class Goomba(pygame.sprite.Sprite):
	def __init__(self, centerx):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("goomba000.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.calcMove()
		self.centerx = centerx
		self.mask = pygame.mask.from_surface(self.image)
		self.walkImage = []
		self.loadPics()
		self.frame = 0
		self.delay = 2
		self.pause = self.delay
		self.reset()
	
	def calcMove(self):
		self.speed = random.randint(1,5)
		self.dir = random.randint(0,1)
		if self.dir	== 0:
			self.dir = -1
		self.speed *= self.dir
	
	def loadPics(self):
		for i in range(2):
			walkImgName = "goomba00{0}.png".format(i)
			walkTmpImg = pygame.image.load(walkImgName)
			walkTmpImg.convert_alpha()
			self.walkImage.append(walkTmpImg)
	
	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.bottom = screen.get_height() - 95
		self.rect.centerx = self.centerx
	
	def update(self):
		self.rect.centerx += self.speed
		self.pause -= 1
		if self.pause <= 0:
			self.pause = self.delay
			
			self.frame += 1
			if self.frame > 2:
				self.frame = 0
				self.image = self.walkImage[self.frame]

class Cloud(pygame.sprite.Sprite):
	def __init__(self, centerx, centery):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("cloud.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.calcMove()
		self.centerx = centerx
		self.centery = centery
		self.mask = pygame.mask.from_surface(self.image)
		self.walkImage = []
		self.frame = 0
		self.delay = 2
		self.pause = self.delay
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
		self.rect.centery = self.centery
	
	def update(self):
		self.rect.centerx += self.speed
		self.pause -= 1

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
		
class BlockT(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("blockT.png")
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

class GrassTop(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("grassTop.png")
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
		
class GrassTopBig(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("grassTopBig.png")
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

class GroundW2A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("groundW2A.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.mask = pygame.mask.from_surface(self.image)
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.x = 0
		self.rect.y = screen.get_height() - 94

class GroundW2B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("groundW2B.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.mask = pygame.mask.from_surface(self.image)
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.x = 8221
		self.rect.y = screen.get_height() - 96

class GroundW3A(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("groundW3A.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.mask = pygame.mask.from_surface(self.image)
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.x = 0
		self.rect.y = screen.get_height() - 94

class GroundW3B(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("groundW3B.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		self.mask = pygame.mask.from_surface(self.image)
		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	def reset(self):
		self.rect.x = 8221
		self.rect.y = screen.get_height() - 96
	
def splashScreen():
	screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
	pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")
	
	splash_image = pygame.image.load("SMBCA Splash Screen.png").convert()
	screen.blit(splash_image, [128 , 0])
	counter = 0
	keepGoing = True
	clock = pygame.time.Clock()
	pygame.mouse.set_visible(True)
	while keepGoing:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
	
		counter = counter + 1
		if counter == 60:
			print("Switching")
			currentScreen = instructionScreen()
				
					
		pygame.display.flip()
	
	pygame.mouse.set_visible(True)
	return donePlaying

def instructionScreen():
	screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
	pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")
	
	instruction_image = pygame.image.load("instructions.png").convert()
	screen.blit(instruction_image, [0 , 0])
	keepGoing = True
	clock = pygame.time.Clock()
	pygame.mouse.set_visible(True)
	while keepGoing:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				print ("Switching")
				currentScreen = helpScreen_lv1()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()				
					
		pygame.display.flip()
	
	pygame.mouse.set_visible(True)
	return donePlaying

def helpScreen_lv1():
	screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
	pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")
	helpScreen_image = pygame.image.load("helpScreen.png").convert()
	screen.blit(helpScreen_image, [0 , 0])
	keepGoing = True
	clock = pygame.time.Clock()
	pygame.mouse.set_visible(True)
	while keepGoing:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				print ("Switching")
				currentScreen = level_1()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
					
		pygame.display.flip()
	
	pygame.mouse.set_visible(True)
	return donePlaying
	
def level_1():
	screen = pygame.display.set_mode((1024, 768))
	#, pygame.FULLSCREEN
	pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")

	background = pygame.Surface(screen.get_size())
	background.fill((0, 0, 0))
	screen.blit(background, (0, 0))

	counter = 0
	time = 180
	flagcounter = 0
	
	player = Alfonso()
	level1A = World1A()
	level1B = World1B()
	flag = Flag()
	stars = []
	goombas = []
	blocks = []
	qboxs = []
	
	scoreboard = Scoreboard() 
	flagFloor = player.rect.y
	flag.rect.x = 12642

	for goomba in range(100):
		goombax = random.randint(level1A.rect.left, (level1B.rect.right - 1278))
		goombas.append(Goomba(goombax))	
		
	BLpos = 0
	for block in range(44):
		# XY POS   0     1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26     27     28     29   30    31   32    33    34    35    36    37    38    39     40     41     42     43 
		blockx = [1278, 1406, 1534, 4927, 5056, 5120, 5184, 5248, 5312, 5376, 5440, 5504, 5568, 5824, 5888, 5952, 6016, 6400, 6464, 7556, 7747, 7811, 7875, 8196, 8387, 8260, 8324, 10755, 10819, 10948, 450, 844, 2176, 2692, 3104, 3902, 4168, 9190, 9394, 9955, 10586, 11230, 11575, 12130]
		blocky = [ 416,  416,  416,  416,  416,  159,  159,  159,  159,  159,  159,  159,  159,  159,  159,  159,  416,  416,  416,  416,  159,  159,  159,  159,  159,  416,  416,   416,   416,   416, 416, 159,  416,  416,  159,  416,  159,  416,  159,  159,   416,   159,   159,   159]
		blocks.append(Block(blockx[BLpos], blocky[BLpos]))
		BLpos += 1
			
	QLpos = 0
	for qbox in range(13):
		# XY POS  0     1     2     3     4     5     6     7     8     9     10    11    12
		qboxx = [1023, 1342, 1471, 1406, 4991, 6016, 6787, 6979, 7171, 6979, 8260, 8324, 10884]
		qboxy = [ 416,  416,  416,  159,  416,  159,  416,  416,  416,  159,  159,  159,   416]
		qboxs.append(Qbox(qboxx[QLpos], qboxy[QLpos]))
		QLpos += 1
		
	SLpos = 0
	for star in range(13):
		# XY POS  0     1     2     3     4     5     6     7     8     9     10    11    12
		starx = [1040, 1359, 1488, 1423, 5008, 6033, 6804, 6996, 7188, 6996, 8277, 8341, 10901]
		stary = [ 366,  366,  366,  109,  366,  109,  366,  366,  366,  109,  109,  109,   366]
		stars.append(Star(starx[SLpos], stary[SLpos]))
		SLpos += 1
			
	backgroundSprites = pygame.sprite.OrderedUpdates(level1B, level1A)
	QboxSprites = pygame.sprite.OrderedUpdates(qboxs)
	blockSprites = pygame.sprite.Group(blocks)
	starSprites = pygame.sprite.OrderedUpdates(stars)
	badSprites = pygame.sprite.Group(goombas)
	playerSprites = pygame.sprite.OrderedUpdates(player)
	scoreSprite = pygame.sprite.Group(scoreboard)
	flagSprites = pygame.sprite.OrderedUpdates(flag)

	level1B.rect.left = (level1A.rect.right)
		
	collideFlag = False
	Level_Finish_1 = False
	timer = True
		
	clock = pygame.time.Clock()
	keepGoing = True
	while keepGoing:
		clock.tick(30)
		key = pygame.key.get_pressed()
		jumping = False
		pygame.mouse.set_visible(False)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					if collideFlag == False:
						player.jump()

				
		if key[pygame.K_LEFT]:
			player.turn = 0
			if collideFlag == False:
				if not level1A.rect.left == 0:
					player.moving = True
					level1A.moveLeft()
					level1B.moveLeft()
					flag.moveLeft()
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
			if collideFlag == False:
				if level1B.rect.right > 1024:
					player.moving = True
					level1A.moveRight()
					level1B.moveRight()
					flag.moveRight()
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
		flagCollide = pygame.sprite.spritecollide(player, flagSprites, False, pygame.sprite.collide_mask)
		
		if blockCollide:	
			for theBlock in blockCollide:
				if collide_mask(player, theBlock):
					player.floor = (theBlock.rect.top - 64)
		elif qboxCollide:	
			for theQbox in qboxCollide:
				if collide_mask(player, theQbox):
					player.floor = (theQbox.rect.top - 64)
		else:
			player.floor = screen.get_height() - 95
		
		if starCollide:
			scoreboard.score += 100
			
		if 	flagCollide:
			player.floor = flagFloor
			collideFlag = True
			Level_Finish_1 = True
			flagcounter = flagcounter + 1

		if Level_Finish_1 == True:
			if flagcounter == 1:
				flagFloor = flagFloor + 1
				flagcounter = 0
				timer = False
				if scoreboard.time != 0:
					scoreboard.time -= 1
				if player.rect.bottom >= 673:
					flagFloor = 609
					if scoreboard.time == 0:
						print ("Switching")
						currentScreen = level_2(scoreboard)
					
		if timer == False:
			timeMoney = scoreboard.time
			timeMoney *= 10
			scoreboard.score += timeMoney
		
		for goomba in goombas:
			if goomba.rect.left >= level1A.rect.left:
				goomba.speed *= -1
			if goomba.rect.left <= (level1B.rect.right - 1278):
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
					flag.reset()
	
		if timer == True:
			counter = counter + 1
		if timer == True and counter == 30:
			time -= 1
			counter = 0
			scoreboard.time = time
		
		player.calc_grav()
			
		playerSprites.update()
		badSprites.update()
		scoreSprite.update()
		backgroundSprites.update()
		QboxSprites.update()
		blockSprites.update()
		starSprites.update()
		flagSprites.update()

		backgroundSprites.draw(screen)
		QboxSprites.draw(screen)
		blockSprites.draw(screen)
		starSprites.draw(screen)
		flagSprites.draw(screen)
		scoreSprite.draw(screen)
		badSprites.draw(screen)
		playerSprites.draw(screen)


		pygame.display.flip()

	pygame.mouse.set_visible(True)

def level_2(scoreboard):
	screen = pygame.display.set_mode((1024, 768))
	#, pygame.FULLSCREEN
	pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")

	background = pygame.Surface(screen.get_size())
	background.fill((0, 0, 0))
	screen.blit(background, (0, 0))

	counter = 0
	time = 180
	flagcounter = 0
	
	player = Alfonso()
	level2A = World2A()
	level2B = World2B()
	grassTop = []
	grassTopBig = []
	qBox = []
	mushroom = []
	clouds = []
	flag = Flag()
	groundW2A = GroundW2A()
	groundW2B = GroundW2B()
	
	flagFloor = player.rect.y	
	flag.rect.x = 9664
	
	for cloud in range(20):
		cloudx = random.randint((level2A.rect.left + 1024), (level2B.rect.right - 1278))
		cloudy = random.randint(0, screen.get_height())
		clouds.append(Cloud(cloudx, cloudy))	
	
	GTLpos = 0
	for grastop in range(13):
		# XY POS        0     1     2     3     4     5     6     7     8     9     10    11    12
		grassTopx = [ 1129, 1675, 1999, 2251, 3180, 3821, 3788, 4172, 4431, 6221, 7147, 7372, 7759]
		grassTopy = [  601,  155,  601,  353,  665,  155,  665,  665,  414,  537,  665,  414,  414]
		grassTop.append(GrassTop(grassTopx[GTLpos], grassTopy[GTLpos]))
		GTLpos += 1
		
	GTBLpos = 0
	for grastopbig in range(4):
		# XY POS           0     1     2     3      
		grassTopBigx = [ 1535, 2528, 4801, 6622]
		grassTopBigy = [  416,   96,  223,  287]
		grassTopBig.append(GrassTopBig(grassTopBigx[GTBLpos], grassTopBigy[GTBLpos]))
		GTBLpos += 1

	for box in range(1):
		qBox.append(Qbox(5752, 536))
		
	for mush in range(1):
		mushroom.append(Mushroom(5769, 486))
	
	backgroundSprites = pygame.sprite.OrderedUpdates(level2B, level2A)
	grassSprites = pygame.sprite.OrderedUpdates(grassTop, grassTopBig)
	qboxSprites = pygame.sprite.OrderedUpdates(qBox)
	mushroomSprites = pygame.sprite.OrderedUpdates(mushroom)
	playerSprites = pygame.sprite.OrderedUpdates(player)
	scoreSprite = pygame.sprite.Group(scoreboard)
	flagSprites = pygame.sprite.OrderedUpdates(flag)
	groundSprites = pygame.sprite.OrderedUpdates(groundW2A, groundW2B)
	CloudSprites = pygame.sprite.Group(clouds)

	level2B.rect.left = (level2A.rect.right)
		
	collideFlag = False
	Level_Finish_2 = False
	timer = True
	
	clock = pygame.time.Clock()
	keepGoing = True
	while keepGoing:
		clock.tick(30)
		key = pygame.key.get_pressed()
		jumping = False
		collideLeft = False
		collideRight = False
		player.floor = (screen.get_height() + 80)
		pygame.mouse.set_visible(False)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player.jump()

				
		if key[pygame.K_LEFT]:
			player.turn = 0
			if collideFlag == False:
				if not level2A.rect.left == 0:
					player.moving = True
					level2A.moveLeft()
					level2B.moveLeft()
					flag.moveLeft()
					groundW2A.moveLeft()
					groundW2B.moveLeft()
					for index in range(13):
						grassTop[index].moveLeft()
					for index in range(4):
						grassTopBig[index].moveLeft()
					for index in range(1):
						qBox[index].moveLeft()
					for index in range(1):
						mushroom[index].moveLeft()
					for index in range(20):
						clouds[index].moveLeft()

		if key[pygame.K_RIGHT]:
			player.turn = 1
			if collideFlag == False:
				if level2B.rect.right > 1024:
					player.moving = True
					level2A.moveRight()
					level2B.moveRight()
					flag.moveRight()
					groundW2A.moveRight()
					groundW2B.moveRight()
					for index in range(13):
						grassTop[index].moveRight()
					for index in range(4):
						grassTopBig[index].moveRight()
					for index in range(1):
						qBox[index].moveRight()
					for index in range(1):
						mushroom[index].moveRight()
					for index in range(20):
						clouds[index].moveRight()
										
		flagCollide = pygame.sprite.spritecollide(player, flagSprites, False, pygame.sprite.collide_mask)
		groundCollide = pygame.sprite.spritecollide(player, groundSprites, False, pygame.sprite.collide_mask)
		grassCollide = pygame.sprite.spritecollide(player, grassSprites, False, pygame.sprite.collide_mask)
		qboxCollide = pygame.sprite.spritecollide(player, qboxSprites, False, pygame.sprite.collide_mask)
		mushroomCollide = pygame.sprite.spritecollide(player, mushroomSprites, True, pygame.sprite.collide_mask)
		cloudCollide = pygame.sprite.spritecollide(player, CloudSprites, True, pygame.sprite.collide_mask)
		
		if groundCollide:	
			for theGround in groundCollide:
				if collide_mask(player, theGround):
					player.floor = (theGround.rect.top - 64)
					
		if grassCollide:	
			for theGrass in grassCollide:
				if collide_mask(player, theGrass):
					player.floor = (theGrass.rect.top - 64)
		
		if qboxCollide:	
			for theqBox in qboxCollide:
				if collide_mask(player, theqBox):
					player.floor = (theqBox.rect.top - 64)
					
		if mushroomCollide:
			print("Colide Mushroom")
			for theMush in mushroomCollide:
				if collide_mask(player, theMush):
					scoreboard.lives += 1
		
		if 	flagCollide:
			player.floor = flagFloor
			collideFlag = True
			Level_Finish_2 = True
			flagcounter = flagcounter + 1

		for cloud in clouds:
			if cloud.rect.centerx > (level2B.rect.right - 1278):
				cloud.reset()
			if cloud.rect.left >= (level2A.rect.left + 1025):
				cloud.speed *= -1
			if cloud.rect.left <= (level2B.rect.right - 1278):
				cloud.speed *= -1
					
		if cloudCollide:	
			for theCloud in cloudCollide:
				if collide_mask(player, theCloud):
					print ("dead")
					scoreboard.score = 0
					scoreboard.lives -= 1
					for index in range(1):
						qBox[index].reset()
					for index in range(1):
						mushroom[index].reset()
					for index in range(13):
						grassTop[index].reset()
					for index in range(4):
						grassTopBig[index].reset()	
					player.reset()
					level2A.reset()
					level2B.reset()
					flag.rect.x = 9664
					groundW2A.reset()
					groundW2B.reset()
					
		if player.rect.top >= screen.get_height() + 1:
			print ("dead")
			scoreboard.score = 0
			scoreboard.lives -= 1
			for index in range(1):
				qBox[index].reset()
			for index in range(1):
				mushroom[index].reset()
			for index in range(13):
				grassTop[index].reset()
			for index in range(4):
				grassTopBig[index].reset()	
			player.reset()
			level2A.reset()
			level2B.reset()
			flag.rect.x = 9664
			groundW2A.reset()
			groundW2B.reset()
			
		if Level_Finish_2 == True:
			if flagcounter == 1:
				flagFloor = flagFloor + 1
				flagcounter = 0
				timer = False
				if scoreboard.time != 0:
					scoreboard.time -= 1
				if player.rect.bottom >= 673:
					flagFloor = 609
					if scoreboard.time == 0:
						print ("Switching")
						currentScreen = level_3(scoreboard)
					
		if timer == False:
			timeMoney = scoreboard.time
			timeMoney *= 10
			scoreboard.score += timeMoney
		
				
		if timer == True:
			counter = counter + 1
		if timer == True and counter == 30:
			time -= 1
			counter = 0
			scoreboard.time = time
		
		player.calc_grav()
			
		playerSprites.update()
		grassSprites.update()
		scoreSprite.update()
		backgroundSprites.update()
		flagSprites.update()
		qboxSprites.update()
		mushroomSprites.update()
		groundSprites.update()
		CloudSprites.update()

		backgroundSprites.draw(screen)
		grassSprites.draw(screen)
		flagSprites.draw(screen)
		qboxSprites.draw(screen)
		mushroomSprites.draw(screen)
		groundSprites.draw(screen)
		CloudSprites.draw(screen)
		scoreSprite.draw(screen)
		playerSprites.draw(screen)
		
		pygame.display.flip()
		
	pygame.mouse.set_visible(True)

	
def level_3(scoreboard):
	screen = pygame.display.set_mode((1024, 768))
	#, pygame.FULLSCREEN
	pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")

	background = pygame.Surface(screen.get_size())
	background.fill((0, 0, 0))
	screen.blit(background, (0, 0))

	counter = 0
	time = 180
	flagcounter = 0
	
	player = Alfonso()
	level3A = World3A()
	level3B = World3B()
	qBox = []
	mushroom = []
	flag = Flag()
	groundW3A = GroundW3A()
	groundW3B = GroundW3B()
	
	flagFloor = player.rect.y	
	flag.rect.x = 9664

	for box in range(1):
		qBox.append(Qbox(5752, 536))
		
	for mush in range(1):
		mushroom.append(Mushroom(5769, 486))
	
	backgroundSprites = pygame.sprite.OrderedUpdates(level3B, level3A)
	qboxSprites = pygame.sprite.OrderedUpdates(qBox)
	mushroomSprites = pygame.sprite.OrderedUpdates(mushroom)
	playerSprites = pygame.sprite.OrderedUpdates(player)
	scoreSprite = pygame.sprite.Group(scoreboard)
	flagSprites = pygame.sprite.OrderedUpdates(flag)
	groundSprites = pygame.sprite.OrderedUpdates(groundW3A, groundW3B)

	level3B.rect.left = (level3A.rect.right)
		
	collideFlag = False
	Level_Finish_3 = False
	timer = True
	
	clock = pygame.time.Clock()
	keepGoing = True
	while keepGoing:
		clock.tick(30)
		key = pygame.key.get_pressed()
		jumping = False
		collideLeft = False
		collideRight = False
		player.floor = (screen.get_height() + 80)
		pygame.mouse.set_visible(False)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player.jump()

				
		if key[pygame.K_LEFT]:
			player.turn = 0
			if collideFlag == False:
				if not level3A.rect.left == 0:
					player.moving = True
					level3A.moveLeft()
					level3B.moveLeft()
					flag.moveLeft()
					groundW3A.moveLeft()
					groundW3B.moveLeft()
					for index in range(1):
						qBox[index].moveLeft()
					for index in range(1):
						mushroom[index].moveLeft()


		if key[pygame.K_RIGHT]:
			player.turn = 1
			if collideFlag == False:
				if level3B.rect.right > 1024:
					player.moving = True
					level3A.moveRight()
					level3B.moveRight()
					flag.moveRight()
					groundW3A.moveRight()
					groundW3B.moveRight()
					for index in range(1):
						qBox[index].moveRight()
					for index in range(1):
						mushroom[index].moveRight()
						
						
		flagCollide = pygame.sprite.spritecollide(player, flagSprites, False, pygame.sprite.collide_mask)
		groundCollide = pygame.sprite.spritecollide(player, groundSprites, False, pygame.sprite.collide_mask)
		qboxCollide = pygame.sprite.spritecollide(player, qboxSprites, False, pygame.sprite.collide_mask)
		mushroomCollide = pygame.sprite.spritecollide(player, mushroomSprites, True, pygame.sprite.collide_mask)
		
		
		if groundCollide:	
			for theGround in groundCollide:
				if collide_mask(player, theGround):
					player.floor = (theGround.rect.top - 64)
		
		if qboxCollide:	
			for theqBox in qboxCollide:
				if collide_mask(player, theqBox):
					player.floor = (theqBox.rect.top - 64)
					
		if mushroomCollide:
			print("Colide Mushroom")
			for theMush in mushroomCollide:
				if collide_mask(player, theMush):
					scoreboard.lives += 1
		
		if 	flagCollide:
			player.floor = flagFloor
			collideFlag = True
			Level_Finish_3 = True
			flagcounter = flagcounter + 1

		if Level_Finish_3 == True:
			if flagcounter == 1:
				flagFloor = flagFloor + 1
				flagcounter = 0
				timer = False
				if scoreboard.time != 0:
					scoreboard.time -= 1
				if player.rect.bottom >= 673:
					flagFloor = 609
					if scoreboard.time == 0:
						print ("Switching")
						currentScreen = Boss_lvl(scoreboard)
					
		if timer == False:
			timeMoney = scoreboard.time
			timeMoney *= 10
			scoreboard.score += timeMoney
		
				
		if timer == True:
			counter = counter + 1
		if timer == True and counter == 30:
			time -= 1
			counter = 0
			scoreboard.time = time
		
		player.calc_grav()
			
		playerSprites.update()
		scoreSprite.update()
		backgroundSprites.update()
		flagSprites.update()
		qboxSprites.update()
		mushroomSprites.update()
		groundSprites.update()

		backgroundSprites.draw(screen)
		flagSprites.draw(screen)
		qboxSprites.draw(screen)
		mushroomSprites.draw(screen)
		groundSprites.draw(screen)
		scoreSprite.draw(screen)
		playerSprites.draw(screen)


		pygame.display.flip()
		
	pygame.mouse.set_visible(True)	
	
currentScreen = level_1()
	
def main():
	currentScreen	
if __name__ == "__main__":
    main()