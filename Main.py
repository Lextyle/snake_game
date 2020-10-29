import pygame
from Apple import *
from SnakeHed import *
from random import randint
window = pygame.display.set_mode((700, 700))
tile_width = tile_height = 10
apple = Apple(randint(0, 700 - tile_width), randint(0, 700 - tile_height), tile_width, tile_height, (200, 0, 0))
snake_hed = SnakeHed(700 // 2 - tile_width // 2, 700 // 2 - tile_height // 2, tile_width, tile_height, (0, 200, 0))
snake_tail = []
while True:
	pygame.time.delay(60)
	window.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		snake_hed.update(event)
		break
	last_score = snake_hed.score
	snake_hed.move(apple, snake_tail)
	present_score = snake_hed.score
	if snake_hed.die:
		pygame.quit()
	if present_score > last_score:
		apple = Apple(randint(0, 700 - tile_width), randint(0, 700 - tile_height), tile_width, tile_height, (200, 0, 0))
		snake_tail.append(SnakeHed(0, 0, tile_width, tile_height, (0, 150, 0)))
	apple.draw(window)
	for snake_detal in snake_tail:
		snake_detal.draw(window)
	snake_hed.draw(window)
	pygame.display.update()