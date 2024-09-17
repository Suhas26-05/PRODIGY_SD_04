import tkinter as tk
from tkinter import font
import random  # Ensure random module is imported

GRID_SIZE = 9
EMPTY_CELL = 0

def is_valid(board, row, col, num):
    """Check if num is a valid number for board[row][col]."""
    if num in board[row]:
        return False
    for r in range(GRID_SIZE):
        if board[r][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def solve_sudoku(board):
    """Solve Sudoku using backtracking."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == EMPTY_CELL:
                for num in range(1, GRID_SIZE + 1):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = EMPTY_CELL
                return False
    return True

def generate_puzzle():
    """Generate a Sudoku puzzle with some cells pre-filled."""
    board = [[EMPTY_CELL] * GRID_SIZE for _ in range(GRID_SIZE)]

    def fill_diagonal_boxes():
        """Fill the diagonal 3x3 boxes."""
        for i in range(0, GRID_SIZE, 3):
            nums = list(range(1, GRID_SIZE + 1))
            random.shuffle(nums)
            for j in range(3):
                for k in range(3):
                    board[i + j][i + k] = nums.pop()

    def remove_numbers():
        """Remove some numbers to create a puzzle."""
        number_of_cells_to_remove = random.randint(40, 60)
        cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE)]
        random.shuffle(cells)
        for r, c in cells[:number_of_cells_to_remove]:
            board[r][c] = EMPTY_CELL

    fill_diagonal_boxes()
    solve_sudoku(board)  # Ensure the board is a valid Sudoku solution
    remove_numbers()    # Create the puzzle
    return board

def extract_board(entries):
    """Extract the board from the Entry widgets."""
    board = []
    for row in range(GRID_SIZE):
        row_values = []
        for col in range(GRID_SIZE):
            value = entries[row][col].get()
            row_values.append(int(value) if value.isdigit() and 1 <= int(value) <= 9 else EMPTY_CELL)
        board.append(row_values)
    return board

def validate_input(P):
    """Validate input to accept only digits between 1 and 9."""
    if len(P) == 0 or (P.isdigit() and 1 <= int(P) <= 9):
        return True
    return False

def fill_entries(board, entries):
    """Fill the Entry widgets with the values from the board and set their state."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            entries[row][col].delete(0, tk.END)
            if board[row][col] != EMPTY_CELL:
                entries[row][col].insert(0, str(board[row][col]))
                entries[row][col].config(state=tk.DISABLED, disabledbackground='lightgrey')
            else:
                entries[row][col].config(state=tk.NORMAL, disabledbackground='white')

def solve():
    """Handle the solve button press."""
    board = extract_board(entries)
    if solve_sudoku(board):
        fill_entries(board, entries)
        status_label.config(text="Puzzle solved!")
    else:
        status_label.config(text="No solution exists for the given Sudoku.")

def new_game():
    """Start a new game with a new Sudoku puzzle."""
    board = generate_puzzle()
    fill_entries(board, entries)
    status_label.config(text="New game started!")

def clear_board():
    """Clear all entries in the board."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            entries[row][col].delete(0, tk.END)
            entries[row][col].config(state=tk.NORMAL)
    status_label.config(text="Board cleared.")

# Create the main window
window = tk.Tk()
window.title("Sudoku Solver")
window.geometry("650x750")
window.configure(bg='lightgrey')

# Create a frame for the Sudoku grid
frame_grid = tk.Frame(window, bg='white')
frame_grid.pack(pady=20)

# Create a grid of Entry widgets with validation
entries = [[tk.Entry(frame_grid, width=3, font=('Arial', 18, 'bold'), justify='center', validate='key', validatecommand=(window.register(validate_input), '%P'), bd=2, relief='solid') for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for r in range(GRID_SIZE):
    for c in range(GRID_SIZE):
        entries[r][c].grid(row=r, column=c, padx=2, pady=2)

# Create a frame for the buttons
frame_buttons = tk.Frame(window, bg='lightgrey')
frame_buttons.pack(pady=10)

# Add buttons with colors and rounded corners
button_style = {'font': ('Arial', 14, 'bold'), 'width': 10}

solve_button = tk.Button(frame_buttons, text="Solve", command=solve, bg='lightblue', fg='black', **button_style)
solve_button.grid(row=0, column=0, padx=10)

new_game_button = tk.Button(frame_buttons, text="New Game", command=new_game, bg='lightgreen', fg='black', **button_style)
new_game_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(frame_buttons, text="Clear", command=clear_board, bg='lightcoral', fg='black', **button_style)
clear_button.grid(row=0, column=2, padx=10)

# Status label to show messages
status_label = tk.Label(window, text="", font=('Arial', 14), bg='lightgrey')
status_label.pack(pady=10)

# Start with a new game
new_game()

# Start the Tkinter event loop
window.mainloop()
