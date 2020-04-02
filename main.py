"GenAI project"

import pygame as pg
import random
import math
import creatures_eat as c_e


WIDTH  = 900
HEIGHT = 600
FPS    = 30

pg.init()
BLACK = (0,0,0)

# Параметры работы приложения
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("MyTask")
clock = pg.time.Clock()
screen.fill(BLACK);
running = True
food_mas = []
enemy_mas = []

#----------------Еда-----------------------
all_s = pg.sprite.Group()	
for i in range(300):
	rand_eat_x = random.randrange(1,899)
	rand_eat_y = random.randrange(1,599)
	eat = c_e.Eat(rand_eat_x, rand_eat_y)
	all_s.add(eat.food)
	food_mas.append(eat)

#--------------Существо-------------------
enemy_s = pg.sprite.Group()
for i in range(15):
	rand_enemy_x = random.randrange(1,899)
	rand_enemy_y = random.randrange(1,599)
	enemy = c_e.Creature(rand_enemy_x, rand_enemy_y)
	enemy_s.add(enemy.enemy)
	enemy_mas.append(enemy)

all_s.add(enemy_s)
print("food_mas ",food_mas)
print("enemy_mas ", enemy_mas)
print("all_s", all_s)
#---------Цикл программы------------------
def distance(food_mas, enemy_mas):
	index = {}
	min_dist = 10000
	ind = None

	for i in range(len(enemy_mas)):
		
		for j in range(len(food_mas)):

			foodX  = food_mas[i].food.rect.x
			foodY  = food_mas[i].food.rect.y
			enemyX = enemy_mas[i].enemy.rect.x 
			enemyY = enemy_mas[i].enemy.rect.y
			dist   = abs(math.sqrt((foodX - enemyX)**2 + (foodY - enemyY)**2))

			if min_dist > dist:
				min_dist = dist
				ind = j				

	return index

print(distance(food_mas, enemy_mas))
	

while running:
	clock.tick(FPS)
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
	# Отрисовка еды
	all_s.draw(screen)
	#enemy_s.draw(screen)
	#print("eat - > ", all_s)
	#print("enemy - > ", enemy_s)
	pg.display.update()
pg.quit()