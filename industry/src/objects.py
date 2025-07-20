# RESOURCES = ['coil', 'steel', 'oil', 'modernization_tockens']


#Manufactories
class Manufactories():
	pass

#Player
class Player():
	coil = 0
	steel = 0
	oil = 0
	modernization_tockens = 0
	bet_tockens = [1, 2, 3, 4]
	def __init__(self, manufacturer : str, queue : int, start_manufactorie):
		MANUFACTORER = manufacturer
		queue = queue
		manufactories = []
		manufactories.append(start_manufactorie)
	
