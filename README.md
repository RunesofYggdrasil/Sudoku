# Sudoku Puzzle Game

This is a Python-based implementation of a Sudoku puzzle game that allows users to load different Sudoku boards from a file, interact with the puzzle, set values, and track changes using undo and redo functionality.

## Table of Contents
1. [Project Description](#project-description)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Code Structure](#code-structure)
6. [Contributors](#contributors)
7. [License](#license)

## Project Description

This project is a console-based Sudoku game in Python that:
- Loads Sudoku puzzles from a text file.
- Allows setting values on the Sudoku grid.
- Tracks changes, allowing the user to undo or redo their actions.
- Provides a simple gameplay interface to interact with the puzzle.

The game is implemented with Python's standard libraries, and the `Sudoku` class is designed to manage the board and handle user input for interacting with the puzzle.

## Features

- **Load Puzzle**: Read a Sudoku puzzle from a file and load it onto the game board.
- **Set Value**: Set a number at a specific row and column.
- **Undo/Redo**: Track changes and allow the user to undo or redo previous actions.
- **Text File Input**: Load boards from a structured text file (`sudokuboards.txt`).
- **Basic Gameplay**: Includes methods for setting values, checking for changes, and applying undo/redo actions.

## Installation

### Requirements

- Python 3.x
- Basic text editor or IDE

### Steps

1. Clone this repository:

   git clone https://github.com/RunesofYggdrasil/Sudoku.git
