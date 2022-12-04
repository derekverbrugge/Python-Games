# Import the random and curses modules to generate random numbers and handle keyboard input
import random
import curses

# Initialize the curses library to capture keyboard input
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)

# Define the different types of fish that can be caught
fish = ["trout", "bass", "salmon", "catfish", "pike"]

# Define the initial state of the game
pond = fish
basket = []

# Define a function to catch a fish from the pond
def catch_fish():
  # Select a random fish from the pond
  caught_fish = random.choice(pond)
  # Remove the caught fish from the pond
  pond.remove(caught_fish)
  # Add the caught fish to the player's basket
  basket.append(caught_fish)
  # Print a message indicating the player caught a fish
  stdscr.addstr("You caught a " + caught_fish + "!\n")

# Print a message indicating the player is at the pond
stdscr.addstr("You are at the pond. There are many fish swimming in the water.\n")

# Main game loop
while True:
  # Get the next keyboard input from the player
  c = stdscr.getch()
  # If the player pressed the up arrow key, attempt to catch a fish
  if c == curses.KEY_UP:
    # If there are no fish left in the pond, print a message
    if len(pond) == 0:
      stdscr.addstr("There are no more fish in the pond.\n")
    # Otherwise, catch a fish
    else:
      catch_fish()
  # If the player pressed the down arrow key, print the contents of the player's basket
  elif c == curses.KEY_DOWN:
    stdscr.addstr("Basket: " + str(basket) + "\n")

# Clean up the curses library
curses.endwin()
