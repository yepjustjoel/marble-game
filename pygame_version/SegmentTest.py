import pygame

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
MAX_BRD_DIM = SCREEN_WIDTH-200
NUM_PLAYERS = 4
SEGMENT_LEN = MAX_BRD_DIM

# Location Class
class Location(pygame.sprite.Sprite):
    # Init
    def __init__(self, location):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Marbles!")

    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()

    # Setup stuff
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(Location((SCREEN_WIDTH/2,SCREEN_HEIGHT/2)))

    # Set up all of the board locations
    for side in range(4):
        xBase = SCREEN_WIDTH/2 + SEGMENT_LEN*math.cos(math.pi*side)/2
        yBase = SCREEN_WIDTH/2 + SEGMENT_LEN*math.sin(math.pi*side)/2
        all_sprites_list.add(Location((xBase, yBase)))
        # for location in range (18):
        #     xLoc = xBase + 
        #     all_sprites_list.add(Location((xLoc, yLoc)))

    # Main game loop
    while not done:

        # Process events (keystrokes, mouse clicks, etc)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              done = True

        # Update object positions, check for collisions

        # Draw the current frame
        screen.fill(WHITE)
        pygame.draw.aalines(screen,BLACK,True,[[100,100],[600,100],[600,600],[100,600]])
        all_sprites_list.draw(screen)
        pygame.display.flip()

        # Pause for the next frame
        clock.tick(60)

    # Close window and exit
    pygame.quit()

# Call the main function, start up the game
if __name__ == "__main__":
    main()
