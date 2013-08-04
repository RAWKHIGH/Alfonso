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
		
class Star(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("star.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
#		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

#	def reset(self):
#		self.rect.top = 270
#		self.rect.left = 10901
		
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
		
class Block(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("block.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
		#self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

	#def reset(self):
		#self.rect.top = 320
		#self.rect.left = 1278
		
class Qbox(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Q_box.png")
		self.image.set_colorkey(white)
		self.image = self.image.convert()
		self.rect = self.image.get_rect()
		self.dx = 10
#		self.reset()

	def moveRight(self):
		self.rect.left -= self.dx

	def moveLeft(self):
		self.rect.left += self.dx

#	def reset(self):
#		self.rect.top = 320
#		self.rect.left = 1023	
		
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
		stars = []
		goombas = []
		blocks = []
		qboxs = []
		
		scoreboard = Scoreboard()
		
		for goomba in range(50):
			goombax = random.randint(level1A.rect.left, level1B.rect.right)
			goombas.append(Goomba(goombax))	
			
		for block in range(30):
			blocks.append(Block())
			
		for qbox in range(30):
			qboxs.append(Qbox())
			
		for star in range(30):
			stars.append(Star())
		
		blocks[0].x = 1278
		blocks[0].y = 320
		blocks[1].x = 1406
		blocks[1].y = 320
		blocks[2].x = 1534
		blocks[2].y = 320
		blocks[3].x = 4927
		blocks[3].y = 320
		blocks[4].x = 5056
		blocks[4].y = 320
		blocks[5].x = 5120
		blocks[5].y = 63
		blocks[6].x = 5184
		blocks[6].y = 63
		blocks[7].x = 5248
		blocks[7].y = 63
		blocks[8].x = 5312
		blocks[8].y = 63
		blocks[9].x = 5376
		blocks[9].y = 63
		blocks[10].x = 5440
		blocks[10].y = 63
		blocks[11].x = 5504
		blocks[11].y = 63
		blocks[12].x = 5568
		blocks[12].y = 63
		blocks[13].x = 5824
		blocks[13].y = 63
		blocks[14].x = 5888
		blocks[14].y = 63
		blocks[15].x = 5952
		blocks[15].y = 63
		blocks[16].x = 6016
		blocks[16].y = 320
		blocks[17].x = 6400
		blocks[17].y = 320
		blocks[18].x = 6464
		blocks[18].y = 320
		blocks[19].x = 7556
		blocks[19].y = 320
		blocks[20].x = 7747
		blocks[20].y = 63
		blocks[21].x = 7811
		blocks[21].y = 63
		blocks[22].x = 7875
		blocks[22].y = 63
		blocks[23].x = 8196
		blocks[23].y = 63
		blocks[24].x = 8387
		blocks[24].y = 63
		blocks[25].x = 8260
		blocks[25].y = 320
		blocks[26].x = 8324
		blocks[26].y = 320
		blocks[27].x = 10755
		blocks[27].y = 320
		blocks[28].x = 10819
		blocks[28].y = 320
		blocks[29].x = 10948
		blocks[29].y = 320
			
		backgroundSprites = pygame.sprite.OrderedUpdates(level1B, level1A)
		QboxSprites = pygame.sprite.OrderedUpdates(qboxs)
		blockSprites = pygame.sprite.Group(blocks)
		starSprites = pygame.sprite.OrderedUpdates(stars)
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
						for index in range(30):
							stars[index].moveLeft()
						for index in range(50):
							goombas[index].moveLeft()
						for index in range(30):
							blocks[index].moveLeft()
						for index in range(30):
							qboxs[index].moveLeft()


			if key[pygame.K_RIGHT]:
				player.turn = 1
				player.image = pygame.image.load("walk R000.png")
				if collideRight == False:
					if level1B.rect.right > 1024:
						level1A.moveRight()
						level1B.moveRight()
						for index in range(30):
							stars[index].moveRight()
						for index in range(50):
							goombas[index].moveRight()
						for index in range(30):
							blocks[index].moveRight()
						for index in range(30):
							qboxs[index].moveRight()


						
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
			
			if starCollide:
				scoreboard.score += 100
			
			for goomba in goombas:
				if goomba.rect.left >= level1A.rect.left:
					goomba.speed *= -1
				if goomba.rect.left <= level1B.rect.right:
					goomba.speed *= -1
		
		
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