from src import func, classes

is_game = True

deck = classes.Deck_of_cards()
player = classes.Player()
diller = classes.Human()

while is_game:
	player.fold_cards()
	diller.fold_cards()
	deck.shuffle()
	print("Ваш баланс: " + str(player.balance))

	while True:
		try: 
			dill = int(input("Ваша ставка: "))
			if dill > player.balance:
				print("Некорректная ставка!")
				continue
		except:
			print("Некорректная ставка!")
			continue
		else:
			break

		
	player.balance -= dill
	
	print("Карты диллера: ")
	for i in range(2):
		card = deck.pick_card()
		diller.pick_card(card)
	back = classes.Card()
	print(diller.cards[0].art()+"\n"+back.art()+"\n-------------")

	print("Ваши карты: ")
	for i in range(2):
		card = deck.pick_card()
		player.pick_card(card)
	print(player.cards[0].art()+"\n"+player.cards[1].art())

	if diller.cards[0].value in "JQKA" and player.cards_value_int == 21:
		print("Блэк Джек!")
		if func.contin(input("Забрать ставку? Д/Н: ")):
			player.balance += dill
			if func.contin(input("Еще раунд? Д/Н: ")):
				continue
			else: break
	
	if (player.cards_value_int < 21):
		pick_card = func.contin(input("Взять еще карту? Д/Н: "))
		while pick_card:
			card = deck.pick_card()
			player.pick_card(card)
			print(card.art())
			if player.cards_value_int > 21:
				break
			elif player.cards_value_int == 21:
				print("Блэк Джек!")
				break
			pick_card = func.contin(input("Еще? Д/Н: "))

	print("Ход диллера:")
	print(diller.cards[0].art()+"\n"+back.art()+"\n-------------")
	print(diller.cards[0].art()+"\n"+diller.cards[1].art())
	while (not (func.win(player.cards_value_int, diller.cards_value_int) in [1, 2])) and diller.cards_value_int < 21:
		card = deck.pick_card()
		diller.pick_card(card)
		print(card.art())
		if diller.cards_value_int == 21:
				print("Блэк Джек!")
	result = func.win(player.cards_value_int, diller.cards_value_int)
	if result == 0:
		print("Вы выигрвли!")
		player.balance += round(1.5 * dill)
	elif result == 1:
		print("Вы проиграли (")
	else:
		print("Ничья")
		player.balance += dill

	if player.balance == 0:
		print("Вы обанкротились, конец игры!")
		break
	is_game = func.contin(input("Еще раунд? Д/Н: "))

print("Ваш выходной баланс: " + str(player.balance))