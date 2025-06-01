from source import *
print_map(game_map)
print("Добро пожаловать в игру \"Крестики нолики\"!\nИнструкция: для того, чтобы сделать ход, введите соответствующую цифру согласно полю выше.\nПервым ходит крестик.")
input("Чтобы начать, нажмите ENTER.")
another_go = 'да'
while one_more(another_go):
    current_go=0
    game_map = [[" " for column in range(3)] for row in range(3)]
    while not win(game_map):
        print_map(game_map)
        move(game_map, current_go)
        if draw(current_go):
            break        
        current_go+=1
    else:
        print_map(game_map)
        if (current_go-1)%2==0:
            winner = "X"
        else:
            winner = "O"
        print(f"Поздравляем! Выиграл {winner}")
    if draw(current_go):
        print_map(game_map)
        print("Ничья!")
    another_go = input("Еще партию? Да/Нет: ")
