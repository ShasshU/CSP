# gui tic-tac-toe project
# by shassh umamaheswaran
# period 4 AP CSP

import tkinter as tk

# colors for the board and text
BG_COLOR     = "#1a1a2e"
CELL_BG      = "#16213e"
CELL_HOVER   = "#0f3460"
TEXT_COLOR   = "#ffffff"
ACCENT_COLOR = "#5dade2"
X_COLOR      = "#f38ba8"   # pinkish for X
O_COLOR      = "#a6e3a1"   # greenish for O
WIN_COLOR    = "#f9e2af"   # yellow highlight when someone wins
WIN_FG       = "#1a1a2e"

# all 8 ways to win, using the index layout below
# 0  1  2
# 3  4  5
# 6  7  8
WIN_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]               # diagonals
]

# setting up the window
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("420x560")
window.resizable(False, False)   # don't want the window to be resizable
window.configure(bg=BG_COLOR)

# game state variables
board          = [""] * 9   # 9 spots, all empty to start
current_player = "X"        # X always goes first
game_over      = False
cells          = []          # stores the 9 label widgets for the board


def start_game():
    # hides the start screen and shows the actual game board
    frame_start.place_forget()
    frame_game.place(relwidth=1, relheight=1)


def handle_click(event):
    global current_player, game_over

    # figure out which cell was clicked using its position in the list
    index = cells.index(event.widget)

    # do nothing if the game ended or the spot is already taken
    if game_over or board[index] != "":
        return

    # mark the board and update the label
    board[index] = current_player
    color = X_COLOR if current_player == "X" else O_COLOR
    cells[index].configure(text=current_player, fg=color)

    # check if that move just won the game
    winning_combo = check_winner()
    if winning_combo:
        # highlight the three winning cells
        for i in winning_combo:
            cells[i].configure(bg=WIN_COLOR, fg=WIN_FG)
        label_status.configure(
            text=f"Player {current_player} Wins!", fg=ACCENT_COLOR)
        game_over = True
        return

    # if no empty spots left and nobody won, it's a draw
    if "" not in board:
        label_status.configure(text="It's a Draw!", fg=ACCENT_COLOR)
        game_over = True
        return

    # switch to the other player
    current_player = "O" if current_player == "X" else "X"
    next_color = X_COLOR if current_player == "X" else O_COLOR
    label_status.configure(
        text=f"Player {current_player}'s Turn", fg=next_color)


def check_winner():
    # go through every possible winning combo and see if all three match
    for combo in WIN_COMBOS:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != "":
            return combo   # return the winning combo so we can highlight it
    return None


def reset_game():
    global board, current_player, game_over

    # reset all the variables back to the start
    board          = [""] * 9
    current_player = "X"
    game_over      = False

    # clear every cell visually
    for cell in cells:
        cell.configure(text="", fg=TEXT_COLOR, bg=CELL_BG)

    label_status.configure(text="Player X's Turn", fg=X_COLOR)


def on_cell_enter(event):
    # only show the hover color if the cell is empty and game is still going
    index = cells.index(event.widget)
    if board[index] == "" and not game_over:
        event.widget.configure(bg=CELL_HOVER)


def on_cell_leave(event):
    # put the cell back to normal when the mouse leaves
    index = cells.index(event.widget)
    if board[index] == "" and not game_over:
        event.widget.configure(bg=CELL_BG)


# start screen
#  shown before the game loads
frame_start = tk.Frame(window, bg=BG_COLOR)
frame_start.place(relwidth=1, relheight=1)

tk.Label(frame_start, text="Tic-Tac-Toe",
         font=("Arial", 40, "bold"),
         bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=(80, 6))

tk.Label(frame_start,
         text="Two players take turns marking X and O.\nFirst to get 3 in a row wins!",
         font=("Arial", 13), bg=BG_COLOR, fg=TEXT_COLOR,
         justify="center").pack(pady=(0, 36))

