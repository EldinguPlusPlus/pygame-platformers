import pygame
import random
import os
import time
#initialize
pygame.init()
# create screen
screen = pygame.display.set_mode((1920,1080))

#title & icon
truegame = False
intro = True
pygame.display.set_caption("Quest")
icon = pygame.image.load('Sprite images/brain.png')
hill = pygame.image.load('Sprite images/hill.png')
dragon = pygame.image.load('Sprite images/dragon.png')
dragonX = 925
groundY = 750
dragonY = groundY-600
dragonlife = 75
pygame.display.set_icon(icon)
textbackgroundblack = (0,0,0)
textfontcolorwhite = (255,255,255)
level1text = True
level1sheildtutorial = False
level2text = False
level3text = False
font = pygame.font.Font('Fonts/Montserrat-Light.ttf',18)
fontbrain = pygame.font.Font('Fonts/Montserrat-Light.ttf',30)
textgreet = font.render('Welcome to Quest.', True, textfontcolorwhite, textbackgroundblack)
moveattacktext = font.render('Use A & D to move. Click to attack.', True, textfontcolorwhite, textbackgroundblack)
goforthmyson = font.render('Now go forth, my son. Try.', True, textfontcolorwhite, textbackgroundblack)
moveattacktextRect = moveattacktext.get_rect()
moveattacktextRect.center = (1700,50)
goforthmysonRect = goforthmyson.get_rect()
goforthmysonRect.center = (1700,71)
textgreetRect = textgreet.get_rect()
textgreetRect.center = (1700,30)
sheildingup = font.render('Hold up your sheild, or you will burn.', True, textfontcolorwhite, textbackgroundblack)
sheildingupRect = sheildingup.get_rect()
sheildingupRect.center = (1700,50)
sheildkeytut = font.render('Hold S to hold up your sheild.', True, textfontcolorwhite, textbackgroundblack)
sheildkeytutRect = sheildkeytut.get_rect()
sheildkeytutRect.center = (1700,30)
bigbraingames = fontbrain.render('A Big Brain Games Production', True, textbackgroundblack, textfontcolorwhite)
bigbraingamesRect = bigbraingames.get_rect()
bigbraingamesRect.center = (960,540)
pythoncred = fontbrain.render('    Programmed Using Python   ', True, textbackgroundblack, textfontcolorwhite)
pythoncredRect = pythoncred.get_rect()
pythoncredRect.center = (960,540)
pygamecred = fontbrain.render('GUI Created Using the Pygame Module', True, textbackgroundblack, textfontcolorwhite)
pygamecredRect = pygamecred.get_rect()
pygamecredRect.center = (960,540)
tsa = fontbrain.render('Motivated By Technology Student Association(TSA)', True, textbackgroundblack, textfontcolorwhite)
tsaRect = tsa.get_rect()
tsaRect.center = (960,540)
linux = fontbrain.render('                       Created On a Linux System                       ', True, textbackgroundblack, textfontcolorwhite)
linuxRect = linux.get_rect()
linuxRect.center = (960,540)
questi = fontbrain.render('                       Quest                       ', True, textbackgroundblack, textfontcolorwhite)
questiRect = questi.get_rect()
questiRect.center = (960,540)
youcanskip = font.render("You cannot skip due to lack of knowledge.", True, textbackgroundblack, textfontcolorwhite)
youcanskipRect = youcanskip.get_rect()
youcanskipRect.center = (960,700)
neverbeen = font.render('Peace and quiet. You can use space to jump.', True, textfontcolorwhite, textbackgroundblack)
neverbeenRect = neverbeen.get_rect()
neverbeenRect.center = (1700,30)
dragoni = font.render(''' Giant red chicken!! Whoops, it's a dragon.''', True, textfontcolorwhite, textbackgroundblack)
dragoniRect = dragoni.get_rect()
dragoniRect.center = (1700,30)
dragonin = font.render(''' Use all I taught you - it's all you can do! Hint: J & S''', True, textfontcolorwhite, textbackgroundblack)
dragoninRect = dragoni.get_rect()
dragoninRect.center = (1650,50)
congrats = fontbrain.render('Congratulations! You beat the dragon!', True, textbackgroundblack, textfontcolorwhite)
congratsRect = congrats.get_rect()
congratsRect.center = (960,540)
toobad = fontbrain.render('''Too bad they don't exist, though. You would feel a better sense of accomplishment.''', True, textbackgroundblack, textfontcolorwhite)
toobadRect = toobad.get_rect()
toobadRect.center = (960,540)
goodbyenow = fontbrain.render('''          Now, goodbye. I've got a declaration of independence to sign. ~ Benjamin          ''', True, textbackgroundblack, textfontcolorwhite)
goodbyenowRect = goodbyenow.get_rect()
goodbyenowRect.center = (960,540)
playerImg = pygame.image.load('Sprite images/knight.png')
playerX = 25
playerY = 536
playerW = 143
playerH = 214
playerJumping = False
PV = 13
PM = 1
playerX_change = 0
playerY_change = 0
groundImg = pygame.image.load('Sprite images/art (9).png')
groundX = 0
groundY = 750
benImg = pygame.image.load('Sprite images/ben1.png')
benX = 1700
benY = 0
lifeImg = pygame.image.load('Sprite images/life.png')
life1X = 0
life2X = 105
life3X = 210
life4X = 315
life5X = 420
lifeY = 0
enemyX = 500
enemyY = 540
enemyW = 150
enemyH = 210
player_rect = pygame.Rect(playerX, playerY, playerW, playerH)
enemy_rect = pygame.Rect(enemyX, enemyY, enemyW, enemyH)
onelifeleft = True
twolivesleft = True
threelivesleft = True
fourlivesleft = True
fivelivesleft = True
lifenum = 5
benUD = True
sheildup = False
enemyImg = pygame.image.load('Sprite images/art (8).png')
enemylife = 2
enemyX_change = 0
enemyY_change = 0
ray = pygame.image.load('Sprite images/sunray.png')
sunImg = pygame.image.load('Sprite images/sunny.png')
sunlife = 3
sunX = benX - 150
sunY = benY + 150
level2enemyY = 525-210
level2enemyX = 700
enemyXspeed = -10
fireX = 925
def player(x,y):
    screen.blit(playerImg, (x, y))
