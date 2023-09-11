from maze import Maze

try:
	userSize = int(input("Enter the side length of the maze you would like to generate as an integer: "))
except ValueError:
	print("Please enter an integer to get a size other than the default of 20")
	userSize = 20

maze = Maze(userSize)
maze.generate_maze()
maze.print()
print("Welcome to 2D maze")