# little X / O preview showing what the colors look like
frame_preview = tk.Frame(frame_start, bg=BG_COLOR)
frame_preview.pack(pady=(0, 44))

tk.Label(frame_preview, text="  X  ", font=("Arial", 28, "bold"),
         bg=CELL_BG, fg=X_COLOR,
         relief=tk.RAISED, bd=3, padx=8, pady=6).pack(side=tk.LEFT, padx=12)

tk.Label(frame_preview, text="  O  ", font=("Arial", 28, "bold"),
         bg=CELL_BG, fg=O_COLOR,
         relief=tk.RAISED, bd=3, padx=8, pady=6).pack(side=tk.LEFT, padx=12)

# using Label instead of Button because macOS ignores bg/fg on actual Buttons
btn_start = tk.Label(frame_start, text="  Start Game  ",
                      font=("Arial", 16, "bold"),
                      bg=ACCENT_COLOR, fg=BG_COLOR,
                      relief=tk.RAISED, bd=2, cursor="hand2",
                      padx=20, pady=12)
btn_start.pack()
btn_start.bind("<Button-1>", lambda e: start_game())
btn_start.bind("<Enter>",    lambda e: btn_start.configure(bg="#3d8ec9"))
btn_start.bind("<Leave>",    lambda e: btn_start.configure(bg=ACCENT_COLOR))


# game screen
# hidden until start button is clicked
frame_game = tk.Frame(window, bg=BG_COLOR)

tk.Label(frame_game, text="Tic-Tac-Toe",
         font=("Arial", 26, "bold"),
         bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=(22, 4))

label_status = tk.Label(frame_game, text="Player X's Turn",
                         font=("Arial", 14),
                         bg=BG_COLOR, fg=X_COLOR)
label_status.pack(pady=(0, 14))

frame_board = tk.Frame(frame_game, bg=BG_COLOR)
frame_board.pack()

# building the 3x3 grid
#  same Label trick as above for macOS color support
for i in range(9):
    cell = tk.Label(frame_board, text="", font=("Arial", 34, "bold"),
                    width=4, height=2,
                    bg=CELL_BG, fg=TEXT_COLOR,
                    relief=tk.RAISED, bd=3, cursor="hand2")
    cell.bind("<Button-1>", handle_click)
    cell.bind("<Enter>",    on_cell_enter)
    cell.bind("<Leave>",    on_cell_leave)
    cell.grid(row=i // 3, column=i % 3, padx=6, pady=6)
    cells.append(cell)

# reset button
btn_reset = tk.Label(frame_game, text="  Reset Game  ",
                      font=("Arial", 13, "bold"),
                      bg=ACCENT_COLOR, fg=BG_COLOR,
                      relief=tk.RAISED, bd=2, cursor="hand2",
                      padx=18, pady=10)
btn_reset.pack(pady=24)
btn_reset.bind("<Button-1>", lambda e: reset_game())
btn_reset.bind("<Enter>",    lambda e: btn_reset.configure(bg="#3d8ec9"))
btn_reset.bind("<Leave>",    lambda e: btn_reset.configure(bg=ACCENT_COLOR))

window.mainloop()


"""
Reflection

What was the hardest part?
    Getting the win detection right. I kept thinking I could just check
    the button text directly but storing everything in the board list
    made it a lot cleaner. The part that actually tripped me up was
    forgetting to check that board[a] != "", so at the very start of
    the game it was saying someone already won because all three empty
    strings matched each other. Once I added that condition it worked.

What did you learn?
    I learned a lot about how event-driven programming works, because instead
    of the program running top to bottom, it just waits for user input
    and responds to it. I also learned the importance of separating game
    logic into functions rather than putting everything in one place.
    Using a list to track the board state made checking wins much simpler
    than trying to read from the buttons directly.

What would you improve?
    I would add a scoreboard that persists across resets so players can
    track wins over multiple rounds. I would also look into implementing
    a basic computer opponent using a decision-making algorithm, which
    would make the game more replayable when only one person is available.
"""
