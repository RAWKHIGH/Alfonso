
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
background2X = 1028
background2Y = -223
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
			print (backgroundX)
			if backgroundX >= -12240:
				backgroundX -= horzMoveAmt()
				groundAX -= horzMoveAmt()
				pipeAX -= horzMoveAmt()
				pipeBX -= horzMoveAmt()
				pipeCX -= horzMoveAmt()
				pipeDX -= horzMoveAmt()
				QboxAX -= horzMoveAmt()
				QboxBX -= horzMoveAmt()
				QboxCX -= horzMoveAmt()
				QboxDX -= horzMoveAmt()
				QboxEX -= horzMoveAmt()
				QboxFX -= horzMoveAmt()
				if backgroundX <= -5630:
					background2X -= horzMoveAmt()
					pipeEX -= horzMoveAmt()
					pipeFX -= horzMoveAmt()
						
		if keys[pygame.K_LEFT]:
			if backgroundX < 0:
				backgroundX -= horzMoveAmt()
				groundAX -= horzMoveAmt()
				pipeAX -= horzMoveAmt()
				pipeBX -= horzMoveAmt()
				pipeCX -= horzMoveAmt()
				pipeDX -= horzMoveAmt()
				QboxAX -= horzMoveAmt()
				QboxBX -= horzMoveAmt()
				QboxCX -= horzMoveAmt()
				QboxDX -= horzMoveAmt()
				QboxEX -= horzMoveAmt()
				QboxFX -= horzMoveAmt()
				if backgroundX <= -5630:
					background2X -= horzMoveAmt()
					pipeEX -= horzMoveAmt()
					pipeFX -= horzMoveAmt()
				
		
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
			if backgroundX >= -12240:
				backgroundX -= horzMoveAmt()
				groundAX -= horzMoveAmt()
				pipeAX -= horzMoveAmt()
				pipeBX -= horzMoveAmt()
				pipeCX -= horzMoveAmt()
				pipeDX -= horzMoveAmt()
				QboxAX -= horzMoveAmt()
				QboxBX -= horzMoveAmt()
				QboxCX -= horzMoveAmt()
				QboxDX -= horzMoveAmt()
				QboxEX -= horzMoveAmt()
				QboxFX -= horzMoveAmt()
				if backgroundX <= -5630:
					background2X -= horzMoveAmt()
					pipeEX -= horzMoveAmt()
					pipeFX -= horzMoveAmt()
				
		
		if keys[pygame.K_LEFT]:
			if backgroundX < 0:
				backgroundX -= horzMoveAmt()
				groundAX -= horzMoveAmt()
				pipeAX -= horzMoveAmt()
				pipeBX -= horzMoveAmt()
				pipeCX -= horzMoveAmt()
				pipeDX -= horzMoveAmt()
				QboxAX -= horzMoveAmt()
				QboxBX -= horzMoveAmt()
				QboxCX -= horzMoveAmt()
				QboxDX -= horzMoveAmt()
				QboxEX -= horzMoveAmt()
				QboxFX -= horzMoveAmt()
				if backgroundX <= -5630:
					background2X -= horzMoveAmt()
					pipeEX -= horzMoveAmt()
					pipeFX -= horzMoveAmt()
				
		
		'''
					if key[pygame.K_LEFT]:
				player.turn = 0
				player.image = pygame.image.load("walk L000.png")
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
					starW1A.moveLeft()
					starW1B.moveLeft()
					starW1C.moveLeft()
					starW1D.moveLeft()
					starW1E.moveLeft()
					starW1F.moveLeft()
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
						starW1G.moveLeft()
						starW1H.moveLeft()
						starW1I.moveLeft()
						starW1J.moveLeft()
						starW1K.moveLeft()
						starW1L.moveLeft()
						starW1M.moveLeft()

			if key[pygame.K_RIGHT]:
				player.turn = 1
				player.image = pygame.image.load("walk R000.png")
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
					starW1A.moveRight()
					starW1B.moveRight()
					starW1C.moveRight()
					starW1D.moveRight()
					starW1E.moveRight()
					starW1F.moveRight()
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
						starW1G.moveRight()
						starW1H.moveRight()
						starW1I.moveRight()
						starW1J.moveRight()
						starW1K.moveRight()
						starW1L.moveRight()
						starW1M.moveRight()
		'''
		
		
		
	screen.blit(background, (backgroundX, backgroundY))
	screen.blit(background2, (background2X, background2Y))
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
