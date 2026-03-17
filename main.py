import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0, 0, 0)
    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # grouped objects that can be updated
    updatable = pygame.sprite.Group()

    # grouped objectst that can be drawn
    drawable = pygame.sprite.Group()

    # Player is the name of the class, not an instance of it
    # (This must be done before any Player objects are created)
    Player.containers = (updatable, drawable)
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        # rendering
        screen.fill(color)
        for instance in drawable:
            instance.draw(screen)
        pygame.display.flip() 
        
        
        

if __name__ == "__main__":
    main()
