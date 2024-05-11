import pygame
from pygame import mixer
from scripts.ui.button import Button
from scripts.loader import ResourceLoader

pygame.init()
pygame.font.init()
w = 700 
h = 700

window = pygame.display

scrn = window.set_mode((w, h), pygame.RESIZABLE) ## window size and calling it resizable
window.set_caption("GARE") ## window name

mm = ResourceLoader.loadImage("main menu template") ## making the GUI surface
icon = ResourceLoader.loadImage("icon").convert() ## making the icon surface
window.set_icon(icon) ## setting the icon in the top left

font_size = 20
font = pygame.font.SysFont("Comic Sans MS", font_size)

button = Button("button", w/2,h/2,50,50)

status = True # runtime variable
cx=0 # canvas x
cy=0 # canvas y

def drawString(text, x, y): # draws string duh
    tw, th = font.size(text) # we just want to get width of text :/
    tx = cx+x-tw/2 # gets the position by offseting it by the canvas position, remove cx/cy and it would just be at actual coords (top left of screen)
    ty = cy+y-font_size/2 # we don't want it to change if j or g is introduced so we use the given font size
    # we dont want the text to go off screen halfway so we just calculate if the position will go off screen
    if x - tw/2 <= 0:
        tx = cx
    if y - font_size/2 <= 0:
        ty = cy

    scrn.blit(font.render(text, False, (255,255,255)), (tx,ty)) # renders at position

def handle_input(): # handles input..
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            return False
    
    return True

#TODO
def draw(mx, my):
    pass

mouse = pygame.mouse

while (status):
    w, h = window.get_surface().get_size() # get window size
    canvas_size = h # set canvas size to height
    
    mainMenuTest = mm.convert() # make sure the image doesn't look funny
    mainMenuTest = pygame.transform.scale(mainMenuTest, (canvas_size, canvas_size))

    canvas = scrn.copy() # copies the window surface as to give it a place to render
    canvas = pygame.transform.scale(canvas, (canvas_size,canvas_size)) # scale canvas to correct size
    canvas.blit(mainMenuTest, (0, 0)) # render image to canvas
    cx = ((w/2)-canvas.get_width()/2) # getting the left of the canvas from window
    cy = ((h/2)-canvas.get_height()/2) # getting the top of the canvas from window
    scrn.blit(canvas, (cx, cy)) # render canvas to screen
    
    # ui stuff
    button.update_with_pos(cx+canvas_size/2, cy+canvas_size/2, scrn,mouse, font) # logic handling
    if button.been_clicked():
        print("clicked!")
    
    drawString("gaming", 0,0) # string

    window.flip() # flip
    
    status = handle_input()

pygame.quit()
