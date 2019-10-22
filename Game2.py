import random
def unbreakable(msg):
  while True:
    try:
      num=int(input(msg))
      if num >2:
        raise
      elif num < 1:
        raise
      else:
        break
    except:
      print("please choose numbers 1 or 2!")
  return num
while True:
  print ("What was the first game ever made?")
  userInput = unbreakable("\nPong(1) or Pac-man(2)")
  if userInput ==(1):
    print("Correct! Next Question\n What was the very first console ever created?")
  elif userInput ==(2):
    print("Incorrect. Pong was the first video game. In October 1958, \nPhysicist William Higinbotham created what is thought to be the first video game,\nit was a very simple tennis game.")
    break 
  userInput = unbreakable("\nMagnavox Odyssey(1) or Nintendo game boy(2)")
  if userInput ==(1): 
    print("Correct! Third Question.\n What is the highest selling video game?")
  elif userInput ==(2):
    print("Incorrect. The world’s first home video game console is none other than the \nMagnavox Odyssey. It was extremely simple, and it didn’t even have sound capabilities. \nOnly three dots were shown on the screen when connected to the television, and the dots would change depending on the game being played. However, people loved it, and it sold \nover 100 million units. It is still one of the highest selling consoles of all time, \nand these consoles are now worth hundreds of dollars in vintage condition.")
    break
  userInput = unbreakable("\nTetris(1) or Minecraft(2)")
  if userInput ==(1):
      print("Incorrect! The best-selling video game to date is Minecraft, a sandbox video game \noriginally released for Microsoft Windows, Mac OS X, and Linux in 2011. The game \nhas been ported to a wide range of platforms, selling over 176 million copies.")
      break
  if userInput ==(2):	
        print("Correct! Next Question.What is the highest selling console?")
  userInput = unbreakable("\nNintendo DS(1) or PlayStation 2(2)")
  if userInput ==(1):
      print("Incorrect. PlayStation 2 remains the best-selling video game console of all time. Sony's beloved system tops Nintendo DS by roughly 5 million units sold, while handily \noutselling every other console in existence.")
      break
  if userInput ==(2):
      print("Correct! Next Question. What was the first game to be \nrated mature?")
  userInput = unbreakable("\nMortal kombat(1)or Death race(2)")
  if userInput ==(2):
      print("Incorrect! Mortal kombat, congressional hearings were held and the Entertainment \nSoftware Rating Board (ESRB) was established in 1994, two years after the release of the game. Unsurprisingly, the game was the first to receive the Mature rating.")
      break 
  if userInput ==(1):
      print("Correct! Next Question. What was the earliest First-person shooter (FPS) game? ")
  userInput = unbreakable("\nMaze War(1) or Wolfenstein 3D(2)")
  if userInput ==(2):
    print ("Incorrect! Maze War (also known as The Maze Game, Maze Wars, Mazewar or simply Maze) is a 1973 computer game which originated or disseminated a number of concepts used in \nthousands of games to follow, and is considered one of the earliest examples of, or \nprogenitor of a first-person shooter.")
    break
  elif userInput ==(1):
      print ("Correct! Next Question. Which Company first proposed the idea \nof microtransactions")
  userInput = unbreakable("\nElectronic Arts(1) or Microsoft(2)")
  if userInput ==(1):
      print("Incorrect! Microsoft had previously offered up the idea of microtransactions in early \n2005 and they  first gained large-scale visibility in 2006.")
      break
  elif userInput ==(2):
      print("Correct! Next Question. What was the first video game to be \nmade into a movie?")
  userInput = unbreakable("\nSuper Mario Bros(1) or Space Invaders(2)")
  if userInput ==(1):
      print("Correct! Next Question. When was the first video game competition")
  elif userInput ==(2):
      print("Incorrect! Super Mario Bros was the first video game movie, released in 1993 American \nfantasy comedy film loosely based on the video game series by Nintendo.")
      break
  userInput = unbreakable("\nOctober 19 1972(1) or march 26 1984 (2)")
  if userInput ==(2):
      print("Incorrect! The earliest known video game competition took place on 19 October 1972 at \nStanford University for the game Spacewar. ")
      break
  elif userInput ==(1):
      print("Correct! Next Question. What was the first VR console?")
  userInput = unbreakable("\n iGlasses(1) or The Nintendo Virtual Boy(2)")
  if userInput ==(1):
      print("Incorrect -1! The Nintendo Virtual Boy (originally known as VR-32) was a 3D gaming console that was hyped to be the first ever portable console that could display true 3D graphics.It was first released in Japan and North America at a price of $180 but it was a \ncommercial failure despite price drops.")
  elif userInput ==(2):
      print("Correct +1!")
      break 
