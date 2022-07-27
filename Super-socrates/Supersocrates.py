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
pygame.display.set_caption("Some random greek game")
icon = pygame.image.load('Sprite images/brain.png')
dragon = pygame.image.load('Sprite images/unnamed1.png')
dragon = pygame.transform.scale(dragon, (256, 158))
dragonX = 925
groundY = 750
dragonY = groundY-158.5
dragonlife = 35
pygame.display.set_icon(icon)
textbackgroundblack = (0,0,0)
textfontcolorwhite = (255,255,255)
level1text = True
level1sheildtutorial = False
level2text = False
level3text = False
font = pygame.font.Font('Fonts/Montserrat-Light.ttf',11)
fontbrain = pygame.font.Font('Fonts/Montserrat-Light.ttf',30)
textgreet = font.render('''Hello players, I'm Socrates, your tour guide.''', True, textfontcolorwhite, textbackgroundblack)
moveattacktext = font.render('''I'll give you useful information about democracy.''', True, textfontcolorwhite, textbackgroundblack)
goforthmyson = font.render('''Sit back and relax as I tell you about it.''', True, textfontcolorwhite, textbackgroundblack)
moveattacktextRect = moveattacktext.get_rect()
moveattacktextRect.center = (1700,50)
goforthmysonRect = goforthmyson.get_rect()
goforthmysonRect.center = (1700,71)
textgreetRect = textgreet.get_rect()
textgreetRect.center = (1700,30)
sheildingup = font.render('Democracy is a form of government that allows its', True, textfontcolorwhite, textbackgroundblack)
sheildingupRect = sheildingup.get_rect()
sheildingupRect.center = (1700,50)
sheildingx = font.render('citizens to have a say in laws, policies, and leadership.', True, textfontcolorwhite, textbackgroundblack)
sheildingxRect = sheildingx.get_rect()
sheildingxRect.center = (1700,70)
sheildingdown = font.render('Democracy originated in athens in 508 B.C. It is', True, textfontcolorwhite, textbackgroundblack)
sheildingdownRect = sheildingdown.get_rect()
sheildingdownRect.center = (1700,90)
sheildingY = font.render('still being used today in countries such as the USA.', True, textfontcolorwhite, textbackgroundblack)
sheildingYRect = sheildingY.get_rect()
sheildingYRect.center = (1700,110)
sheildkeytut = font.render('To start this journey I will give you the basics.', True, textfontcolorwhite, textbackgroundblack)
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
tsa = fontbrain.render('   Created for a random school project   ', True, textbackgroundblack, textfontcolorwhite)
tsaRect = tsa.get_rect()
tsaRect.center = (960,540)
linux = fontbrain.render('                       Based on Quest                       ', True, textbackgroundblack, textfontcolorwhite)
linuxRect = linux.get_rect()
linuxRect.center = (960,540)
questi = fontbrain.render('                       Some random greek game                       ', True, textbackgroundblack, textfontcolorwhite)
questiRect = questi.get_rect()
questiRect.center = (960,540)
youcanskip = font.render("You cannot skip due to lack of knowledge.", True, textbackgroundblack, textfontcolorwhite)
youcanskipRect = youcanskip.get_rect()
youcanskipRect.center = (960,700)
neverbeen = font.render('Avoid the minotaur.', True, textfontcolorwhite, textbackgroundblack)
neverbeenRect = neverbeen.get_rect()
neverbeenRect.center = (1700,30)
word1 = font.render('In his time as ruler of Athens, Cleisthenes created the first known', True, textfontcolorwhite, textbackgroundblack)
word1Rect = word1.get_rect()
word1Rect.center = (1700,30)
word2 = font.render('democracy. Although this democracy would only last 2 centuries,', True, textfontcolorwhite, textbackgroundblack)
word2Rect = word2.get_rect()
word2Rect.center = (1700,50)
word3 = font.render('this democracy impacted the way we would run our current government.', True, textfontcolorwhite, textbackgroundblack)
word3Rect = word3.get_rect()
word3Rect.center = (1700,70)
word4 = font.render('Democracy is a benefitial way of running a government because it allows', True, textfontcolorwhite, textbackgroundblack)
word4Rect = word4.get_rect()
word4Rect.center = (1700, 90)
word5 = font.render('citizens to have a voice in government no matter their social class.', True, textfontcolorwhite, textbackgroundblack)
word5Rect = word5.get_rect()
word5Rect.center = (1700,110)
word6 = font.render('Democracy prevents people from being ruled without a say.', True, textfontcolorwhite, textbackgroundblack)
word6Rect = word6.get_rect()
word6Rect.center = (1700,130)
word7 = font.render('''There have been many differences between democracy now''', True, textfontcolorwhite, textbackgroundblack)
word7Rect = word7.get_rect()
word7Rect.center = (1700,30)
word8 = font.render('''and thousands of years ago. In today's government women''', True, textfontcolorwhite, textbackgroundblack)
word8Rect = word8.get_rect()
word8Rect.center = (1700,50)
word9 = font.render('''can vote, and we have a represenative democracy with an electoral''', True, textfontcolorwhite, textbackgroundblack)
word9Rect = word9.get_rect()
word9Rect.center = (1700,70)
word10 = font.render('''college. However, Athens did not do this. Ancient Greek''', True, textfontcolorwhite, textbackgroundblack)
word10Rect = word10.get_rect()
word10Rect.center = (1700,90)
word11 = font.render('''democracy IS similar to the one today, by a minimum voting age of 18,''', True, textfontcolorwhite, textbackgroundblack)
word11Rect = word11.get_rect()
word11Rect.center = (1700,110)
word12 = font.render('''and a trial by jury.''', True, textfontcolorwhite, textbackgroundblack)
word12Rect = word12.get_rect()
word12Rect.center = (1700,130)
ord1 = font.render('''Citizens typically participate in democracy by having a set of rights''', True, textfontcolorwhite, textbackgroundblack)
ord1Rect = ord1.get_rect()
ord1Rect.center = (1700,30)
ord2 = font.render('''and responsibilities. These rights include the ability to participate in decisions''', True, textfontcolorwhite, textbackgroundblack)
ord2Rect = ord2.get_rect()
ord2Rect.center = (1700,50)
ord3 = font.render('''that affect public welfare. This allows citizens to congregate to vote on laws and''', True, textfontcolorwhite, textbackgroundblack)
ord3Rect = ord3.get_rect()
ord3Rect.center = (1700,70)
ord4 = font.render('''policies. Democracy is demonstrated all of the time in the U.S. When someone''', True, textfontcolorwhite, textbackgroundblack)
ord4Rect = ord4.get_rect()
ord4Rect.center = (1700,90)
ord5 = font.render('''commits a crime, they are put on trial.(Trial by jury) More evidence of''', True, textfontcolorwhite, textbackgroundblack)
ord5Rect = ord5.get_rect()
ord5Rect.center = (1700,110)
ord6 = font.render('''democracy is voting. In the past few centuries, citizens cast votes to''', True, textfontcolorwhite, textbackgroundblack)
ord6Rect = ord6.get_rect()
ord6Rect.center = (1700,130)
ord7 = font.render('''decide who is going to lead their country, or represent them.''', True, textfontcolorwhite, textbackgroundblack)
ord7Rect = ord7.get_rect()
ord7Rect.center = (1700,150)
n1 = font.render('''To me, Socrates, democracy means having a government where citizens''', True, textfontcolorwhite, textbackgroundblack)
n1Rect = n1.get_rect()
n1Rect.center = (1700,30)
n2 = font.render('''have a say in laws, policies, and leadership. Democracy prevents''', True, textfontcolorwhite, textbackgroundblack)
n2Rect = n2.get_rect()
n2Rect.center = (1700,50)
n3 = font.render('''citizens from being ruled without a say. Democracy also means''', True, textfontcolorwhite, textbackgroundblack)
n3Rect = n3.get_rect()
n3Rect.center = (1700,70)
n4 = font.render('''the right to elect your own officials, and vote on policies and laws.''', True, textfontcolorwhite, textbackgroundblack)
n4Rect = n4.get_rect()
n4Rect.center = (1700,90)
dragoni = font.render(''' Now that you know about democracy, take down that baby and''', True, textfontcolorwhite, textbackgroundblack)
dragoniRect = dragoni.get_rect()
dragoniRect.center = (1700,30)
dragonin = font.render('''Caillou oligarchy and create the best government possible - DEMOCRACY!!!''', True, textfontcolorwhite, textbackgroundblack)
dragoninRect = dragoni.get_rect()
dragoninRect.center = (1650,50)
congrats = fontbrain.render('Congrats on beating Baby Polydectes...', True, textbackgroundblack, textfontcolorwhite)
congratsRect = congrats.get_rect()
congratsRect.center = (960,540)
toobad = fontbrain.render('''   ...And creating a democratic government!   ''', True, textbackgroundblack, textfontcolorwhite)
toobadRect = toobad.get_rect()
toobadRect.center = (960,540)
goodbyenow = fontbrain.render('''          And I wish you luck with your democracy!          ''', True, textbackgroundblack, textfontcolorwhite)
goodbyenowRect = goodbyenow.get_rect()
goodbyenowRect.center = (960,540)
goodbyenoww = fontbrain.render('''          Go to: bit.ly/3hWkppi for the sources and dialogue!         ''', True, textbackgroundblack, textfontcolorwhite)
goodbyenowwRect = goodbyenoww.get_rect()
goodbyenowwRect.center = (960,540)
playerImg = pygame.image.load('Sprite images/art (3).png')
playerX = 25
playerY = 543
playerW = 145
playerH = 207
mooseImg = pygame.image.load('Sprite images/arq.png')
mooseImg = pygame.transform.scale(mooseImg, (150,120))
playerJumping = False
PV = 13
PM = 1
playerX_change = 0
playerY_change = 0
groundImg = pygame.image.load('Sprite images/art (9).png')
groundX = 0
groundY = 750
benImg = pygame.image.load('Sprite images/Webp.net-resizeimage.png')
benX = 1353
benY = 100
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
enemylife = 0
enemyX_change = 0
enemyY_change = 0
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
level2inbe = False
level2sub = False
level2subb = False
level2subbb = False
mooseLife = 0
enemy2life = 8
jujubes = False
while running:
    if intro:
        
        screen.fill((255,255,255))
        pygame.display.update()
        screen.blit(benImg, (1888, 982))
        screen.blit(youcanskip, youcanskipRect)
        time.sleep(1.5)
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
        screen.blit(goodbyenoww, goodbyenowwRect)
        pygame.display.update()
        time.sleep(5)
        ending = False
        pygame.quit()
        quit()
        
    if truegame:
        keys = pygame.key.get_pressed()
        if playerJumping == False:
            if keys[pygame.K_SPACE]:
                playerJumping = True
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
        if playerX > 1000 and level1prev:
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
        if mooseLife > 0 and level2text:
            if playerX >= 200-playerW and playerX <= 350 and playerY >= 630-playerH:
                lifenum -= 1
        if playerX > 400 and level2text:
            level2text = False
            level2inbe = True
        if playerX > 700 and level2inbe:
            level2inbe = False
            level2sub = True
        if playerX > 900 and level2sub:
            level2sub = False
            level2subb = True
        if playerX > 1100 and level2subb:
            level2subb = False
            level2subbb = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    playerX_change = -15
                    playerImg = pygame.image.load('Sprite images/art (4).png')
                if event.key == pygame.K_d:
                    playerX_change = 15
                    playerImg = pygame.image.load('Sprite images/art (3).png')
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
        if playerX > 1777 and level2subbb:
            playerX = 200
            level2subbb = False
            level3text = True
        screen.fill((0, 175, 225))
        if level2text:
            mooseLife = 15
            screen.blit(neverbeen, neverbeenRect)
        screen.blit(pygame.image.load('Sprite images/pillar.png'), (-120, 315))
        screen.blit(pygame.image.load('Sprite images/art (2).png'), (1455,0))
        screen.blit(pygame.image.load('Sprite images/pillar.png'), (1820, 315))
        if level2inbe:
            screen.blit(word1, word1Rect)
            screen.blit(word2, word2Rect)
            screen.blit(word3, word3Rect)
            screen.blit(word4, word4Rect)
            screen.blit(word5, word5Rect)
            screen.blit(word6, word6Rect)
        if level2sub:
            screen.blit(word7, word7Rect)
            screen.blit(word8, word8Rect)
            screen.blit(word9, word9Rect)
            screen.blit(word10, word10Rect)
            screen.blit(word11, word11Rect)
            screen.blit(word12, word12Rect)
        if level2subb:
            screen.blit(ord1, ord1Rect)
            screen.blit(ord2, ord2Rect)
            screen.blit(ord3, ord3Rect)
            screen.blit(ord4, ord4Rect)
            screen.blit(ord5, ord5Rect)
            screen.blit(ord6, ord6Rect)
            screen.blit(ord7, ord7Rect)
        if level2subbb:
            screen.blit(n1, n1Rect)
            screen.blit(n2, n2Rect)
            screen.blit(n3, n3Rect)
            screen.blit(n4, n4Rect)
        player(playerX,playerY)
        if mooseLife > 0 and level2text:
            screen.blit(mooseImg, (200, groundY-120))
        if level3text:
            dragonlifetext = fontbrain.render("Just jump him. His weapon does nothing.", True, textfontcolorwhite, textbackgroundblack)
            dragonlifetextRect = dragonlifetext.get_rect()
            dragonlifetextRect.center = (1000, groundY-300)
            screen.blit(dragoni, dragoniRect)
            screen.blit(dragonin, dragoninRect)
            screen.blit(pygame.image.load("Sprite images/art (6).png"), (487.5,0))
            if playerX > 1181:
                dragonlife = 0
            if dragonlife >= 1:
                screen.blit(pygame.image.load('Sprite images/art (5).png'), (fireX, dragonY + 200))
                screen.blit(dragon, (dragonX, dragonY))
                screen.blit(dragonlifetext, dragonlifetextRect)
            if dragonlife <= 0:
                time.sleep(3)
                truegame = False
                ending = True
        if playerY >= dragonY+200 and level3text and playerY <= dragonY+320 and playerX >= fireX and playerX <= fireX+285:
            justthrown = False
            if level3text and keys[pygame.K_s]:
                reflectors = True
            else:
                lifenum -= 1
        if reflectors:
            dragonlife -= 0.045
        if playerX >= dragonX-playerW and level3text and dragonlife >= 1 and playerX <= dragonX-playerW+256 and playerY >= dragonY -playerH:
            lifenum -= 1
        if fireX <= 0:
            fireX = 925
            reflectors = False
            justthrown = True
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
            screen.blit(sheildingx, sheildingxRect)
            screen.blit(sheildingdown, sheildingdownRect)
            screen.blit(sheildingY, sheildingYRect)
            if enemylife > 0:
                enemy(enemyX, enemyY)
            if enemylife >= 1:
                screen.blit(lifeImg, (enemyX, enemyY-100))
                if enemylife == 2:
                    screen.blit(lifeImg, (enemyX+105, enemyY-100))
        ground(groundX,groundY)
        benjamin(benX,benY)
        if level3text:
            fireX -= firemove
        playerY += playerY_change
        pygame.display.update()
