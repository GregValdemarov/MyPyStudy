game_map = [[str(column+row+1) for column in range(0,3)] for row in range(0, 7, 3)] 


def print_map(current_map: list) -> None:
    print(
        "   |   |   \n" \
        " {0} | {1} | {2} \n" \
        "   |   |   \n" \
        "———|———|———\n" \
        "   |   |   \n" \
        " {3} | {4} | {5} \n" \
        "   |   |   \n" \
        "———|———|———\n" \
        "   |   |   \n" \
        " {6} | {7} | {8} \n" \
        "   |   |   ".format(current_map[0][0], current_map[0][1], current_map[0][2], current_map[1][0], current_map[1][1], current_map[1][2], current_map[2][0], current_map[2][1], current_map[2][2]) 
    )

def win(current_map:list) -> bool:
    X = ["X", "X", "X"]
    O = ["O", "O", "O"]
    column1 = []
    column2 = []
    column3 = []
    diag1 = []
    diag2 = []
    for i in range(3):
        column1.append(current_map[i][0])
        column2.append(current_map[i][1])
        column3.append(current_map[i][2])
        diag1.append(current_map[i][i])
        diag2.append(current_map[i][2-i])
    return current_map[0][0:]==X or current_map[0][0:]==O or current_map[1][0:]==X or current_map[1][0:]==O or current_map[2][0:]==X or current_map[2][0:]==O or column1==X or column1==O or column2==X or column2==O or column3==X or column3==O or diag1==X or diag1==O or diag2==X or diag2==O

def draw(current_go: int) -> bool:
    return current_go==8
    
def move(current_map:list, current_go:int) -> None:
    if current_go%2==0:
        player='X'
    else: player='O'
    tranlate = {"1":(0, 0), "2":(0,1), "3":(0,2), "4":(1,0), "5":(1,1), "6":(1,2), "7":(2,0), "8":(2,1), "9":(2,2)}
    player_input = (input(f"Ходит {player}: "))
    while player_input not in "1 2 3 4 5 6 7 8 9":
        print_map(current_map) 
        print("ОШИБКА")
        player_input = (input(f"Ходит {player}: "))
    row, column = tranlate[player_input]
    while current_map[row][column]!=" ":
        print_map(current_map)
        print("Это поле уже занято.")
        player_input = (input(f"Ходит {player}: "))
        row, column = tranlate[player_input]
    current_map[row][column] = player

def one_more(another_go:str) -> bool:
    return another_go.lower().startswith('д')