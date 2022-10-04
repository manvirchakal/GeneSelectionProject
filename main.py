import pygame
import os

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Gene Selection")

WHITE = (255,255,255)

FPS = 60

ANT_IMAGE = pygame.image.load(os.path.join('Assets','ant.png'))
ANT = pygame.transform.scale(ANT_IMAGE, (40,40))

def draw_window(ant):
	WIN.fill(WHITE)
	WIN.blit(ANT, (ant.x, ant.y))
	pygame.display.update()

def main():
	ant = pygame.Rect(100, 300, 40, 40)

	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
	
		draw_window(ant)

	pygame.quit()

if __name__ == '__main__':
	main()