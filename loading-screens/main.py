import pygame
from settings import *
from sprites import *
import sys
import time




class Game(object):
    def __init__(self):
        # Set up a level to load
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.currentLevelNumber = 0
        self.levels = []
        """self.levels.append(screen 1)"""
        self.levels.append(Level(fileName="resources/level5.tmx"))
        self.currentLevel = self.levels[self.currentLevelNumber]



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            # Get keyboard input and move player accordingly


        return False

    def update(self):
        pass

    # Draw level, player, overlay
    def draw(self, screen):
        screen.fill(BACKGROUND)
        self.currentLevel.draw(screen)
        pygame.display.flip()


    def show_start_screen(self):
        self.screen.fill(BACKGROUND)

        startnewgame_surf = pygame.Surface((SCREEN_WIDTH, 60))
        self.startnewgame_collide = startnewgame_surf.get_rect()
        startnewgame_font = pygame.font.SysFont("comicsansms", 37)
        startnewgame_text = startnewgame_font.render("Start new game", True, (30, 90, 90))
        # text, true, colour
        self.screen.blit(startnewgame_surf, (0, 0))
        self.screen.blit(startnewgame_text, (SCREEN_WIDTH/2.5, 0))

        highscore_surf = pygame.Surface((SCREEN_WIDTH, 60))
        self.highscore_collide = highscore_surf.get_rect()
        highscore_font = pygame.font.SysFont("comicsansms", 37)
        highscore_text = highscore_font.render("Highscores", True, (30, 90, 90))
        # text, true, colour
        self.screen.blit(highscore_surf, (0, 180))
        self.screen.blit(highscore_text, (SCREEN_WIDTH / 2.5, 180))

        pygame.display.flip()

    def show_high_score_screen(self):
        pass

def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Screen loading code")
    clock = pygame.time.Clock()
    done = False
    game = Game()

    startscreenshown = False
    while not done:
        while startscreenshown == False:
            game.show_start_screen()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if game.startnewgame_collide.collidepoint(mouse_pos):
                        startscreenshown = True
                        print("Start Game Button Clicked")
                    mouse_pos2 = event.pos
                    if game.highscore_collide.collidepoint(mouse_pos2):
                        show_high_score_screen = True
                        print("Highscore Button Clicked")
                    
        done = game.events()
        game.update()
        game.draw(screen)
        clock.tick(60)

    pygame.quit()


main()