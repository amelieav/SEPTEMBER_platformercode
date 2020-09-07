import settings
import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([settings.WIDTH, settings.HEIGHT])
pygame.display.set_caption("settings")

def settings_draw():
    global redtheme_collide
    global bluetheme_collide
    global bigtext_collide
    global smalltext_collide
    screen.fill(settings.background_colour)

    """theme colour buttons"""

    redtheme_surf = pygame.Surface((100, 100))
    redtheme_collide = pygame.Rect(100, 100, 100, 100)
    redtheme_font = pygame.font.SysFont("comicsansms", settings.text_size)
    redtheme_text = redtheme_font.render("R", True, settings.text_colour)
    # text, true, colour
    screen.blit(redtheme_surf, (100, 100))
    screen.blit(redtheme_text, (100, 100))


    bluetheme_surf = pygame.Surface((100, 100))
    bluetheme_collide = pygame.Rect(200, 200, 100, 100)
    bluetheme_font = pygame.font.SysFont("comicsansms", settings.text_size)
    bluetheme_text = bluetheme_font.render("B", True, settings.text_colour)
    # text, true, colour
    screen.blit(bluetheme_surf, (200, 200))
    screen.blit(bluetheme_text, (200, 200))

    """text size buttons"""

    bigtext_surf = pygame.Surface((100, 100))
    bigtext_collide = pygame.Rect(300, 300, 100, 100)
    bigtext_font = pygame.font.SysFont("comicsansms", settings.text_size)
    bigtext_text = bigtext_font.render("Big", True, settings.text_colour)
    # text, true, colour
    screen.blit(bigtext_surf, (300, 300))
    screen.blit(bigtext_text, (300, 300))

    smalltext_surf = pygame.Surface((100, 100))
    smalltext_collide = pygame.Rect(400, 400, 200, 200)
    smalltext_font = pygame.font.SysFont("comicsansms", settings.text_size)
    smalltext_text = smalltext_font.render("Small", True, settings.text_colour)
    # text, true, colour
    screen.blit(smalltext_surf, (400, 400))
    screen.blit(smalltext_text, (400, 400))





    pygame.display.flip()


def settings_main():
    done = False

    while not done:
        settings_draw()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if redtheme_collide.collidepoint(pos):
                    print("Red theme clicked")
                    settings.background_colour = (255, 10, 10)
                elif bluetheme_collide.collidepoint(pos):
                    print("Blue theme clicked")
                    settings.background_colour = (10, 10, 200)
                elif bigtext_collide.collidepoint(pos):
                    print("Big text clicked")
                    settings.text_size = 60
                elif smalltext_collide.collidepoint(pos):
                    print("Small text clicked")
                    settings.text_size = 30

            if event.type == pygame.QUIT:
                done = True

    pygame.quit()


settings_main()
