import pytmx
import pygame
from pytmx.util_pygame import load_pygame
from settings import *

pygame.init()

SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Loading in objects")
clock = pygame.time.Clock()

coin = pygame.image.load('resources/coin.png').convert_alpha()
coin = pygame.transform.scale(coin, (48, 48))

currentLevel = 'resources/level6.tmx'


class LevelLoad():
    def __init__(self):
        self.tiled_map = pytmx.load_pygame(currentLevel)
        self.tilewidth = self.tiled_map.tilewidth
        self.tileheight = self.tiled_map.tileheight

    def load(self):
        for layer in self.tiled_map.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, tile in layer.tiles():
                    if tile:
                        SCREEN.blit(tile, [(x * self.tilewidth) - CAMERA.x + (SCREEN_WIDTH / 2),
                                           (y * self.tileheight) - CAMERA.y + (SCREEN_HEIGHT / 2)])

            elif isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == "coin":
                    for object in layer:
                        SCREEN.blit(coin, [object.x - CAMERA.x + (SCREEN_WIDTH / 2),
                                             object.y - CAMERA.y + (SCREEN_HEIGHT / 2)])


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        LevelLoad.load(self=)

        pygame.display.update()


    pos = [0, 0]
    for events in pygame.event.get():  # get all pygame events
        if events.type == pygame.KEYDOWN:
            temp = b.rect.topleft
            if events.key == pygame.K_LEFT:
                pos[0] -= 10
            elif events.key == pygame.K_RIGHT:
                pos[0] += 10
            elif events.key == pygame.K_UP:
                pos[1] -= 10
            elif events.key == pygame.K_DOWN:
                pos[1] += 10

    LevelLoad.tiled_map.get_object_by_name("Player").x += pos[0]
    LevelLoad.tiled_map.get_object_by_name("Player").y += pos[1]

    return False

CAMERA = 10



def main():
    done = False

    while not done:
        done = events()
        clock.tick(60)

    pygame.quit()


main()




