import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""A class to manage bullets fired from the ship"""
	
	def __init__(self, game_set, screen, player):
		super().__init__()
		self.screen = screen
		self.game_set = game_set
		self.player = player
		
		self.image_u = pygame.image.load('images/bullet_blue_u.png').convert_alpha()  # alpha for see-through background
		self.image_r = pygame.image.load('images/bullet_blue_r.png').convert_alpha()
		self.image_d = pygame.image.load('images/bullet_blue_d.png').convert_alpha()
		self.image_l = pygame.image.load('images/bullet_blue_l.png').convert_alpha()
		self.image = self.image_r
		self.rect = self.image.get_rect()
		self.rect.centerx = player.rect.centerx
		self.rect.centery = player.rect.centery
		
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		self.speed_factor = game_set.bullet_speed_factor
		
		self.direction = 'none'  # will help determine starting direction
		self.is_start = 0

	def update(self):
		"""Move the bullet up the screen."""
		# confirming it's bullets first iteration and assigning its direction if yes
		if self.is_start == 0: 
			if self.player.image == self.player.image_u:
				self.direction = 'up'
			elif self.player.image == self.player.image_r:
				self.direction = 'right'
			elif self.player.image == self.player.image_d:
				self.direction = 'down'
			elif self.player.image == self.player.image_l:
				self.direction = 'left'
		# adding +1 to show that this object already has a direction
		self.is_start += 1
		
		if self.direction == 'up':
			self.y -= self.speed_factor
			self.image = self.image_u
		if self.direction == 'right':
			self.x += self.speed_factor
			self.image = self.image_r
		if self.direction == 'down':
			self.y += self.speed_factor
			self.image = self.image_d
		if self.direction == 'left':
			self.x -= self.speed_factor
			self.image = self.image_l

		# Update rect object
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the bullet at its current location."""
		self.screen.blit(self.image, self.rect)
