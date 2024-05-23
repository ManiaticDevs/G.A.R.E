import pygame
from pygame import mixer

pygame.init()
X = 900
Y = 900

scrn = pygame.display.set_mode((X, Y), pygame.RESIZABLE) ## window size and calling it resizable

pygame.display.set_caption("GARE") ## window name

mainMenuTest = pygame.image.load("assets\\main menu template.png").convert() ## making the GUI surface
mainMenuTest = pygame.transform.scale(mainMenuTest, (X, Y)) ## scaling the gui surface to the beginning window size
buttonTest = pygame.image.load("assets\\button.png").convert()

icon = pygame.image.load("assets\\icon.png").convert() ## making the icon surface

pygame.display.set_icon(icon) ## setting the icon in the top left
scrn.blit(mainMenuTest, (0, 0))

mixer.init()
pygame.mixer.set_num_channels(8)
music = pygame.mixer.Channel(1)
mainMenuTestMusic = pygame.mixer.Sound("assets\\ApocalypticEchoes.mp3")    ## music biz, all you need to know is that the music for the main menu lies in channel 1, in a surface (for audio?) called music
music.set_volume(0.1)
music.play(mainMenuTestMusic)

status = True
while (status):
    
                                                    ## RUNTIME
    
    screen_w, screen_h = pygame.display.get_surface().get_size() ## making variables for the current window size
    button_w, button_h = buttonTest.get_size()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    buttonTest_min_x, buttonTest_min_y, button_w, button_h = buttonTest.get_rect()
    buttonTest_max_x, buttonTest_max_y = buttonTest_min_x + button_w, buttonTest_min_y + button_h
    print(buttonTest_min_x, buttonTest_min_y, buttonTest_max_x, buttonTest_max_y)
    mainMenuTest = pygame.transform.scale(mainMenuTest, (screen_w, screen_h))
    scrn.blit(mainMenuTest, (0, 0))
    buttonTest = pygame.transform.scale(buttonTest, (screen_w/3, screen_h/3))
    scrn.blit(buttonTest, ((screen_w/2) - (button_w/2), (screen_h/2) - (button_h/2)))
    pygame.display.flip()
    if screen_w != screen_h: ## if the x and y window size are different
        pygame.display.set_mode((screen_h, screen_h), pygame.RESIZABLE) ## keeping a constant 1:1 ratio
        mainMenuTest = pygame.image.load("assets\\main menu template.png").convert()
        buttonTest = pygame.image.load("assets\\button.png").convert()
    if music.get_busy() == False:
        mixer.init()
        pygame.mixer.set_num_channels(8)
        music = pygame.mixer.Channel(1)
        mainMenuTestMusic = pygame.mixer.Sound("assets\\ApocalypticEchoes.mp3")    ## makes music repeat if the audo surface isn't playing anything
        music.set_volume(0.1)
        music.play(mainMenuTestMusic)
    if (buttonTest_min_x<=mouse_x and mouse_x<=buttonTest_max_x) and (buttonTest_min_y<=mouse_y and mouse_y<=buttonTest_max_y):
        print("high")
    
                                                    ## RUNTIME
        
    for i in pygame.event.get():

        if i.type == pygame.QUIT: ## if X button is pressed
            status = False

pygame.quit()
