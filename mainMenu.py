#main menu file
import pygame, time
from main import Game as game
pygame.init()

fps = 120
clock = pygame.time.Clock()
obamaFix = 1

pygame.mixer.music.load("menumusic.mp3")

bg = pygame.image.load('bg2.jpg')
bg_rect = bg.get_rect()
keys = {'right':False, 'up':False, 'left':False, 'down':False}

screen = pygame.display.set_mode((1280, 720))
screen_rect = screen.get_rect()

controlScreen = pygame.display.set_mode((1280, 720))
controlScreen_rect = controlScreen.get_rect()

creditsScreen = pygame.display.set_mode((1280, 720))
creditsScreen_rect = controlScreen.get_rect()

logo = pygame.image.load('ohiologo.png')
logo_rect = logo.get_rect()
logo_rect.x = (screen.get_rect().centerx - (logo_rect.width / 2))
logo_rect.y = (screen.get_rect().centery - (logo_rect.height/2) - 150) / 2

controlsTab_rect = pygame.Rect((screen.get_rect().centerx - (logo_rect.width / 2)), (screen.get_rect().centery - (logo_rect.height/2) + 50), 275, 100)
creditsTab_rect = pygame.Rect((screen.get_rect().centerx - (logo_rect.width / 2) + 325), (screen.get_rect().centery - (logo_rect.height/2) + 50), 275, 100)
startTab_rect = pygame.Rect((screen.get_rect().centerx - (logo_rect.width / 2)), (screen.get_rect().centery - (logo_rect.height/2) + 175), 600, 100)
exitTab_rect = pygame.Rect((screen.get_rect().centerx - (logo_rect.width / 2)), (screen.get_rect().centery - (logo_rect.height/2) + 300), 600, 100)

menuFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 48)
controlsText = pygame.font.Font.render(menuFont, "Controls", True, (255, 255, 255))
controlsText_rect = controlsText.get_rect()

creditsText = pygame.font.Font.render(menuFont, "Credits", True, (255, 255, 255))
creditsText_rect = controlsText.get_rect()

startText = pygame.font.Font.render(menuFont, "Start", True, (255, 255, 255))
startText_rect = controlsText.get_rect()
print(startText_rect.width)

exitText = pygame.font.Font.render(menuFont, "Exit", True, (255, 255, 255))
exitText_rect = controlsText.get_rect()

backText = pygame.font.Font.render(menuFont, "Back", True, (255, 255, 255))

def loadingScreen():
    screen.fill((0,0,0))
    loadingText = pygame.font.Font.render(menuFont, "Loading...", True, (255, 255, 255))
    loadingText_rect = loadingText.get_rect()
    loadingText_rect.x = screen_rect.centerx
    loadingText_rect.y = screen_rect.centery
    screen.blit(loadingText, loadingText_rect)
    pygame.display.update()
    time.sleep(1)

level = 0

pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
running = True
controlsMenuActive = False
creditsActive = False
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            if (x >= startTab_rect.x and x <= (startTab_rect.x + startTab_rect.width) and y >= startTab_rect.y and y <= (startTab_rect.y + startTab_rect.height) and controlsMenuActive == False):
                loadingScreen()
                newGame = game()
                newGame.run()
                pygame.display.update()
            elif (x >= exitTab_rect.x and x <= (exitTab_rect.x + exitTab_rect.width) and y >= exitTab_rect.y and y <= (exitTab_rect.y + exitTab_rect.height) and controlsMenuActive == False):
                running = False
            # elif (x >= exitTab_rect.x and x <= (exitTab_rect.x + exitTab_rect.width) and y >= exitTab_rect.y and y <= (exitTab_rect.y + exitTab_rect.height) and controlsMenuActive == True):
            #     controlsMenuActive = False
            elif (x >= controlsTab_rect.x and x <= (controlsTab_rect.x + controlsTab_rect.width) and y >= controlsTab_rect.y and y <= (controlsTab_rect.y + controlsTab_rect.height) and controlsMenuActive == False):
                controlsMenuActive = True
            # elif (x >= exitTab_rect.x and x <= (exitTab_rect.x + exitTab_rect.width) and y >= exitTab_rect.y and y <= (exitTab_rect.y + exitTab_rect.height) and creditsActive == True):
            #     creditsActive = False
            elif (x >= creditsTab_rect.x and x <= (creditsTab_rect.x + creditsTab_rect.width) and y >= creditsTab_rect.y and y <= (creditsTab_rect.y + creditsTab_rect.height) and creditsActive == False):
                creditsActive = True


    while controlsMenuActive:
            controlScreen.blit(bg, (0,0))
            controlsMenuText = pygame.font.Font.render(menuFont, "arrow keys to move", True, (255, 255, 255))
            controlScreen.blit(controlsMenuText, ((controlsTab_rect.centerx - 90), (controlsTab_rect.centery - 50)))
            pygame.draw.rect(controlScreen, (0, 0, 255), exitTab_rect)
            controlScreen.blit(backText, ((exitTab_rect.centerx), (exitTab_rect.centery - 50)))
            pygame.display.update()
            clock.tick(fps)

            while (controlsMenuActive == True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        controlsMenuActive = False
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (x, y) = pygame.mouse.get_pos()
                        if (x >= exitTab_rect.x and x <= (exitTab_rect.x + exitTab_rect.width) and y >= exitTab_rect.y and y <= (exitTab_rect.y + exitTab_rect.height) and controlsMenuActive == True):
                            controlsMenuActive = False

    while creditsActive:
            creditsScreen.blit(bg, (0,0))
            creditsMenuText = pygame.font.Font.render(menuFont, "tiago made this", True, (255, 255, 255))
            creditsScreen.blit(creditsMenuText, ((creditsTab_rect.centerx - 90), (creditsTab_rect.centery - 50)))
            pygame.draw.rect(creditsScreen, (0, 0, 255), exitTab_rect)
            creditsScreen.blit(backText, ((exitTab_rect.centerx), (exitTab_rect.centery - 50)))
            pygame.display.update()
            clock.tick(fps)

            while (creditsActive == True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        creditsActive = False
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (x, y) = pygame.mouse.get_pos()
                        if (x >= exitTab_rect.x and x <= (exitTab_rect.x + exitTab_rect.width) and y >= exitTab_rect.y and y <= (exitTab_rect.y + exitTab_rect.height) and creditsActive == True):
                            creditsActive = False

    screen.blit(bg, (0,0))
    screen.blit(logo, logo_rect)
    pygame.draw.rect(screen, (255, 0, 0), controlsTab_rect)
    screen.blit(controlsText, ((controlsTab_rect.centerx - 90), (controlsTab_rect.centery - 50)))
    pygame.draw.rect(screen, (255, 0, 0), creditsTab_rect)
    screen.blit(creditsText, ((creditsTab_rect.centerx - 75), (creditsTab_rect.centery - 50)))
    pygame.draw.rect(screen, (0, 255, 0), startTab_rect)
    screen.blit(startText, ((startTab_rect.centerx - (startText_rect.width/2)), (startTab_rect.centery - 50)))
    pygame.draw.rect(screen, (0, 0, 255), exitTab_rect)
    screen.blit(exitText, ((exitTab_rect.centerx), (exitTab_rect.centery - 50)))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()