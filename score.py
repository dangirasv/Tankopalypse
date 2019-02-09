import pygame.font
from pygame.sprite import Group

from tank import Tank


class Score():
	"""A class to report character score information."""
	
	def __init__(self, game_set, screen):
		self.game_set = game_set
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.text_color = (20, 20, 20)
		self.font = pygame.font.SysFont(None, 32)
		
		self.prep_players()
		self.prep_lives()
		
	def prep_players(self):
		"""Prepare player names and their possition on screen"""
		self.p1_image = self.font.render('Player 1', True, self.text_color,
			self.game_set.name_bg_color)
		self.p2_image = self.font.render('Player 2', True, self.text_color,
			self.game_set.name_bg_color)
		
		self.p1_image_rect = self.p1_image.get_rect()
		self.p1_image_rect.left = 30
		self.p1_image_rect.top = 30
		
		self.p2_image_rect = self.p2_image.get_rect()
		self.p2_image_rect.right = self.screen_rect.right - 30
		self.p2_image_rect.top = 30
		
	def show_score(self):
		"""Draw players and lives on screen"""
		self.screen.blit(self.p1_image, self.p1_image_rect)
		self.screen.blit(self.p2_image, self.p2_image_rect)
		self.p1_lives.draw(self.screen)
		self.p2_lives.draw(self.screen)
		
	def prep_lives(self):
		"""Creating two sprite groups for both players to show lives"""
		self.p1_lives = Group()
		self.p2_lives = Group()
		for tank_number in range(self.game_set.p1_lives):
			tank1 = Tank(self.game_set, self.screen, 'lives', 'p1')
			tank1.rect.x = 30 + tank_number * (tank1.rect.width + 5)
			tank1.rect.y = 60
			self.p1_lives.add(tank1)
		for tank_number in range(self.game_set.p2_lives):
			tank2 = Tank(self.game_set, self.screen, 'lives', 'p2')
			tank2.rect.x = 884 + tank_number * (tank2.rect.width + 5)
			tank2.rect.y = 60
			self.p2_lives.add(tank2)			
