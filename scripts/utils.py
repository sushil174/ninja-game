import pygame
import os
BASE_PATH = 'data/images/'

def loadImage(path):
    img = pygame.image.load(BASE_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def loadImages(path):
    images = []
    for image in sorted(os.listdir(BASE_PATH + path)):
        images.append(loadImage(path + '/' + image))

    return images