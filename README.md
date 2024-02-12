# Maze solver

This Python program generate random maze and solve it with minimum steps

![Maze Solver](maze-solver.gif)

## Description

The program uses a 2D grid to represent a maze, where 1s represent walls and 0s represent paths. The BFS algorithm is used to find a path from the top-left corner to the bottom-right corner of the maze.

## Classes

- `Colors`: This class defines some constant colors used in the program. It also includes a method to generate a random color.
- `Settings`: This class inherits from `Colors` and defines some constant settings used in the program, such as screen size, grid size, and frames per second.
- `BFSVisualizer`: This class inherits from `Settings` and includes the main logic of the program. It initializes the Pygame environment, generates the maze, implements the BFS algorithm, handles user events, and updates the screen.

## Methods

- `draw_grids()`: Draws the grid on the screen.
- `generate_maze()`: Generates the maze based on the `maze` list.
- `BFS()`: Implements the BFS algorithm to find a path in the maze.
- `handle_events()`: Handles user events, such as closing the window.
- `update()`: Updates the screen and the state of the algorithm.
- `run()`: Runs the main loop of the program.

## Usage

To run the program, simply execute the script with a Python interpreter:

```bash
python main.py
```

## Requirements
- **python3.X**
- **pygame**

> :warning: **Ensure your array maze is squared (NxN)**
