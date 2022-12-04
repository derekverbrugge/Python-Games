# Define the rooms and items in the game
cave = ["You are in a dark cave.", ["torch"], []]
treasure_room = ["You are in a room filled with treasure.", [], ["gold coins", "diamond"]]

# Define the starting room
current_room = cave

# Define the directions the player can move
directions = ["north", "south", "east", "west"]

# Define a function to move the player to a different room
def move(direction):
  global current_room
  if direction == "north":
    current_room = treasure_room
  else:
    print("You can't go that way.")

# Print the initial description of the current room
print(current_room[0])

# Print the items in the current room
print("Items:", current_room[1])

# Print the treasures in the current room
print("Treasures:", current_room[2])

# Prompt the player to enter a direction to move
direction = input("Enter a direction to move (north, south, east, or west): ")

# Move the player in the specified direction
move(direction)

# Print the description of the new room
print(current_room[0])

# Print the items in the new room
print("Items:", current_room[1])

# Print the treasures in the new room
print("Treasures:", current_room[2])
