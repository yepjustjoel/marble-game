"""
Show the proper way to organize a game using the a game class.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Explanation video: http://youtu.be/O4Y5KrNgP_c
"""

import pygame
import random
import math

# --- Global constants ---
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# --- Classes ---


class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """

    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 1

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()

# Board Class
class GameBoard:
    def __init__(self, numPlayers, colors, playerTypes):
        self.numPlayers = numPlayers
        self.player_list = [None] * numPlayers
        self.segment_list = [None] * numPlayers
        for playerIdx in range (self.numPlayers):
            self.player_list[playerIdx] = Player(color, playerType)
            angle = math.radians((360/numPlayers)*playerIdx)
            center = (100 * math.cos(angle), 100 * math.sin(angle))
            self.segment_list[playerIdx] = Segment(color, center, angle)
      
# Segment Class
class Segment(pygame.sprite.Sprite):
    # Init
    def __init__(self, color, center, angle):
        super().__init__()
        self.color   = color
        self.image = pygame.transform.rotate(pygame.Surface([20, 20]), math.degrees(angle))
        self.rect = self.image.get_rect()
        self.rect.x = center[0]
        self.rect.y = center[1]
        pygame.draw.circle(self.image,self.color,(self.rect.x+10,self.rect.y+10),10)


# Board Location Class
class BoardLocation(pygame.sprite.Sprite):

    locType = "play"
    index   = 0
    color   = BLUE
    full    = False

    # Init
    def __init__(self, locType, index, color, full):
        super().__init__()
        self.locType = locType # Should be one of: home, play, base
        self.index   = index
        self.color   = color
        self.full    = full # Boolean
        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image,self.color,(self.rect.x+10,self.rect.y+10),10)

    #def update(self):
    #    """ Update the player location. """
    #    pos = pygame.mouse.get_pos()
    #    self.rect.x = pos[0]
    #    self.rect.y = pos[1]

    # Setters
    def set_locType(self, new_locType):
        self.locType = new_locType
    def set_index(self, new_index):
        self.index = new_index
    def set_color(self, new_color):
        self.color = new_color
    def set_full(self, new_full):
        self.full = new_full

    # Getters
    def get_locType(self):
        return self.locType
    def get_index(self):
        return self.index
    def get_color(self):
        return self.color
    def get_full(self):
        return self.full

class Player(pygame.sprite.Sprite):
    """ This class represents the player. """
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image,(0,255,0),(self.rect.x+10,self.rect.y+10),10)

    def update(self):
        """ Update the player location. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """

    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """

        self.score = 0
        self.game_over = False

        # Create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the block sprites
        for i in range(50):
            block = Block()

            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

        # Create a board location for testing
        self.segment1 = Segment(RED,(20,1),math.radians(60))
        self.all_sprites_list.add(self.segment1)

        # Create a board location for testing
        # self.boardLocation = BoardLocation("play",0,BLUE,False)
        # self.all_sprites_list.add(self.boardLocation)

        # Create the player
        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False

    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()

            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            # Check the list of collisions.
            for block in blocks_hit_list:
                self.score += 1
                print(self.score)
                # You can do something with "block" here.

            if len(self.block_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(WHITE)

        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


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

    # Create an instance of the Game class
    game = Game()

    # Main game loop
    while not done:

        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        game.run_logic()

        # Draw the current frame
        game.display_frame(screen)

        # Pause for the next frame
        clock.tick(60)

    # Close window and exit
    pygame.quit()

# Call the main function, start up the game
if __name__ == "__main__":
    main()
