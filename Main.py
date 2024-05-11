import pygame
from pygame import mixer
from scripts.ui.button import Button
from scripts.loader import ResourceLoader

pygame.init()
w = 700 
h = 700

window = pygame.display

scrn = window.set_mode((w, h), pygame.RESIZABLE) ## window size and calling it resizable
window.set_caption("GARE") ## window name

mm = ResourceLoader.loadImage("main menu template") ## making the GUI surface
icon = ResourceLoader.loadImage("icon").convert() ## making the icon surface

window.set_icon(icon) ## setting the icon in the top left
button = Button("button", w/2,h/2,50,50)

status = True

def handle_input():
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            return False
    
    return True

def draw(mx, my):
    pass

mouse = pygame.mouse

while (status):
    mx, my = mouse.get_pos()
    ## RUNTIME
    w, h = window.get_surface().get_size() ## making variables for the current window size
    mainMenuTest = mm.convert()
    mainMenuTest = pygame.transform.scale(mainMenuTest, (w,h))
    scrn.blit(mainMenuTest, (0, 0))
    button.update_with_pos(w/2, h/2, scrn,mouse)
    if button.been_clicked():
        print("clicked!")
    window.flip()
    if w != h: ## if the x and y window size are different
        window.set_mode((w, w), pygame.RESIZABLE) ## keeping a constant 1:1 ratio           

    status = handle_input()

pygame.quit()
