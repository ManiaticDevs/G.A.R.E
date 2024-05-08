import pygame
from pygame import mixer

pygame.init()
X = 700
Y = 700

scrn = pygame.display.set_mode((X, Y), pygame.RESIZABLE) ## window size and calling it resizable

pygame.display.set_caption("GARE") ## window name

mainMenuTest = pygame.image.load("assets\\main menu template.png").convert() ## making the GUI surface
mainMenuTest = pygame.transform.scale(mainMenuTest, (X, Y)) ## scaling the gui surface to the beginning window size
icon = pygame.image.load("assets\\icon.png").convert() ## making the icon surface

pygame.display.set_icon(icon) ## setting the icon in the top left
scrn.blit(mainMenuTest, (0, 0))

mixer.init()
pygame.mixer.set_num_channels(8)
voice = pygame.mixer.Channel(1)
mainMenuTestMusic = pygame.mixer.Sound("assets\\fallout 4 menu.mp3")    ## music biz, all you need to know is that the music for the main menu lies in channel 1, in a surface (for audio?) called voice
voice.set_volume(1)
voice.play(mainMenuTestMusic)

status = True
while (status):
    
                                                    ## RUNTIME
    
    w, h = pygame.display.get_surface().get_size() ## making variables for the current window size
    mainMenuTest = pygame.transform.scale(mainMenuTest, (w,h))
    scrn.blit(mainMenuTest, (0, 0))
    pygame.display.flip()
    if w != h: ## if the x and y window size are different
        pygame.display.set_mode((h, h), pygame.RESIZABLE) ## keeping a constant 1:1 ratio
    if voice.get_busy() == False:
        mixer.init()
        pygame.mixer.set_num_channels(8)
        voice = pygame.mixer.Channel(1)
        mainMenuTestMusic = pygame.mixer.Sound("assets\\fallout 4 menu.mp3")    ## makes music repeat if the audo surface isn't playing anything
        voice.set_volume(1)
        voice.play(mainMenuTestMusic)
        
                                                    ## RUNTIME
        
    for i in pygame.event.get():

        if i.type == pygame.QUIT: ## if X button is pressed
            status = False

pygame.quit()
