import time
import sys
import os
from world import World

GLIDER = {
    (2, 2),
    (2, 1),
    (0, 2),
    (1, 2),
    (1, 0),
}

def main(start_state, iterations=100, world_size=30):
	world = World(world_size, world_size)
	set_state(start_state, world)

	for step in range(iterations):
		sys.stdout.write('\033[H')  # move to the top
		sys.stdout.write('\033[J')  # clear the screen
		print "step", step, "\n"
		print_world(world)
		world.advance()
		time.sleep(0.2)

def set_state(start_state, world):
	for x, y in start_state:
		world.init_cell(x, y)

def print_world(world):
	for c in range(world.cols):
		for r in range(world.rows):
			if world.grid[r][c].isAlive():
				sys.stdout.write(u"\u2588")
			else:
				sys.stdout.write(u" ")
		print "\n"

if __name__ == '__main__':
    main(GLIDER)
