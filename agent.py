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

	def move(self, ant, WIDTH, HEIGHT):
		if ant.x <= 0:
			vector_x = random.randint(1,3)
			vector_y = random.randrange(3)

		if ant.y <= 0:
			direction_choices = [0,2,3]
			index_choice = randrange(3)
			vector_x = direction_choices[index_choice]
			vector_y = random.randrange(3)

		if ant.x >= WIDTH:
			direction_choices = [0,1,3]
			index_choice = randrange(3)
			vector_x = direction_choices[index_choice]
			vector_y = random.randrange(3)

		if ant.y >= HEIGHT:
			direction_choices = [0,1,2]
			index_choice = randrange(3)
			vector_x = direction_choices[index_choice]
			vector_y = random.randrange(3)

		else:
			vector_x = self.current_x_vector
			vector_y = random.randrange(3)
		
		#vector_y = random.randrange(3)

		if vector_x == 0 and vector_y == 0:
			ant.x += -1

		if vector_x == 0 and vector_y == -1:
			ant.x += -1
			ant.y += 1

		if vector_x == 0 and vector_y == 1:
			ant.x += -1
			ant.y += -1

		if vector_x == 1 and vector_y == 0:
			ant.y += -1

		if vector_x == 1 and vector_y == -1:
			ant.x += -1
			ant.y += -1

		if vector_x == 1 and vector_y == 1:
			ant.x += 1
			ant.y += -1

		if vector_x == 2 and vector_y == 0:
			ant.x += 1

		if vector_x == 2 and vector_y == -1:
			ant.x += 1
			ant.y += -1

		if vector_x == 2 and vector_y == 1:
			ant.x += 1
			ant.y += 1

		if vector_x == 3 and vector_y == 0:
			ant.y += 1

		if vector_x == 3 and vector_y == -1:
			ant.x += 1
			ant.y += 1

		if vector_x == 3 and vector_y == 1:
			ant.x += -1
			ant.y += 1

		self.x = ant.x 
		self.y = ant.y
		self.current_x_vector = vector_x
		print(vector_x,' ',vector_y,'\t\t',ant.x,ant.y)