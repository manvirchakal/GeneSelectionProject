import random

class AntAgent():
	def __init__(self, x_pos, y_pos):
		self.x = x_pos
		self.y = y_pos
		self.current_x_vector = random.randrange(4)

	def set_x(self, x_pos):
		x = x_pos

	def set_y(self, y_pos):
		y = y_pos

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
			vector_x = self.current_x_vector
			vector_y = random.randrange(3)
		
		#vector_y = random.randrange(3)

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