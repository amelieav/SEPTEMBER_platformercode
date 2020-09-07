import pytmx
import pygame
from pytmx.util_pygame import load_pygame
from settings import *

pygame.init()
SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Base code")
clock = pygame.time.Clock()

tiled_map = load_pygame('resources/level6.tmx', pixelalpha=True)
tilewidth = tiled_map.tilewidth
tileheight = tiled_map.tileheight

coin = pygame.image.load('resources/coin.png').convert_alpha()
coin = pygame.transform.scale(coin, (48,48))
player = pygame.image.load('resources/coin.png').convert_alpha()
player = pygame.transform.scale(player, (48,48))


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    for layer in tiled_map.layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, tile in layer.tiles():
                if tile:
                    SCREEN.blit(tile, [(x * tilewidth) - CAMERA.x + (SCREEN_WIDTH / 2),
                                       (y * tileheight) - CAMERA.y + (SCREEN_HEIGHT / 2)])
        elif isinstance(layer, pytmx.TiledObjectGroup):
            if layer.name == "coin":
                for object in layer:
                    SCREEN.blit(coin,
                                [object.x - CAMERA.x + (SCREEN_WIDTH / 2), object.y - CAMERA.y + (SCREEN_HEIGHT / 2)])

        elif isinstance(layer, pytmx.TiledObjectGroup):
            if layer.name == "Player":
                for object in layer:
                    SCREEN.blit(player, [object.x - CAMERA.x, object.y - CAMERA.y])

    pygame.display.update()


    """
    self.tiles.add(Tile(image=img, x=(x * self.mapObject.tilewidth), y=(y * self.mapObject.tileheight)))
    """

    pos = [0, 0]
    for events in pygame.event.get():  # get all pygame events
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                pos[0] -= 10
            elif events.key == pygame.K_RIGHT:
                pos[0] += 10
            elif events.key == pygame.K_UP:
                pos[1] -= 10
            elif events.key == pygame.K_DOWN:
                pos[1] += 10

    tiled_map.get_object_by_name("Player").x += pos[0]
    tiled_map.get_object_by_name("Player").y += pos[1]

    return False

CAMERA = tiled_map.get_object_by_name("Player")



def main():
    done = False

    while not done:
        done = events()
        clock.tick(60)

    pygame.quit()


main()








"""
import pytmx
import pygame
from pytmx.util_pygame import load_pygame
from settings import *

pygame.init()
SCREEN = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Base code")
clock = pygame.time.Clock()

tiled_map = load_pygame('resources/level6.tmx', pixelalpha=True)
tilewidth = tiled_map.tilewidth
tileheight = tiled_map.tileheight

coin = pygame.image.load('resources/coin.png').convert_alpha()
coin = pygame.transform.scale(coin, (48,48))
player = pygame.image.load('resources/player.png').convert_alpha()
player = pygame.transform.scale(player, (48,48))

CAMERA = tiled_map.get_object_by_name("Player")



def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    for layer in tiled_map.layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, tile in layer.tiles():
                if tile:
                    SCREEN.blit(tile, [(x * tilewidth) - CAMERA.x + (SCREEN_WIDTH / 2),
                                       (y * tileheight) - CAMERA.y + (SCREEN_HEIGHT / 2)])

        elif isinstance(layer, pytmx.TiledObjectGroup):
            if layer.name == "Player":
                for object in layer:
                    SCREEN.blit(player,
                                [object.x - CAMERA.x + (SCREEN_WIDTH / 2), object.y - CAMERA.y + (SCREEN_HEIGHT / 2)])


        elif isinstance(layer, pytmx.TiledObjectGroup):
            if layer.name == "coin":
                for object in layer:
                    SCREEN.blit(player,
                                [object.x - CAMERA.x + (SCREEN_WIDTH / 2), object.y - CAMERA.y + (SCREEN_HEIGHT / 2)])

    pygame.display.update()


    pos = [0, 0]
    for events in pygame.event.get():  # get all pygame events
        if events.type == pygame.KEYDOWN:
            temp = player.rect.topleft
            if events.key == pygame.K_LEFT:
                pos[0] -= 10
            elif events.key == pygame.K_RIGHT:
                pos[0] += 10
            elif events.key == pygame.K_UP:
                pos[1] -= 10
            elif events.key == pygame.K_DOWN:
                pos[1] += 10

    tiled_map.get_object_by_name("Player").x += pos[0]
    tiled_map.get_object_by_name("Player").y += pos[1]

    return False




def main():
    done = False

    while not done:
        done = events()
        clock.tick(60)

    pygame.quit()


main()









"""