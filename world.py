from cell import Cell
from copy import copy, deepcopy
import time

class World:
	def __init__(self, rows, cols):
		self.grid = [[Cell(x,y) for x in range(rows)] for y in range(cols)]
		self.rows = rows
		self.cols = cols

	def advance(self):
		new_grid = deepcopy(self.grid)

		for x in range(self.rows):
			for y in range(self.cols):
				 newCellState = self.getCellDestiny(self.grid[x][y])
				 
				 if newCellState:
				 	new_grid[x][y].setAlive()
				 else:
				 	new_grid[x][y].kill()
		self.grid = new_grid

	def getCellDestiny(self, cell):
		if cell.isAlive():
			return not self.shouldKill(cell)
		return self.shouldBirth(cell)


	def shouldKill(self, cell):
		numNeighbors = self.getNumNeighbors(cell)
		return numNeighbors < 2 or numNeighbors > 3

	def getNumNeighbors(self, cell):
		rowStart = cell.row - 1
		rowEnd = rowStart + 2
		colStart = cell.col - 1
		colEnd = colStart + 2
		numNeighbors = 0

		if rowStart == 0:
			rowStart = 0
		if rowEnd == self.rows:
			rowEnd = self.rows - 1
		if colStart == 0:
			colStart = 0
		if colEnd == self.cols:
			colEnd = self.cols - 1

		for r in range(rowStart, rowEnd+1):
			for c in range(colStart, colEnd+1):
				neighbor = self.grid[c][r]
				if neighbor.isAlive():
					numNeighbors+= 1
		if cell.isAlive():
			numNeighbors-= 1
		return numNeighbors

	def shouldBirth(self, cell):
		if self.getNumNeighbors(cell) == 3:
			return True
		return False

	def init_cell(self, row, col):
		self.grid[row][col].setAlive()	
