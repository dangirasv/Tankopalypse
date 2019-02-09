import pygame
from pygame.sprite import Sprite


class Obstacle(Sprite):
	def __init__(self, screen, layout, x, y):
		super().__init__()
		self.screen = screen
		self.x = x
		self.y = y
		# Load images
		self.image = pygame.image.load('images/sandbag_beige_' + layout + '.bmp').convert()
		self.rect = self.image.get_rect()
		
		# Default obstacle position
		self.rect.x = x
		self.rect.y = y
	
	def blitme(self):
		"""Draw obstacle at provided location"""
		self.screen.blit(self.image, self.rect)
