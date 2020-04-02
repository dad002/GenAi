
import pygame as pg

class Eat:
	def __init__(self, x, y):
		self.food = pg.sprite.Sprite()
		self.food.image = pg.Surface([5,5])
		self.food.image.fill((29, 251, 201))

		self.food.rect = self.food.image.get_rect()
		self.food.rect.x = x
		self.food.rect.y = y


class Creature:
	def __init__(self, x, y):
		self.enemy_circle = pg.sprite.Sprite()		
		self.enemy = pg.sprite.Sprite()
		
		#self.enemy_circle.image = pg.Surface([12,12])
		self.enemy.image = pg.Surface([8,8])
		
		#self.enemy_circle.image.fill((0,100,21))
		self.enemy.image.fill((0, 252, 21))

		#self.enemy_circle.rect = self.enemy_circle.image.get_rect()
		#self.enemy_circle.rect.x = x
		#self.enemy_circle.rect.y = y

		self.enemy.rect = self.enemy.image.get_rect()
		self.enemy.rect.x = x
		self.enemy.rect.y = y

	def motion(self, target):
		pass
