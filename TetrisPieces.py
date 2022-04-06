import pygame
import Pieces
import random
import sys

pygame.init()

#Initialize
screenX = 700
screenY = 750
gameX = 450
gameY = 700
boxSide = 25
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Tetris")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
playerState = "PLACED"
gameover = False
run = True
score = 0        
playerX = gameX/2
playerY = 0
piecesArray = ["T", "L", "J", "Step", "StepR", "I", "Box"]

#Load Images
boximg = pygame.image.load("box.png")
placedimg = pygame.image.load('placed.png')
placedred = pygame.image.load("placedred.png")
placedorange = pygame.image.load("placedorange.png")
placedyellow = pygame.image.load("placedyellow.png")
placedgreen = pygame.image.load("placedgreen.png")
placedblue = pygame.image.load("placedblue.png")
gamebgimg = pygame.image.load('game.png')

colorArray = [placedred, placedorange, placedyellow, placedgreen, placedblue]

#Array to Remember Placed Objects
mainArray = [[False for x in range(int(gameX/boxSide))] for y in range(int(gameY/boxSide))]


#Draw Game Box
def gamebg():
    screen.blit(gamebgimg, (0,boxSide))


#Game Over Screen
def gameOver():
    global score
    screen.fill((0,0,0))
    font = pygame.font.Font("GOTHIC.TTF", 40)
    overText = font.render("GAME OVER", True, (255,255,255))
    screen.blit(overText, (200,270))
    finalScore = font.render("Score : "+str(score), True, (255,255,255))
    screen.blit(finalScore, (250, 400))
    pygame.display.update()


#Score Display
def scoreKeep():
    global score
    font = pygame.font.Font("GOTHIC.TTF", 24)
    scoreText = font.render("Score : "+str(score), True, (255,255,255))
    screen.blit(scoreText, (gameX+75, gameY/2))
    
def pauseMenu() :
    overlayimg = gamebgimg.convert_alpha()
    #alpha = 128
    #overlayimg.fill((255,255,255, alpha), None, pygame.BLEND_RGBA_MULT)
    overlayimg.set_alpha(128)
    screen.blit(overlayimg, (0, boxSide))
    pygame.display.update()
    pauseSwitch = True
    while pauseSwitch :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE : 
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RETURN : pauseSwitch = False
    return

#Get next piece for the start only
nextPiece = Pieces.pieceClass(piecesArray[random.randint(0, len(piecesArray)-1)])


#Print next piece
def whatsNext() :
    font = pygame.font.Font("GOTHIC.TTF", 24)
    nextText = font.render("Next Piece", True, (255,255,255))
    screen.blit(nextText, (gameX+50, gameY/2 + 150))
    for y in range(len(nextPiece.pieceArray)):
        for x in range(len(nextPiece.pieceArray[0])) :
            if nextPiece.pieceArray[y][x] :
                screen.blit(boximg, (gameX + 100 + (x-len(nextPiece.pieceArray[0])//2)*boxSide,  gameY/2 + 200 + y*boxSide))
                
                
#Game Loop
while run:

    #DEFAULTS
    tickdelay = 200
    playerXchange = 0
    playerYchange = boxSide
    screen.fill((0,0,0))
    if playerState == "PLACED" :
        piece = nextPiece
        nextPiece = Pieces.pieceClass(piecesArray[random.randint(0, len(piecesArray)-1)])
        playerX = gameX/2
        playerY = 0
        playerState = "FALLING"
    gamebg()
    pauseSwitch = False




    #INPUTS
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False
            pygame.display.quit()
            pygame.quit()
            sys.exit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT : playerXchange = 0-boxSide
            if event.key == pygame.K_RIGHT : playerXchange = boxSide
            if event.key == pygame.K_DOWN : tickedelay = 100
            if event.key == pygame.K_SPACE : piece.rotate()
            if event.key == pygame.K_RSHIFT : piece, nextPiece = nextPiece, piece
            if event.key == pygame.K_ESCAPE : pauseSwitch = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: playerXchange = 0-boxSide
    if keys[pygame.K_RIGHT]: playerXchange = boxSide
    if keys[pygame.K_DOWN] : tickdelay = 100




    #Check if colliding with walls of game or horizontal collision with other blocks
    piece.collisionCheck()



    #Set New Coords
    playerX += playerXchange
    playerY += playerYchange




    #Gameover
    for x in range(len(mainArray[0])):
        if mainArray[0][x] : 
            gameover = True
            run = False
            break
    if run == False : break





    #Draw all placed blocks and check for filled row
    for arrY in range(len(mainArray)) :
        for arrX in range(len(mainArray[arrY])) :
            if mainArray[arrY][arrX] : screen.blit(random.choice(colorArray),(arrX*boxSide, (arrY+1)*boxSide))
        if mainArray[arrY] == [True for x in range(int(gameX/boxSide))] : 
            mainArray.insert(0, [False for x in range(int(gameX/boxSide))])
            mainArray.pop(arrY+1)
            score += 1



    #Draw piece and check vertical collisions to solidify
    piece.drawer()
    piece.checker()



    #UPDATE
    whatsNext()
    scoreKeep()
    
    if pauseSwitch : pauseMenu()
    pygame.display.update()
    pygame.time.wait(int(tickdelay))


while gameover : 
    gameOver()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
           gameover = False
           pygame.display.quit()
           pygame.quit()
           sys.exit()