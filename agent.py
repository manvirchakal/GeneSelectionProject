import random

class AntAgent():
	def __init__(self, x_pos, y_pos, max_steps):
		self.x = x_pos
		self.y = y_pos
		self.current_x_vector = random.randrange(4)
		self.random_change_factor = 0.01
		self.steps_taken = 0
		self.max_steps = max_steps

	def set_x(self, x_pos):
		x = x_pos

	def set_y(self, y_pos):
		y = y_pos

	def get_steps_taken(self):
		return self.steps_taken

	def get_max_steps(self):
		return self.max_steps

	def move(self, ant, WIDTH, HEIGHT, STEP):
		if ant.x <= 0:
			direction_choices = [1,2,3]
			vector_x = random.choice(direction_choices)
			self.current_x_vector = vector_x
			vector_y = random.randrange(3)

		if ant.y <= 0:
			direction_choices = [0,2,3]
			vector_x = random.choice(direction_choices)
			self.current_x_vector = vector_x
			vector_y = random.randrange(3)

		if ant.x >= WIDTH - 40:
			direction_choices = [0,1,3]
			vector_x = random.choice(direction_choices)
			self.current_x_vector = vector_x
			vector_y = random.randrange(3)

		if ant.y >= HEIGHT - 40:
			direction_choices = [0,1,2]
			vector_x = random.choice(direction_choices)
			self.current_x_vector = vector_x
			vector_y = random.randrange(3)

		else:
			if self.random_change_factor*100 > random.choice(range(100)):
				vector_x = random.randrange(4)
			else:
				vector_x = self.current_x_vector

			vector_y = random.randrange(3)

		if vector_x == 0 and vector_y == 1:
			ant.x += -STEP

		if vector_x == 0 and vector_y == 0:
			ant.x += -STEP
			ant.y += STEP

		if vector_x == 0 and vector_y == 2:
			ant.x += -STEP
			ant.y += -STEP

		if vector_x == 1 and vector_y == 1:
			ant.y += -STEP

		if vector_x == 1 and vector_y == 0:
			ant.x += -STEP
			ant.y += -STEP

		if vector_x == 1 and vector_y == 2:
			ant.x += STEP
			ant.y += -STEP

		if vector_x == 2 and vector_y == 1:
			ant.x += STEP

		if vector_x == 2 and vector_y == 0:
			ant.x += STEP
			ant.y += -STEP

		if vector_x == 2 and vector_y == 2:
			ant.x += STEP
			ant.y += STEP

		if vector_x == 3 and vector_y == 1:
			ant.y += STEP

		if vector_x == 3 and vector_y == 0:
			ant.x += STEP
			ant.y += STEP

		if vector_x == 3 and vector_y == 2:
			ant.x += -STEP
			ant.y += STEP

		self.x = ant.x 
		self.y = ant.y
		self.current_x_vector = vector_x
		self.steps_taken += STEP