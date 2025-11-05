import project


def play():
    r1 = [" ", " ", " "]
    r2 = [" ", " ", " "]
    r3 = [" ", " ", " "]
    rows = {"A": r1, "B": r2, "C": r3}

    start_game()
    for turn in range(9):
        if turn % 2 == 0:
            piece = "X"
        else:
            piece = "O"
        print(f"{piece} to move")
        while True:
            try:
                change_grid(rows, piece, input("Coordinate: "))
                break
            except (KeyError, IndexError, ValueError):
                pass
        print_grid(rows)
    print("It's a tie! ")
    play_again()


def change_grid(rows, piece, coordinate):
    row = coordinate[0]
    column = int(coordinate[1]) - 1
    if rows[row][column] == "X" or rows[row][column] == "O":
        raise ValueError
    rows[row][column] = piece
    check_win(rows, piece)


def check_win(rows, piece):
    # Horizontal
    for row in rows.values():
        if (row[0] == row[1] == row[2]) and row[0] != " ":
            game_over(rows, piece)
    # Vertical
    for i in range(3):
        if (rows["A"][i] == rows["B"][i] == rows["C"][i]) and rows["A"][i] != " ":
            game_over(rows, piece)
    # Diagonal
    if (rows["A"][0] == rows["B"][1] == rows["C"][2]) and rows["B"][1] != " ":
        game_over(rows, piece)
    if (rows["A"][2] == rows["B"][1] == rows["C"][0]) and rows["B"][1] != " ":
        game_over(rows, piece)


def game_over(rows, piece):
    print_grid(rows)
    print(f"Game over! Player {piece} wins!")
    play_again()


def print_grid(rows):
    print(f"  {rows["A"][0]}  |  {rows["A"][1]}  |  {rows["A"][2]}")
    print("~~~~~|~~~~~|~~~~~")
    print(f"  {rows["B"][0]}  |  {rows["B"][1]}  |  {rows["B"][2]}")
    print("~~~~~|~~~~~|~~~~~")
    print(f"  {rows["C"][0]}  |  {rows["C"][1]}  |  {rows["C"][2]}")


def start_game():
    print("Welcome to Tic-Tac-Toe! Write your coordinate to begin!")
    print("Write Row (A, B, C) Column (1, 2, 3) with no space (e.g. A1, B3, C2)")
    print("A1 goes to top left, B2 goes to middle, C3 goes to bottom right, etc.")


def play_again():
    again = input("Play again? (y/n): ")
    if again.lower().strip() == "y":
        play()
    else:
        project.continue_or_exit()


if __name__ == "__main__":
    play()
