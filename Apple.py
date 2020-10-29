from pygame import Surface
class Apple():
	def __init__(self, x, y, width, height, color):
		self.width = width
		self.height = height
		self.image = Surface((self.width, self.height))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.image.fill(color)
	def draw(self, window):
		window.blit(self.image, (self.rect.x, self.rect.y))