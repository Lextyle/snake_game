from pygame import Surface, K_UP, K_LEFT, K_DOWN, K_RIGHT, KEYDOWN
from pygame.sprite import collide_rect
class SnakeHed():
	def __init__(self, x, y, width, height, color):
		self.width = width
		self.height = height
		self.image = Surface((width, height))
		self.image.fill((color))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.direction = "STOP"
		self.speed = self.width
		self.score = 0
		self.die = False
	def update(self, event):
		if event.type == KEYDOWN:
			if event.key == K_UP:
				if self.direction != "DOWN":
					self.direction = "UP"
			if event.key == K_LEFT:
				if self.direction != "RIGHT":
					self.direction = "LEFT"
			if event.key == K_DOWN:
				if self.direction != "UP":
					self.direction = "DOWN"
			if event.key == K_RIGHT:
				if self.direction != "LEFT":
					self.direction = "RIGHT"
	def move(self, apple, snake_tail):
		last_pos = [self.rect.x, self.rect.y]
		for snake_detal in snake_tail:
			last_pos_2 = [snake_detal.rect.x, snake_detal.rect.y]
			snake_detal.rect.x = last_pos[0]
			snake_detal.rect.y = last_pos[1]
			last_pos = last_pos_2
		if self.rect.x < 0:
			self.rect.x = 700 - self.width
		if self.rect.x > 700 - self.width:
			self.rect.x = 0
		if self.rect.y < 0:
			self.rect.y = 700 - self.height
		if self.rect.y > 700 - self.height:
			self.rect.y = 0
		if self.direction == "UP":
			self.rect.y -= self.speed
		if self.direction == "LEFT":
			self.rect.x -= self.speed
		if self.direction == "DOWN":
			self.rect.y += self.speed
		if self.direction == "RIGHT":
			self.rect.x += self.speed
		if collide_rect(self, apple):
			self.score += 1
		for snake_detal in snake_tail:
			if collide_rect(self, snake_detal):
				self.die = True
	def draw(self, window):
		window.blit(self.image, (self.rect.x, self.rect.y))