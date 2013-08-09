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
		self.rect.y = 0
		
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
		
def splashScreen():
	screen = pygame.display.set_mode((1024, 672))
	pygame.display.set_caption("Cousin Alfonso Start Screen")
	
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
			currentScreen = level_1()
				
					
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
   	
	for goomba in range(100):
		goombax = random.randint(level1A.rect.left, (level1B.rect.right - 1278))
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
	flagSprites = pygame.sprite.OrderedUpdates(flag)

	level1B.rect.left = (level1A.rect.right)
		
	collideFlag = False
	Level_Finish_1 = False
		
	clock = pygame.time.Clock()
	keepGoing = True
	while keepGoing:
		clock.tick(30)
		key = pygame.key.get_pressed()
		jumping = False
		
		pygame.mouse.set_visible(False)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				keepGoing = False
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
			player.floor = 513
				
			
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
				if player.rect.bottom >= 577:
					flagFloor = 513
					print(flagFloor)
					print(player.rect.bottom)
					player.moveRight()
					if player.rect.left >= 600:
						print("Hit Castle")
					
		
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
							
		counter = counter + 1
		if counter == 30:
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

def level_2():
	screen = pygame.display.set_mode((1024, 672))
	pygame.display.set_caption("Super Mario Bros. Cousin Alfonso")

	background = pygame.Surface(screen.get_size())
	background.fill((0, 0, 0))
	screen.blit(background, (0, 0))
	
	score = 0
	counter = 0
	time = 180
	
	player = Alfonso()
	level2A = World2A()
	level2B = World2B()
	scoreboard = Scoreboard()      
	
	backgroundSprites = pygame.sprite.OrderedUpdates(level2B, level2A)
	playerSprites = pygame.sprite.OrderedUpdates(player)
	scoreSprite = pygame.sprite.Group(scoreboard)

	level2B.rect.left = (level2A.rect.right)
	
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
				if not level2A.rect.left == 0:
					level2A.moveLeft()
					level2B.moveLeft()

		if key[pygame.K_RIGHT]:
			player.turn = 1
			player.image = pygame.image.load("walk R000.png")
			if collideRight == False:
				if level2B.rect.right > 1024:
					level2A.moveRight()
					level2B.moveRight()			
						
		counter = counter + 1
		if counter == 30:
			time -= 1
			counter = 0
			scoreboard.time = time
		
		player.calc_grav()
			
		playerSprites.update()
		scoreSprite.update()
		backgroundSprites.update()

		backgroundSprites.draw(screen)
		scoreSprite.draw(screen)
		playerSprites.draw(screen)


		pygame.display.flip()
		
	pygame.mouse.set_visible(True)
	

currentScreen = splashScreen()
	
def main():
	currentScreen	
if __name__ == "__main__":
    main()