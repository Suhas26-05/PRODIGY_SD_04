# PRODIGY_SD_04 Sudoku Solver

This Python application provides an interactive Sudoku Solver with a graphical user interface (GUI) using the Tkinter library. The solver employs a backtracking algorithm to solve Sudoku puzzles and includes features for generating new puzzles and providing real-time feedback.

## Features

- **Solve Sudoku Puzzles**: Uses backtracking to find the solution to the given Sudoku puzzle.
- **Generate New Puzzles**: Start a new game with randomly generated puzzles.
- **Interactive GUI**: User-friendly interface to input and visualize the puzzle.
- **Clear and Reset**: Easily clear the board and reset the game state.

## Requirements

- Python 3.x
- Tkinter (Included with most Python installations)

## How to Run

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the script.
3. Navigate to the directory containing the script.
4. Run the script using the following command:
   ```bash
   python sudoku_solver.py
   ```
5. The Sudoku Solver window will open, allowing you to interact with the application.

## Usage

1. **Input the Puzzle**: Enter the initial values of the Sudoku puzzle into the grid.
2. **Click the "Solve" Button**: Find the solution to the puzzle and display it in the grid.
3. **Click the "New Game" Button**: Generate a new Sudoku puzzle and start a fresh game.
4. **Click the "Clear" Button**: Reset all entries and clear the board.

## Example

If you input a Sudoku puzzle into the grid and click "Solve," the application will use the backtracking algorithm to fill in the missing numbers and display the complete solution. When you click "New Game," the program will generate a new puzzle with some cells pre-filled.
