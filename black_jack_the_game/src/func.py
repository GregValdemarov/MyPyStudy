def win(value_cards_p: int, value_cards_d: int) -> int:
	if ((value_cards_p > value_cards_d) or (value_cards_p == 21) or (value_cards_d > 21)) and value_cards_d != 21 and value_cards_p <= 21: 
		#Игрок выиграл
		return 0
	if ((value_cards_p < value_cards_d) or (value_cards_d == 21) or (value_cards_p > 21)) and value_cards_p != 21 and value_cards_d <= 21:
		#Диллер выиграл
		return 1
	if (value_cards_p == value_cards_d == 21) or (value_cards_p > 21 and value_cards_d > 21):
		#Ничья
		return 2

def contin(answer: str) -> bool:
	return answer.lower().startswith('д')


	
	