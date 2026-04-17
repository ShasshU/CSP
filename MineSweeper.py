import random

def create_board(size):
    # make a size x size grid filled with 0s
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        board.append(row)
    return board

def place_mines(board, num_mines):
    size = len(board)
    placed = 0
    while placed < num_mines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if board[row][col] != 'M':
            board[row][col] = 'M'
            placed += 1

def get_neighbors(board, row, col):
    size = len(board)
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r = row + dr
            c = col + dc
            if 0 <= r < size and 0 <= c < size:
                neighbors.append((r, c))
    return neighbors

def calculate_numbers(board):
    size = len(board)
    for row in range(size):
        for col in range(size):
            if board[row][col] == 'M':
                continue
            count = 0
            for r, c in get_neighbors(board, row, col):
                if board[r][c] == 'M':
                    count += 1
            board[row][col] = count

def display_board(board, revealed, show_all=False):
    size = len(board)
    print("  " + " ".join(str(c) for c in range(size)))
    for row in range(size):
        row_str = str(row) + " "
        for col in range(size):
            if show_all:
                row_str += str(board[row][col]) + " "
            elif revealed[row][col]:
                row_str += str(board[row][col]) + " "
            else:
                row_str += "- "
        print(row_str)

def reveal_cell(board, revealed, row, col):
    # if already revealed, skip
    if revealed[row][col]:
        return True

    revealed[row][col] = True

    if board[row][col] == 'M':
        return False

    # if the cell is empty, reveal neighbors too
    if board[row][col] == 0:
        for r, c in get_neighbors(board, row, col):
            if not revealed[r][c]:
                reveal_cell(board, revealed, r, c)

    return True

def check_win(board, revealed):
    size = len(board)
    for row in range(size):
        for col in range(size):
            if board[row][col] != 'M' and not revealed[row][col]:
                return False
    return True

def get_input(size):
    while True:
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            if 0 <= row < size and 0 <= col < size:
                return row, col
            else:
                print("Out of bounds, try again.")
        except ValueError:
            print("Please enter a number.")

def main():
    print("Select difficulty:")
    print("1. Easy (6x6)")
    print("2. Medium (9x9)")
    print("3. Hard (12x12)")
    choice = input("Choice: ").strip()

    if choice == '2':
        size = 9
        num_mines = 15
    elif choice == '3':
        size = 12
        num_mines = 30
    else:
        size = 6
        num_mines = 6

    board = create_board(size)
    place_mines(board, num_mines)
    calculate_numbers(board)

    revealed = []
    for i in range(size):
        revealed.append([False] * size)

    game_over = False
    won = False

    while not game_over:
        print("\nCurrent Board:")
        display_board(board, revealed)

        row, col = get_input(size)

        if revealed[row][col]:
            print("Already revealed, pick another cell.")
            continue

        safe = reveal_cell(board, revealed, row, col)

        if not safe:
            game_over = True
        elif check_win(board, revealed):
            game_over = True
            won = True

    if won:
        print("\nCurrent Board:")
        display_board(board, revealed)
        print("\nYou win!")
    else:
        print("\nBOOM! You hit a mine.")
        print("\nFull Board:")
        display_board(board, revealed, show_all=True)

main()