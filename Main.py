import pygame

pygame.init()
X = 900
Y = 900

scrn = pygame.display.set_mode((X, Y), pygame.RESIZABLE) ## window size and calling it resizable

pygame.display.set_caption("GARE") ## window name

gui = pygame.image.load("assets\\GUI-main.png").convert() ## making the GUI surface
gui = pygame.transform.scale(gui, (900,900)) ## scaling the gui surface to the beginning window size (hardcoded)
icon = pygame.image.load("assets\\icon.png").convert() ## making the icon surface

pygame.display.set_icon(icon) ## setting the icon in the top left
scrn.blit(gui, (0, 0))

status = True
while (status):
                                                    ## RUNTIME
    w, h = pygame.display.get_surface().get_size() ## making variables for the current window size
    gui = pygame.transform.scale(gui, (w,h))
    scrn.blit(gui, (0, 0))
    pygame.display.flip()
    if w != h: ## if the x and y window size are different
        pygame.display.set_mode((h, h), pygame.RESIZABLE) ## keeping a constant 1:1 ratio
                                                    ## RUNTIME
    for i in pygame.event.get():

        if i.type == pygame.QUIT: ## if X button is pressed
            status = False

pygame.quit()
