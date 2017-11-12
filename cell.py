
class Cell:
	def __init__(self, row, col, living=False):
		self.row = row
		self.col = col
		self.living = living

	def isAlive(self):
		return self.living

	def setAlive(self):
		self.living = True

	def kill(self):
		self.living = False
