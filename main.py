import pygame
import os
from agent import AntAgent

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Gene Selection")

WHITE = (255,255,255)

FPS = 60

NUMBER_ANTS = 60

ANT_IMAGE = pygame.image.load(os.path.join('Assets','ant.png'))
ANT = pygame.transform.rotate(pygame.transform.scale(ANT_IMAGE, (40,40)), 320)

def draw_window(ant):
	WIN.fill(WHITE)
	WIN.blit(ANT, (ant.x, ant.y))
	pygame.display.update()

def main():
	ant = pygame.Rect(0, 0, 40, 40)
	agent = AntAgent(100, 300)

	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
	
		agent.set_x(ant.x)
		agent.set_y(ant.y)
		agent.move(ant, WIDTH, HEIGHT)

		draw_window(ant)

	pygame.quit()

if __name__ == '__main__':
	main()