import utill


# todo choose the players
# todo create the board
# todo show the board
# todo choose initial player
# todo until someone wins choose location, mark it toggle active player and update the board
# game over!


def main():
    utill.print_header('Tic Tac Toe')
    # Board is a list of rows
    # rows are a list of cells
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    # choose initial player
    # the first player is index/number 0 the second player is index/number 1
    # ie. player 1 is 0 player 2 is 1
    active_player_index = 0
    players = ["Jacob", "Computer"]
    symbols = ["X", "O"]
    player = players[active_player_index]
    # UNTIL SOMEONE WINS
    while not find_winner(board):
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)

        if not choose_location(board, symbol):
            print("thats not a option, try again.")
            continue

        # toggle active player
        active_player_index = (active_player_index + 1) % len(players)

    print(f'Game Over {player} has won with the board: ')
    show_board(board)


def choose_location(board, symbol):
    row = int(input("choose which row"))
    column = int(input("choose which column"))

    row -= 1
    column -= 1
    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False

    cell = board[row][column]
    if cell is not None:
        return False

    board[row][column] = symbol
    return True


def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"it is {player}'s turn. Here's the board:")
    print()


def find_winner(board):
    # win by rows
    rows = board
    for row in rows:
        symbol1 = row[0]
        if symbol1 and all(symbol1 == cell for cell in row):
            return True

    # win by columns
    columns = []
    for col_idx in range(0, 3):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx],
        ]
        columns.append(col)

    for col in columns:
        symbol1 = col[0]
        if symbol1 and all(symbol1 == cell for cell in col):
            return True

    # win by diagonals
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    for diag in diagonals:
        symbol1 = diag[0]
        if symbol1 and all(symbol1 == cell for cell in diag):
            return True

    return False


if __name__ == '__main__':
    main()
