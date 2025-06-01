import random
from src import art

SETS = ("&", "^", "v", "o")
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Card:
	def __init__(self, card_set="a", card_value=""):
		self.set = card_set
		self.value = card_value
	def art(self) -> str:
		if self.value == '2': return art.TWO(self.set)
		elif self.value == '3': return art.THREE(self.set)
		elif self.value == '4': return art.FOUR(self.set)
		elif self.value == '5': return art.FIVE(self.set)
		elif self.value == '6': return art.SIX(self.set)
		elif self.value == '7': return art.SEVEN(self.set)
		elif self.value == '8': return art.EIGHT(self.set)
		elif self.value == '9': return art.NINE(self.set)
		elif self.value == '10': return art.TEN(self.set)
		elif self.value == 'J' and self.set == '^': return art.JACK_CLUBS
		elif self.value == 'J' and self.set == '&': return art.JACK_SPADES
		elif self.value == 'J' and self.set == 'v': return art.JACK_HEARTS
		elif self.value == 'J' and self.set == 'o': return art.JACK_DIAMONDS
		elif self.value == 'Q' and self.set == '^': return art.QUEEN_CLUBS
		elif self.value == 'Q' and self.set == '&': return art.QUEEN_SPADES
		elif self.value == 'Q' and self.set == 'v': return art.QUEEN_HEARTS
		elif self.value == 'Q' and self.set == 'o': return art.QUEEN_DIAMONDS
		elif self.value == 'K' and self.set == '^': return art.KING_CLUBS
		elif self.value == 'K' and self.set == '&': return art.KING_SPADES
		elif self.value == 'K' and self.set == 'v': return art.KING_HEARTS
		elif self.value == 'K' and self.set == 'o': return art.KING_DIAMONDS
		elif self.value == 'A' and self.set == '^': return art.ACE_CLUBS
		elif self.value == 'A' and self.set == '&': return art.ACE_SPADES
		elif self.value == 'A' and self.set == 'v': return art.ACE_HEARTS
		elif self.value == 'A' and self.set == 'o': return art.ACE_DIAMONDS
		elif self.set == 'a': return art.BACK
		
class Deck_of_cards:
	DECK = []
	FOLD = []
	
	def __init__(self):
		for card_set in SETS:
			for card_value in VALUES:
				card = Card(card_set, card_value)
				self.DECK.append(card) 

	def pick_card(self) -> Card:
		card = random.choice(self.DECK)
		self.DECK.remove(card)
		self.FOLD.append(card)
		return card

	def shuffle(self) -> None: 
		new_deck = []
		for n in range(len(self.DECK)):
			card = self.pick_card()
			new_deck.append(card)
		self.DECK = new_deck
		self.FOLD = []

class Human:

	def __init__(self):
		self.cards = []
		self.cards_value = sum([n.value_int for n in self.cards])
		self.cards_value_int = 0

	def pick_card(self, card: Card) -> None:
		self.cards.append(card)
		try: 
			self.cards_value_int += int(card.value)
		except:
			if card.value in 'JQK':
				self.cards_value_int += 10
			elif card.value == "A" and (self.cards_value_int + 11 <= 21):
				self.cards_value_int += 11
			elif card.value == "A" and (self.cards_value_int + 11 > 21):
				self.cards_value_int += 1
			else:
				print("Неверное значение карты!")	
	
	def fold_cards(self) -> None:
		self.cards = []	
		self.cards_value_int = 0
	
class Player(Human):
	def __init__(self, balance=500):
		Human.__init__(self)
		self.balance = balance
		