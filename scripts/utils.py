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


class Animation:
    def __init__(self,images,img_dur=5,loop=True):
        self.images = images
        self.img_duration = img_dur
        self.loop = loop
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images,self.img_duration,self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True
                 
    def img(self):
        return self.images[int(self.frame / self.img_duration)]