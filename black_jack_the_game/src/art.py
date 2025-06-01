def TWO(card_set: str) -> str: 
	return f" _____\n|2    |\n|  {card_set}  |\n|     |\n|  {card_set}  |\n|____Z|"

def THREE(card_set: str) -> str: 
	return f" _____\n|3    |\n| {card_set} {card_set} |\n|     |\n|  {card_set}  |\n|____E|"

def FOUR(card_set: str) -> str: 
	return f" _____\n|4    |\n| {card_set} {card_set} |\n|     |\n| {card_set} {card_set} |\n|____h|"

def FIVE(card_set: str) -> str: 
	return f" _____\n|5    |\n| {card_set} {card_set} |\n|  {card_set}  |\n| {card_set} {card_set} |\n|____S|"

def SIX(card_set: str) -> str:
	return f" _____\n|6    |\n| {card_set} {card_set} |\n| {card_set} {card_set} |\n| {card_set} {card_set} |\n|____9|"

def SEVEN(card_set: str) -> str:
	return f" _____\n|7    |\n| {card_set} {card_set} |\n|{card_set} {card_set} {card_set}|\n| {card_set} {card_set} |\n|____L|"

def EIGHT(card_set: str) -> str:
	return f" _____\n|8    |\n|{card_set} {card_set} {card_set}|\n| {card_set} {card_set} |\n|{card_set} {card_set} {card_set}|\n|____8|"

def NINE(card_set: str) -> str:
	return f" _____\n|9    |\n|{card_set} {card_set} {card_set}|\n|{card_set} {card_set} {card_set}|\n|{card_set} {card_set} {card_set}|\n|____6|"

def TEN(card_set: str) -> str:
	return f" _____\n|10 {card_set} |\n|{card_set} {card_set} {card_set}|\n|{card_set} {card_set} {card_set}|\n|{card_set} {card_set} {card_set}|\n|___0I|"

JACK_CLUBS = " _____\n|J  mm|\n| o {)|\n|o o% |\n| | % |\n|__%%[|"

JACK_SPADES = " _____\n|J  mm|\n| ^ {)|\n|(.)% |\n| | % |\n|__%%[|"

JACK_HEARTS = " _____\n|J  mm|\n|(v){)|\n| V % |\n|   % |\n|__%%[|"

JACK_DIAMONDS = " _____\n|J  mm|\n|/\\ {)|\n|\\/ % |\n|   % |\n|__%%[|"

QUEEN_CLUBS = " _____\n|Q  ww|\n| o {)|\n|o o%(|\n| |%%%|\n|__%%O|"

QUEEN_SPADES = " _____\n|Q  ww|\n| ^ {)|\n|(.)%(|\n| |%%%|\n|__%%O|"

QUEEN_HEARTS = " _____\n|Q  ww|\n|(v){)|\n| V %(|\n|  %%%|\n|__%%O|"

QUEEN_DIAMONDS = " _____\n|Q  ww|\n|/\\ {)|\n|\\/ %(|\n|  %%%|\n|__%%O|"

KING_CLUBS = " _____\n|K  WW|\n| o {)|\n|o o%%|\n| |%%%|\n|__%%>|"

KING_SPADES = " _____\n|K  WW|\n| ^ {)|\n|(.)%%|\n| |%%%|\n|__%%>|"

KING_HEARTS = " _____\n|K  WW|\n|(v){)|\n| V %%|\n|  %%%|\n|__%%>|"

KING_DIAMONDS = " _____\n|K  WW|\n|/\\ {)|\n|\\/ %%|\n|  %%%|\n|__%%>|"

ACE_CLUBS = " _____\n|A _  |\n| ( ) |\n|(_._)|\n|  |  |\n|____V|"

ACE_SPADES = " _____\n|A .  |\n| /.\\ |\n|(_._)|\n|  |  |\n|____V|"

ACE_HEARTS = " _____\n|A_ _ |\n|( v )|\n| \\ / |\n|  V  |\n|____V|"

ACE_DIAMONDS = " _____\n|A ^  |\n| / \\ |\n| \\ / |\n|  v  |\n|____V|"

BACK = " _____\n|a a a|\n| a a |\n|a a a|\n| a a |\n|a_a_a|"