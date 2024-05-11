import pygame

class ResourceLoader:
    @staticmethod
    def loadImage(image):
        return pygame.image.load("assets/images/"+image+".png")
    
    @staticmethod
    def loadAudio():
        pass
