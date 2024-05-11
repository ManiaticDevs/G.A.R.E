import pygame
from scripts.loader import ResourceLoader

class Button:
    def __init__(self, image, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(ResourceLoader.loadImage(image).convert(), (width,height))
        self.clickLock = False
        self.clicked = False
        self.hovering = False
    
    def update(self, screen, mouse):
        self.update_with_pos(self.x,self.y, screen, mouse)
    
    def update_with_pos(self, x, y, screen, mouse, font): # handles drawing and logic
        self.x = x
        self.y = y
        self.clicked = False
        mx, my = mouse.get_pos() # gets position
        if(self.y + self.height/2 > my and self.y-self.height/2 < my and self.x+self.width/2 > mx and self.x-self.width/2 < mx): # checks the bounds from x, y using width and height
            self.hovering = True
            if mouse.get_pressed()[0]: # checks if left click has been pressed
                if not self.clickLock: # prevent holding
                    self.clicked = True
                    self.clickLock = True
            else:
                self.clickLock = False
        else:
            self.hovering = False
        screen.blit(self.image, (self.x-self.width/2,self.y-self.height/2))
        self.drawString(font)

    def update_position(self, x, y): # guess.
        self.x = x
        self.y = y
    
    def drawString(self, font):
        pass 

    def is_hovering(self): # returns true the mouse is hovering over it
        return self.hovering

    def been_clicked(self): # returns true (for a milisec) if mouse clicked on it
        return self.clicked
