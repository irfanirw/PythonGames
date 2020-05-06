def show_board():
    print("\n" * 100)
    print("| " + board_content[7] + " | " + board_content[8] + " | " + board_content[9] + " |")
    print("=============")
    print("| " + board_content[4] + " | " + board_content[5] + " | " + board_content[6] + " |")
    print("=============")
    print("| " + board_content[1] + " | " + board_content[2] + " | " + board_content[3] + " |")

def check_empty(position):
    global board_content
    if (board_content[position] is "X" or board_content[position] is "O"):
        return False
    else:
        return True

def player_input(player_mark):
    position = ' '
    choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while position not in choices:
        position = input("Make your move '" + player_mark + "' (1-9): ")
        while check_empty(int(position)) is False:
            print("Choose another position")
            position = input("Make your move " + player_mark + " (1-9): ")
    board_content [int(position)] = player_mark
    return int(position)

def check_win(player_mark):
    global win
    global draw
    if (board_content[1] == board_content[2] == board_content[3] == player_mark or
        board_content[4] == board_content[5] == board_content[6] == player_mark or
        board_content[7] == board_content[8] == board_content[9] == player_mark or
        board_content[1] == board_content[4] == board_content[7] == player_mark or
        board_content[2] == board_content[5] == board_content[8] == player_mark or
        board_content[3] == board_content[6] == board_content[9] == player_mark or
        board_content[1] == board_content[5] == board_content[9] == player_mark or
        board_content[3] == board_content[5] == board_content[7] == player_mark):
        win = True
        return win
    elif board_content.count(" ") is 1:
        draw = True
        print("Game draw")
        return draw

def choose_player():
    first_player = ""
    player_choice = ["X", "O"]
    while first_player not in player_choice:
        first_player = input("Choose your marker (X or O): ").upper()
    return first_player

if __name__ == '__main__':
    board_content = [" "] * 10
    win = False
    draw = False
    game_on = True
    if choose_player() == 'X':
        count = 0
    else:
        count = 1
    show_board()
    while game_on:
        if count%2 is 0:
            player_mark = 'X'
        else:
            player_mark = 'O'
        player_input(player_mark)
        game_on = not check_win(player_mark)
        show_board()
        count+=1
        show_board()
        if win:
            print("Player '" + player_mark + "' win")
        elif draw:
            print("Game is draw")

input("Press Enter to close")