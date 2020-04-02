import random

#проверка рандома 
def checkProbability(percent):
	if int(random.random() * 100) < percent:
		return True
	else:
		return False

def reproduction(cre):

	#для мутации
	tmp = { 1: "speed",
			2: "sensitive",
			3: "reprodChance" }

	if checkProbability(cre["reprodChance"]):

		speed = cre["speed"] + random.randint(-5, 5)
		sensitive = cre["sensitive"] + random.randint(-5, 5)
		reprodChance = cre["reprodChance"] + random.randint(-5, 5)

		speed = speed if speed < 40 else 40
		sensitive = sensitive if sensitive < 40 else 40
		reprodChance = reprodChance if reprodChance < 40 else 40

		speed = 5 if speed < 5 else speed
		sensitive = 5 if sensitive < 5 else sensitive
		reprodChance = 5 if reprodChance < 5 else reprodChance


		CreatureS = { "speed": speed, 
			 		  "size": random.randint(1, 3),
			 		  "sensitive": sensitive,
			 	 	  "reprodChance": reprodChance }

		#мутация
		if checkProbability(3):
			CreatureS[tmp[random.randint(1, 3)]] += random.randint(3, 7)

		return CreatureS

	return None


Creature = { "speed": 13.1, 
			 "size": 3,
			 "sensitive": 15,
			 "reprodChance": 20 }

#for i in range(1, 100):
#	print(reproduction(Creature))
