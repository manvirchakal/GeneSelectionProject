import pygame
import os
import random
from agent import AntAgent

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Gene Selection")

WHITE = (255,255,255)

STEP = 1

FPS = 60

NUMBER_ANTS = 60*2

ANT_IMAGE = pygame.image.load(os.path.join('Assets','ant.png'))
ANT = pygame.transform.rotate(pygame.transform.scale(ANT_IMAGE, (40,40)), 320)

def draw_window(ants):
	WIN.fill(WHITE)
	for ant_agent_pair in ants:
		ant = ant_agent_pair[0]
		WIN.blit(ANT, (ant.x, ant.y))

	pygame.display.update()

def main():
	ants = []

	for i in range(NUMBER_ANTS):		
		ant = pygame.Rect(random.choice(range(1000)), random.choice(range(1000)), 40, 40)
		agent = AntAgent(ant.x, ant.y)
		ant_agent_pair = (ant, agent)
		ants.append(ant_agent_pair)

	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for ant_agent_pair in ants:
			ant = ant_agent_pair[0]
			agent = ant_agent_pair[1]
			agent.move(ant, WIDTH, HEIGHT, STEP)

		draw_window(ants)

	pygame.quit()

if __name__ == '__main__':
	main()