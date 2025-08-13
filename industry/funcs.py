from objects import Player

def to_produce():
	return input('produce?: ').lower().startswith('y')

#Funcs for Manufactories
def coil2_to_points(owner: Player, none):
	print('2 coil -> 2 vp (2x)')
	for counts in range(2):
		if owner.coil < 2:
			print('not enough coil')
			break
		else:
			if to_produce():
				owner.coil -= 2
				owner.victory_points += 2
			else: break

def mt_n_coil_to_upgrade(owner: Player, none):
	print('modernization_tocken + coil -> upgrade')
	while True:
		if owner.coil < 1 or owner.modernization_tockens < 1:
			print('not enough resources')
			break
		else:
			if to_produce():
				owner.coil -= 1
				owner.modernization_tockens -= 1
				owner.modernisation()
			else: break

def oil_to_points(owner: Player, none):
	print('oil -> 4 vp (1x)')
	if owner.oil < 1:
		print('not enough oil')
	else:
		if to_produce():
			owner.oil -= 1
			owner.victory_points += 4

def coil3_to_points(owner: Player, none):
	print('3 coil -> 4 vp (1x)')
	if owner.coil < 3:
		print('not enough coil')
	else:
		if to_produce():
			owner.coil -= 3
			owner.victory_points += 4

def coil_n_steel_to_points(owner: Player, none):
	print('coil + steel -> 4 vp (1x)')
	if owner.coil < 1 or owner.steel < 1:
		print('not enough resources')
	else:
		if to_produce():
			owner.coil -= 1
			owner.steel -= 1
			owner.victory_points += 4

def steel_to_points_2x(owner: Player, none):
	print('steel -> 2 vp (2x)')
	for counts in range(2):
		if owner.steel < 1:
			print('not enough steel')
			break
		else:
			if to_produce():
				owner.steel -= 1
				owner.victory_points += 2
			else: break

def steel_n_oil_to_points_mod(owner: Player, card_status):
	if card_status:
		print('(if mod) steel + oil -> 7 vp (2x)')
		for counts in range(2):
			if owner.steel < 1 or owner.oil < 1:
				print('not enough resources')
				break
			else:
				if to_produce():
					owner.steel -= 1
					owner.oil -= 1
					owner.victory_points += 7
				else: break

def mt_to_points_mod(owner: Player, card_status):
	if card_status:
		print('modernisation_tocken -> 5 vp (2x)')
		for counts in range(2):
			if owner.modernization_tockens < 1:
				print('not enough modernisation_tockens')
				break
			else:
				if to_produce():
					owner.modernization_tockens -= 1
					owner.victory_points += 5
				else:
					break

def coil_n_oil_to_points_mod(owner: Player, card_status):
	if card_status:
		print('(if mod) coil + oil -> 6 vp (2x)')
		for counts in range(2):
			if owner.coil < 1 or owner.oil < 1:
				print('not enough resources')
				break
			else:
				if to_produce():
					owner.coil -= 1
					owner.oil -= 1
					owner.victory_points += 6
				else: break

def steel_to_oil(owner: Player, bet_tocken):
	print('steel -> oil')
	for counts in range(bet_tocken):
		if owner.steel < 1:
			print('not enough steel')
			break
		else:
			if to_produce():
				owner.steel -= 1
				owner.oil += 1
			else: break

def steel_to_mt(owner: Player, none):
	print('steel -> modernisation_tocken (1x)')
	if owner.steel < 1:
		print('not enough steel')
	else:
		if to_produce():
			owner.steel -= 1
			owner.modernization_tockens += 1

def steel_to_points_4x_mod(owner: Player, card_status):
	if card_status:
		print('steel -> 2 vp (4x)')
		for counts in range(4):
			if owner.steel < 1:
				print('not enough steel')
				break
			else:
				if to_produce():
					owner.steel -= 1
					owner.victory_points += 2
				else: break

def mt_to_vp_mod(owner: Player, card_status):
	if card_status:
		print('modernisation_tocken -> 5 vp (2x)')
		for counts in range(2):
			if owner.modernization_tockens < 1:
				print('not enough modernisation_tockens')
				break
			else:
				if to_produce():
					owner.modernization_tockens -= 1
					owner.victory_points += 5
				else: break

def coil3_mod(owner: Player, card_status):
	if card_status:
		owner.coil += 3

def steel_to_mt(owner: Player, bet_tocken):
	print('steel -> modernisation_tocken')
	for counts in range(bet_tocken):
		if owner.steel < 1:
			print('not enough steel')
			break
		else:
			if to_produce():
				owner.steel -= 1
				owner.modernization_tockens += 1
			else: break

def coil_to_oil(owner: Player, bet_tocken):
	print('2 coil -> oil')
	for counts in range(bet_tocken):
		if owner.coil < 2:
			print('not enough coil')
			break
		else:
			if to_produce():
				owner.coil -= 2
				owner.oil += 1
			else: break

def coil_to_oil_2x(owner: Player, none):
	print('2 coil -> oil')
	for counts in range(2):
		if owner.coil < 2:
			print('not enough coil')
			break
		else: 
			if to_produce():
				owner.coil -= 2
				owner.oil += 1
			else: break

def mt_mod(owner: Player, card_status):
	if card_status:
		owner.modernization_tockens += 1

def oil_to_points_mod(owner: Player, card_status):
	if card_status:
		print('oil -> 4 vp (2x)')
		for counts in range(2):
			if owner.oil < 1:
				print('not enough oil')
				break
			else:
				if to_produce():
					owner.oil -= 1
					owner.victory_points += 4
				else: break
