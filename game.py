import pygame
import sys

from scripts.entity import PhysicsEntity
from scripts.utils import loadImage,  loadImages
from scripts.tilemap import Tilemap
from scripts.clouds import clouds

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320,240))
        self.clock = pygame.time.Clock()
        self.assets = {
            'decor' : loadImages('tiles/decor'),
            'grass' : loadImages('tiles/grass'),
            'stone' : loadImages('tiles/stone'),
            'large_decor' : loadImages('tiles/large_decor'),
            'player': loadImage('entities/player.png'),
            'background' : loadImage('background.png'),
            'clouds' : loadImages('clouds')
        }

        self.clouds  = clouds(self.assets['clouds'], count=16)
        self.movement = [False, False]
        self.player = PhysicsEntity(self,'player',(50,50),(8,15))
        self.tilemap = Tilemap(self,tile_size=16)
        self.scroll = [0,0]
    def run(self):
        while True:
            self.display.blit(self.assets['background'],(0,0))
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width()/2 - self.scroll[0]) /30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height()/2 - self.scroll[1]) /30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            self.clouds.update()
            self.clouds.render(self.display,render_scroll)
            self.tilemap.render(self.display, offset = render_scroll)
            self.player.update(self.tilemap,(self.movement[1] - self.movement[0],0))
            self.player.render(self.display, offset = render_scroll)           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT: 
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT: 
                        self.movement[1] = False
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()),(0,0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()