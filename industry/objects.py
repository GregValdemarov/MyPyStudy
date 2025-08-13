# RESOURCES = ['coil', 'steel', 'oil', 'modernization_tockens']

#Player
class Player():
	victory_points = 0
	coil = 0
	steel = 0
	oil = 0
	modernization_tockens = 0
	bet_tockens = [1, 2, 3, 4]
	manufactories = []
	def __init__(self, manufacturer : str, queue : int, start_manufactorie):
		self.MANUFACTURER = manufacturer
		self.queue = queue
		self.manufactories.append(start_manufactorie)
	def modernisation(self):
		for card in self.manufactories:
			print(card.description)
		while True:
			try: 
				choice = int(input('pick a Manufactorie to modernise\n(enter a number counting from top to bottom): '))-1 
				if choice < 0 or choice > len(self.manufactories):
					print('!incorrect value!')
					continue
			except:
				print('!incorrect value!')
				continue
			else: break
		self.manufactories[choice].is_modernised = True
	
#Effects that cards (Manufactories) may cause
class Effect():
	def __init__(self, coil=0, steel=0, oil=0, modernization_tockens=0, funcs = []):
		self.effect = {'coil': coil, 'steel': steel, 'oil': oil, 'modernization_tockens': modernization_tockens, 'funcs': funcs}

#Manufactories
class Manufactories():
	is_modernised = False
	owner = None
	def __init__(self, description, compensation, production):
		self.compensation = compensation.effect
		self.production = production.effect
		self.description = description
	def Compensation(self, bet_tocken = 1):
		self.owner.coil += self.compensation['coil']*bet_tocken
		self.owner.steel += self.compensation['steel']*bet_tocken
		self.owner.oil += self.compensation['oil']*bet_tocken
		self.owner.modernization_tockens += self.compensation['modernization_tockens']*bet_tocken
		for func in self.compensation['funcs']:
			func(self.owner, bet_tocken)
	def Production(self):
		self.owner.coil += self.production['coil']
		self.owner.steel += self.production['steel']
		self.owner.oil += self.production['oil']
		self.owner.modernization_tockens += self.production['modernization_tockens']
		for func in self.production['funcs']:
			func(self.owner, self.is_modernised)





