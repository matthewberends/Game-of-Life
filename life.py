import time
import sys
import os
from world import World
import Tkinter as tk

GLIDER = {
    (2, 2),
    (2, 1),
    (0, 2),
    (1, 2),
    (1, 0),
}

WINDOW_SIZE = 500

class Life(tk.Tk):
	def __init__(self, start_state, world_size=50, *args, **kwargs):
		self.world = World(world_size, world_size)
		self.set_world(start_state, self.world)

		tk.Tk.__init__(self, *args, **kwargs)
		self.canvas = tk.Canvas(
			self,
			width=WINDOW_SIZE,
			height=WINDOW_SIZE,
			borderwidth=0,
			highlightthickness=0)
		self.canvas.pack(side="top", fill="both", expand="true")

		self.rect = {}
		self.rows = world_size
		self.columns = world_size
		self.cellwidth = WINDOW_SIZE / world_size
		self.cellheight = WINDOW_SIZE / world_size

		for row in range(world_size):
			for col in range(world_size):
				x1 = col*self.cellwidth
				y1 = row * self.cellheight
				x2 = x1 + self.cellwidth
				y2 = y1 + self.cellheight
				self.rect[row,col] = self.canvas.create_rectangle(
					x1,y1,x2,y2, fill="blue", tags="rect")

	def draw_world(self, world):
		self.canvas.itemconfig("rect", fill="grey")
		for c in range(self.world.cols):
			for r in range(self.world.rows):
				if self.world.grid[r][c].isAlive():
					cell = self.rect[r, c]
					self.canvas.itemconfig(cell, fill="red")

	def advance(self):
		self.draw_world(self.world)
		self.world.advance()
		self.after(20, lambda: self.advance())

	def set_world(self, start_state, world):
		for x, y in start_state:
			world.init_cell(x, y)


if __name__ == '__main__':
    life = Life(GLIDER)
    life.advance()
    life.mainloop()