def ground(x,y):
    screen.blit(groundImg, (x, y))
def benjamin(x,y):
    screen.blit(benImg, (x,y))
#game loop
def enemy(x,y):
    screen.blit(enemyImg, (x,y))
running = True
firemove = 7
reflectors = False
bigbrain = True
pythonc = False
ending = False
pygamec = False
tsac = False
notoverhight = True
level1prev = True
justthrown = True
enemy2life = 8
while running:
    if intro:
        
        screen.fill((255,255,255))
        pygame.display.update()
        screen.blit(benImg, (1888, 982))
        screen.blit(youcanskip, youcanskipRect)
        time.sleep(1.5)
        pythonlogo = pygame.image.load('Sprite images/Python.jpeg')
        if bigbrain:
            screen.blit(bigbraingames, bigbraingamesRect)
            pygame.display.update()
        
            time.sleep(2)
            bigbrain = False
            pythonc = True
        if pythonc:
            
            screen.blit(pythoncred, pythoncredRect)
            pygame.display.update()
        
            time.sleep(2)
            pythonc = False
            pygamec = True
        if pygamec:
            screen.blit(pygamecred, pygamecredRect)
            pygame.display.update()
        
            time.sleep(2)
            pygamec = False
            tsac = True
        if tsac:
            screen.blit(tsa, tsaRect)
            pygame.display.update()
        
            time.sleep(2)
            tsac = False
            linuxc = True
        if linuxc:
            screen.blit(linux, linuxRect)
            pygame.display.update()
            time.sleep(2)
            linuxc = False
            questic = True
        if questic:
            screen.blit(questi, questiRect)
            pygame.display.update()
            time.sleep(3.5)
            questic = False
        intro = False
        truegame = True
    if ending:
        screen.fill((255,255,255))
        pygame.display.update()
        screen.blit(congrats, congratsRect)
        pygame.display.update()
        time.sleep(5)
        screen.blit(toobad, toobadRect)
        pygame.display.update()
        time.sleep(5)
        screen.blit(goodbyenow, goodbyenowRect)
        pygame.display.update()
        time.sleep(5)
        ending = False
        pygame.quit()
        quit()
        
    if truegame:
        keys = pygame.key.get_pressed()
        
        if playerX >= 400 - playerW and playerY >= 525-playerH and level2text and playerX <= 500 and keys[pygame.K_d]:
            playerY_change = -7
        elif playerX >= 400 - playerW and playerY >= 525-playerH and level2text and playerX <= 500 and keys[pygame.K_a]:
            playerY_change = 7
        elif playerX >= 925 and playerY >= 525-playerH and level2text and keys[pygame.K_d]:
            playerY_change = 7
        elif playerX >= 925 and playerY >= 525-playerH and playerX <= 1225 and level2text and keys[pygame.K_a]:
            playerY_change = -7
        elif playerY < 525-playerH and level2text:
            playerY = 525-playerH
        else:
            playerY_change = 0
        if playerY >= groundY - playerH:
            playerY = groundY - playerH
    
        if playerJumping == False:
            if keys[pygame.K_SPACE]:
                playerJumping = True
        if playerX > enemyX-playerW and playerX < enemyX+enemyW and playerY > enemyY-playerH and enemylife > 0 and level1text:
            lifenum -= 1
        if pygame.mouse.get_pressed()[0]:
            if playerX > enemyX-(playerW+50) and playerX < enemyX-playerW and playerY == 536 or playerX < enemyX+enemyW+50 and playerX > enemyX+enemyW and playerY == 536 and enemylife > 0:
                enemylife -= 1
        if lifenum == 4:
            fivelivesleft = False
        if lifenum == 3:
            fourlivesleft = False
        if lifenum == 2:
            threelivesleft = False
        if lifenum == 1:
            twolivesleft = False
        if lifenum == 0:
            onelifeleft = False
        if playerX > 1300 and level1prev:
            level1text = False
            level1sheildtutorial = True
        if playerJumping:
            F =(1/2)*PM*(PV**2)
            playerY -= F
            PV = PV-1
            if PV<0:
                PM =-1
            if PV ==-14:
                playerJumping = False
                PV = 13
                PM = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    playerX_change = -15
                    playerImg = pygame.image.load('Sprite images/knight2.png')
                if event.key == pygame.K_d:
                    playerX_change = 15
                    playerImg = pygame.image.load('Sprite images/knight.png')
                    
                if event.key != pygame.K_s and event.key != pygame.K_a:
                    playerImg = pygame.image.load('Sprite images/knight.png')
                if event.key == pygame.K_s:
                    sheildup = True
                    playerImg = pygame.image.load('Sprite images/art.png')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_UP:
                    playerX_change = 0
                    sheildup = False
                    playerY_change = 0

        
        playerX += playerX_change
        playerY += playerY_change
        if playerX <= 0:
            playerX = 0
        if playerX > 1777 and level1sheildtutorial:
            playerX = 25
            level1sheildtutorial = False
            level1prev = False
            level2text = True
        if playerX > 1777 and level2text:
            playerX = 25
            level2text = False
            level3text = True
        screen.fill((0, 175, 225))
        if level2text:
            screen.blit(hill, (200, groundY-225))
            screen.blit(neverbeen, neverbeenRect)
        player(playerX,playerY)
        if level3text:
            dragonlifetext = fontbrain.render(str(dragonlife)+" health", True, textfontcolorwhite, textbackgroundblack)
            dragonlifetextRect = dragonlifetext.get_rect()
            dragonlifetextRect.center = (1000, groundY-618)
            screen.blit(dragoni, dragoniRect)
            screen.blit(dragonin, dragoninRect)
            
            if dragonlife >= 1:
                screen.blit(pygame.image.load('Sprite images/fireball.png'), (fireX, dragonY + 200))
                screen.blit(dragon, (dragonX, dragonY))
                screen.blit(dragonlifetext, dragonlifetextRect)
            if dragonlife <= 0:
                time.sleep(3)
                truegame = False
                ending = True
        if playerX >= sunX+50 and playerX <= sunX+95 and sunlife > 0 and sheildup == False:
            lifenum -= 1
        if playerX >= sunX+50 and playerX <= sunX+95 and sunlife > 0 and sheildup:
            sunlife -= 1
        if playerY >= dragonY+200 and level3text and playerY <= dragonY+320 and playerX >= fireX and playerX <= fireX+285:
            justthrown = False
            if level3text and keys[pygame.K_s]:
                reflectors = True
            else:
                lifenum -= 1
        if reflectors:
            dragonlife -= 0.045
        if playerX >= dragonX-playerW and level3text and dragonlife >= 1:
            lifenum -= 1
        if fireX <= 0:
            fireX = 925
            reflectors = False
            justthrown = True
        if playerX >= sunX+50 and sunlife > 0 and sheildup:
            sunlife -= 1
        if onelifeleft:
            screen.blit(lifeImg, (life1X,lifeY))
            if twolivesleft:
                screen.blit(lifeImg, (life2X,lifeY))
                if threelivesleft:
                    screen.blit(lifeImg, (life3X,lifeY))
                    if fourlivesleft:
                        screen.blit(lifeImg, (life4X,lifeY))
                        if fivelivesleft:
                            screen.blit(lifeImg, (life5X,lifeY))
        if onelifeleft == False and twolivesleft == False and threelivesleft == False and fourlivesleft == False and fivelivesleft == False:
            running = False
            pygame.quit()
            quit()
        if level1text:
            screen.blit(textgreet, textgreetRect)
            screen.blit(moveattacktext, moveattacktextRect)
            screen.blit(goforthmyson, goforthmysonRect)
            if enemylife > 0:
                enemy(enemyX, enemyY)
            if enemylife >= 1:
                screen.blit(lifeImg, (enemyX, enemyY-100))
                if enemylife == 2:
                    screen.blit(lifeImg, (enemyX+105, enemyY-100))
        if level1sheildtutorial:
            screen.blit(sheildkeytut, sheildkeytutRect)
            screen.blit(sheildingup, sheildingupRect)
            if enemylife > 0:
                enemy(enemyX, enemyY)
            if enemylife >= 1:
                screen.blit(lifeImg, (enemyX, enemyY-100))
                if enemylife == 2:
                    screen.blit(lifeImg, (enemyX+105, enemyY-100))
            if sunlife > 0:
                screen.blit(sunImg, (sunX, sunY))
            if sunlife>=1:
                screen.blit(lifeImg, (sunX-50, sunY+210))
                screen.blit(ray, (sunX+50, sunY+80))
                if sunlife>=2:
                    screen.blit(lifeImg, (sunX+55, sunY+210))
                    if sunlife == 3:
                        screen.blit(lifeImg,(sunX+160, sunY+210))
        ground(groundX,groundY)
        benjamin(benX,benY)
        if level3text:
            fireX -= firemove
        playerY += playerY_change
        pygame.display.update()
