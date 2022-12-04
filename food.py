class Food():
	def __init__(self, x_pos, y_pos):
		self.x = x_pos
		self.y = y_pos
		self.replenish_value = 100

	def acquire(self, agent):
		agent.replenish(self.replenish_value)