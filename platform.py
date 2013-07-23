
import pygame
from pygame.locals import *

MAN_SCREEN_MARGIN = 95       # pixels
JUMPING_DURATION = 1000      # milliseconds
HORZ_MOVE_INCREMENT = 10     # pixels
TIME_AT_PEAK = JUMPING_DURATION / 2
JUMP_HEIGHT = 300            # pixels

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1024, 672), 0)
pygame.display.set_caption('Super Mario Bros. Cousin Alfonso')
man = pygame.image.load('walk R000.png').convert_alpha()
background = pygame.image.load('world1(1).png')
background2 = pygame.image.load('world1(2).png')
groundA = pygame.image.load('world1(1)groundA.png')
pipeA = pygame.image.load('small_pipe.png')
pipeB = pygame.image.load('large_pipe.png')
pipeC = pygame.image.load('large_pipe.png')
pipeD = pygame.image.load('large_pipe.png')
pipeE = pygame.image.load('large_pipe.png')
pipeF = pygame.image.load('large_pipe.png')
QboxA = pygame.image.load('Q_box.png')
QboxB = pygame.image.load('Q_box.png')
QboxC = pygame.image.load('Q_box.png')
QboxD = pygame.image.load('Q_box.png')
QboxE = pygame.image.load('Q_box.png')
QboxF = pygame.image.load('Q_box.png')

def floorY():
	return screen.get_height() - man.get_height() - MAN_SCREEN_MARGIN

def jumpHeightAtTime(elapsedTime):
	return ((-1.0/TIME_AT_PEAK**2)* \
		((elapsedTime-TIME_AT_PEAK)**2)+1)*JUMP_HEIGHT

jumping = False
jumpingHorz = 0
manX = screen.get_width() / 2.5
manY = floorY()
backgroundX = 0
backgroundY = -223
groundAX = 0 
groundAY = 577
pipeAX = 1791
pipeAY = 449
pipeBX = 2431
pipeBY = 383
pipeCX = 2943
pipeCY = 319
pipeDX = 3648
pipeDY = 319
pipeEX = 4803
pipeEY = 449
pipeFX = 5827
pipeFY = 449
QboxAX = 1023
QboxAY = 320
QboxBX = 1342
QboxBY = 320
QboxCX = 1471
QboxCY = 320
QboxDX = 1406
QboxDY = 63
QboxEX = 4991
QboxEY = 320
QboxFX = 6016
QboxFY = 63

loop = True
while loop:
	for event in pygame.event.get():
		if event.type == QUIT \
			or (event.type == KEYDOWN and event.key == K_ESCAPE):
			loop = False

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT]:
		man = pygame.image.load('walk L000.png').convert_alpha()
		
	if keys[pygame.K_RIGHT]:
		man = pygame.image.load('walk R000.png').convert_alpha()

	def horzMoveAmt():
		return (keys[K_RIGHT] - keys[K_LEFT]) * HORZ_MOVE_INCREMENT

	if not jumping:
		if keys[pygame.K_RIGHT]:
			if not backgroundX == -5630:
				backgroundX -= horzMoveAmt()
				groundAX -= horzMoveAmt()
				pipeAX -= horzMoveAmt()
				pipeBX -= horzMoveAmt()
				pipeCX -= horzMoveAmt()
				pipeDX -= horzMoveAmt()
				pipeEX -= horzMoveAmt()
				pipeFX -= horzMoveAmt()
				QboxAX -= horzMoveAmt()
				QboxBX -= horzMoveAmt()
				QboxCX -= horzMoveAmt()
				QboxDX -= horzMoveAmt()
				QboxEX -= horzMoveAmt()
				QboxFX -= horzMoveAmt()
				
		
		if keys[pygame.K_LEFT]:
			if not backgroundX == 0:
				backgroundX -= horzMoveAmt()
				groundAX -= horzMoveAmt()
				pipeAX -= horzMoveAmt()
				pipeBX -= horzMoveAmt()
				pipeCX -= horzMoveAmt()
				pipeDX -= horzMoveAmt()
				pipeEX -= horzMoveAmt()
				pipeFX -= horzMoveAmt()
				QboxAX -= horzMoveAmt()
				QboxBX -= horzMoveAmt()
				QboxCX -= horzMoveAmt()
				QboxDX -= horzMoveAmt()
				QboxEX -= horzMoveAmt()
				QboxFX -= horzMoveAmt()
				
		
		if keys[K_SPACE]:
			jumping = True
			jumpingStart = pygame.time.get_ticks()

	if jumping:
		t = pygame.time.get_ticks() - jumpingStart
		if t > JUMPING_DURATION:
			jumping = False
			jumpHeight = 0
		else:
			jumpHeight = jumpHeightAtTime(t)

		manY = floorY() - jumpHeight
		
		if keys[pygame.K_RIGHT]:
			if not backgroundX == -5630:
				backgroundX -= horzMoveAmt()
				groundAX -= horzMoveAmt()
				pipeAX -= horzMoveAmt()
				pipeBX -= horzMoveAmt()
				pipeCX -= horzMoveAmt()
				pipeDX -= horzMoveAmt()
				pipeEX -= horzMoveAmt()
				pipeFX -= horzMoveAmt()
				QboxAX -= horzMoveAmt()
				QboxBX -= horzMoveAmt()
				QboxCX -= horzMoveAmt()
				QboxDX -= horzMoveAmt()
				QboxEX -= horzMoveAmt()
				QboxFX -= horzMoveAmt()
				
		
		if keys[pygame.K_LEFT]:
			if not backgroundX == 0:
				backgroundX -= horzMoveAmt()
				groundAX -= horzMoveAmt()
				pipeAX -= horzMoveAmt()
				pipeBX -= horzMoveAmt()
				pipeCX -= horzMoveAmt()
				pipeDX -= horzMoveAmt()
				pipeEX -= horzMoveAmt()
				pipeFX -= horzMoveAmt()
				QboxAX -= horzMoveAmt()
				QboxBX -= horzMoveAmt()
				QboxCX -= horzMoveAmt()
				QboxDX -= horzMoveAmt()
				QboxEX -= horzMoveAmt()
				QboxFX -= horzMoveAmt()
				
		
		
	screen.blit(background, (backgroundX, backgroundY))
	screen.blit(pipeA, (pipeAX, pipeAY))
	screen.blit(pipeB, (pipeBX, pipeBY))
	screen.blit(pipeC, (pipeCX, pipeCY))
	screen.blit(pipeD, (pipeDX, pipeDY))
	screen.blit(pipeE, (pipeEX, pipeEY))
	screen.blit(pipeF, (pipeFX, pipeFY))
	screen.blit(QboxA, (QboxAX, QboxAY))
	screen.blit(QboxB, (QboxBX, QboxBY))
	screen.blit(QboxC, (QboxCX, QboxCY))
	screen.blit(QboxD, (QboxDX, QboxDY))
	screen.blit(QboxE, (QboxEX, QboxEY))
	screen.blit(QboxF, (QboxFX, QboxFY))
	screen.blit(groundA, (groundAX, groundAY))
	screen.blit(man, (manX, manY))
	pygame.display.flip()
	clock.tick(50)