print("\nThanks for playing!") 
"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 100

PLAYER_START_X = 64
PLAYER_START_Y = 225


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.coin_list = None
        self.wall_list = None
        self.foreground_list = None
        self.background_list = None
        self.dont_touch_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Where is the right edge of the map?
        self.end_of_map = 0

        # Level
        self.level = 1

        # Load sounds
        self.collect_coin_sound = arcade.load_sound("sounds/coin1.wav")
        self.jump_sound = arcade.load_sound("sounds/jump1.wav")
        self.game_over = arcade.load_sound("sounds/gameover1.wav")

    def setup(self, level):
        """ Set up the game here. Call this function to restart the game. """

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.foreground_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite("images/player_1/player_stand.png",
                                           CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)

        # --- Load in a map from the tiled editor ---

        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'
        # Name of the layer that has items for pick-up
        coins_layer_name = 'Coins'
        # Name of the layer that has items for foreground
        foreground_layer_name = 'Foreground'
        # Name of the layer that has items for background
        background_layer_name = 'Background'
        # Name of the layer that has items we shouldn't touch
        dont_touch_layer_name = "Don't Touch"

        # Map name
        map_name = f"map2_level_{level}.tmx"

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = my_map.map_size.width * GRID_PIXEL_SIZE

        # -- Background
        self.background_list = arcade.tilemap.process_layer(my_map,
                                                            background_layer_name,
                                                            TILE_SCALING)

        # -- Foreground
        self.foreground_list = arcade.tilemap.process_layer(my_map,
                                                            foreground_layer_name,
                                                            TILE_SCALING)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(my_map,
                                                      platforms_layer_name,
                                                      TILE_SCALING)

        # -- Coins
        self.coin_list = arcade.tilemap.process_layer(my_map,
                                                      coins_layer_name,
                                                      TILE_SCALING)

        # -- Don't Touch Layer
        self.dont_touch_list = arcade.tilemap.process_layer(my_map,
                                                            dont_touch_layer_name,
                                                            TILE_SCALING)

        # --- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.background_list.draw()
        self.wall_list.draw()
        self.coin_list.draw()
        self.dont_touch_list.draw()
        self.player_list.draw()
        self.foreground_list.draw()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.BLACK, 18)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(self.collect_coin_sound)
            # Add one to the score
            self.score += 1

        # Track if we need to change the viewport
        changed_viewport = False

        # Did the player fall off the map?
        if self.player_sprite.center_y < -100:
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            # Set the camera to the start
            self.view_left = 0
            self.view_bottom = 0
            changed_viewport = True
            arcade.play_sound(self.game_over)

        # Did the player touch something they should not?
        if arcade.check_for_collision_with_list(self.player_sprite,
                                                self.dont_touch_list):
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

            # Set the camera to the start
            self.view_left = 0
            self.view_bottom = 0
            changed_viewport = True
            arcade.play_sound(self.game_over)

        # See if the user got to the end of the level
        if self.player_sprite.center_x >= self.end_of_map:
            # Advance to the next level
            self.level += 1

            # Load the next level
            self.setup(self.level)

            # Set the camera to the start
            self.view_left = 0
            self.view_bottom = 0
            changed_viewport = True

        # --- Manage Scrolling ---

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed_viewport = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed_viewport = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed_viewport = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed_viewport = True

        if changed_viewport:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame()
    window.setup(window.level)
    arcade.run()


if __name__ == "__main__":
    main()
Note