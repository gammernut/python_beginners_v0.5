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

    # board = [
    #     [cell1, cell3, cell3],
    #     [r2_c1, r2_c1, r2_c1],
    #     [r3_c1, r3_c1, r3_c1]
    # ]


if __name__ == '__main__':
    main()
