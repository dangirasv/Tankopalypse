import pygame
from pygame.sprite import Sprite


class Tank(Sprite):
	def __init__(self, game_set, screen, color, player):
		"""Initialize the tanks"""
		super().__init__()  # Tank class inherits from Sprite class
		# super(Tank, self).__init__() for 2.7 syntax
		self.screen = screen
		self.game_set = game_set
		self.color = color

		# set up tank location and facing direction (taken from settings class) depending on which players thank it is
		self.loc_x = eval('game_set.' + player + '_start_loc_x')
		self.loc_y = eval('game_set.' + player + '_start_loc_y')
		self.facing = eval('game_set.' + player + '_start_facing')
		
		# Load the tank images and get its rect, check for what player
		self.image_u = pygame.image.load('images/tank_' + color + '_u.bmp').convert()
		self.image_r = pygame.image.load('images/tank_' + color + '_r.bmp').convert()
		self.image_d = pygame.image.load('images/tank_' + color + '_d.bmp').convert()
		self.image_l = pygame.image.load('images/tank_' + color + '_l.bmp').convert()
		self.image_explode = pygame.image.load('images/smoke.png').convert_alpha()
		self.rect = self.image_u.get_rect()
		self.screen_rect = screen.get_rect()
		# starting tank position and facing direction
		self.rect.x = self.loc_x
		self.rect.y = self.loc_y
		self.image = eval(self.facing)
				
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		# Movement flags
		self.moving_up = False
		self.moving_right = False
		self.moving_down = False
		self.moving_left = False

		self.w = False
		self.d = False
		self.s = False
		self.a = False

	def update(self):
		"""Update the tank's position based on the movement flags."""
		if self.moving_up and self.rect.top > 0:
			self.y -= self.game_set.tank_speed_factor
			self.image = self.image_u
			
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.game_set.tank_speed_factor
			self.image = self.image_d
			
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.game_set.tank_speed_factor
			self.image = self.image_r
			
		if self.moving_left and self.rect.left > 0:
			self.x -= self.game_set.tank_speed_factor
			self.image = self.image_l

		# Update rect object
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		"""Draw the tank at its current location."""
		self.screen.blit(self.image, self.rect)
	
	def starting_loc(self):
		"""Set tank to starting position"""
		self.x = self.loc_x
		self.y = self.loc_y
		self.image = eval(self.facing)
