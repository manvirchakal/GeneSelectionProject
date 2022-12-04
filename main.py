import pygame
import os
import random
from agent import AntAgent
from food import Food

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Gene Selection")

WHITE = (255,255,255)

STEP = 1

MAX_STEPS = range(7000,10000)

FPS = 60

NUMBER_ANTS = 15

NUMBER_LEAF = 15

LEAF_REPLENISH_RATE = STEP*300

ANT_IMAGE = pygame.image.load(os.path.join('Assets','ant.png'))
LEAF_IMAGE = pygame.image.load(os.path.join('Assets','leaf.png'))

ANT = pygame.transform.rotate(pygame.transform.scale(ANT_IMAGE, (40,40)), 320)
LEAF = pygame.transform.rotate(pygame.transform.scale(LEAF_IMAGE, (40,40)), 0)

def draw_window(ants, leaves):
	WIN.fill(WHITE)
	for ant_agent_pair in ants:
		ant = ant_agent_pair[0]
		WIN.blit(ANT, (ant.x, ant.y))

	for leaf_particle_pair in leaves:
		leaf = leaf_particle_pair[0]
		WIN.blit(LEAF, (leaf.x, leaf.y))

	pygame.display.update()

def respawn_food(leaves):
	leaf_particle = pygame.Rect(random.choice(range(1000)), random.choice(range(1000)), 40, 40)
	leaf = Food(leaf_particle.x, leaf_particle.y)
	leaf_particle_pair = (leaf_particle, leaf)
	leaves.append(leaf_particle_pair)

def main():
	ants = []

	leaves = []

	for i in range(NUMBER_LEAF):
		leaf_particle = pygame.Rect(random.choice(range(1000)), random.choice(range(1000)), 40, 40)
		leaf = Food(leaf_particle.x, leaf_particle.y)
		leaf_particle_pair = (leaf_particle, leaf)
		leaves.append(leaf_particle_pair)

	for i in range(NUMBER_ANTS):		
		ant = pygame.Rect(random.choice(range(1000)), random.choice(range(1000)), 40, 40)
		agent = AntAgent(ant.x, ant.y, random.choice(MAX_STEPS))
		ant_agent_pair = (ant, agent)
		ants.append(ant_agent_pair)

	steps = 0
	clock = pygame.time.Clock()
	run = True
	while run:
		steps += 1
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for ant_agent_pair in ants:
			ant = ant_agent_pair[0]
			agent = ant_agent_pair[1]
			agent.move(ant, WIDTH, HEIGHT, STEP)

			if agent.get_steps_taken() >= agent.get_max_steps():
				ants.remove(ant_agent_pair)

		for leaf_particle_pair in leaves:
			leaf_particle = leaf_particle_pair[0]
			leaf = leaf_particle_pair[1]

			for ant_agent_pair in ants:
				ant = ant_agent_pair[0]
				agent = ant_agent_pair[1]

				if agent.x in range(leaf.x - 5, leaf.x + 5) and agent.y in range(leaf.y - 5, leaf.y + 5):
					leaf.acquire(agent)
					leaves.remove(leaf_particle_pair)
					print("Success")

		if steps%LEAF_REPLENISH_RATE == 0:
			respawn_food(leaves)
			print("respawned")

		if len(ants) == 0:
			run = False

		draw_window(ants, leaves)

	pygame.quit()

if __name__ == '__main__':
	main()