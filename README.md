# Tic-Tac-Toe Game

Welcome to the **Tic-Tac-Toe Game**! A fun and interactive implementation of the classic Tic-Tac-Toe game with enhanced features and varying difficulty levels. Whether you're playing against a friend or challenging the computer, this game offers an engaging experience for all skill levels.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Running the Game](#running-the-game)
- [Game Modes](#game-modes)
- [User Interface](#user-interface)
- [Difficulty Levels](#difficulty-levels)
- [Technical Overview](#technical-overview)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features
- **Graphical User Interface (GUI):** Built with Tkinter for a seamless user experience.
- **Multiple Game Modes:**
  - Player vs. Player
  - Player vs. Computer
- **Three Difficulty Levels:** Easy, Normal, and Hard, each with unique strategies.
- **Customizable Board Size:** Choose the size of the playing board to vary the challenge.
- **Dynamic Victory Conditions:** Victory conditions adjust based on the board size.
- **Theme Switching:** Toggle between light and dark modes to suit your preference.
- **Responsive Design:** Optimized for different screen sizes and resolutions.

## Installation

Ensure you have Python installed on your system. Then, follow these steps to set up the game:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Nazar050802/Tic-tac-toe-game.git
    ```
2. **Navigate to the Game Directory:**
    ```bash
    cd tic-tac-toe-game/Game/
    ```
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Game

To start the game, ensure you're in the `Game/` directory and run the `main.py` script:

```bash
cd Game/
python main.py
```

> **Note:** Only run `main.py` from its directory to ensure all resources are correctly loaded.

## Game Modes

Choose between two exciting modes:

1. **Player vs. Player:** Challenge a friend in a classic Tic-Tac-Toe match.
2. **Player vs. Computer:** Test your skills against the computer with varying difficulty levels.

## User Interface

The game features a clean and intuitive GUI developed using the Tkinter library. Key aspects include:

- **Theme Customization:** Switch between light and dark themes for comfortable gameplay.
- **Main Menu:** Access settings, view author information, and start the game.
- **Settings:** Adjust game parameters such as board size, number of players, and computer difficulty.
- **Gameplay Area:** Interactive board that adapts to your chosen settings.

![Game Screenshot](https://github.com/Nazar050802/Tic-tac-toe-game/blob/main/Documentation/pictures/gui_structure.jpg)

## Difficulty Levels

Enhance your gameplay experience with three distinct difficulty levels:

### Easy
- **Behavior:** Computer makes random moves.
- **Strategy:** Minimal, perfect for beginners.

### Normal
- **Behavior:** Computer uses basic strategies.
- **Strategy:**
  1. Win if possible.
  2. Block opponent's winning move.
  3. Make a random move otherwise.

### Hard
- **Behavior:** Computer employs advanced tactics.
- **Strategy:**
  1. Win if possible.
  2. Block opponent's winning move.
  3. Prevent opponent's strategic setups on larger boards.
  4. Prioritize center positions.
  5. Block multiple winning threats.
  6. Make moves near previous computer moves.
  7. Make a random move otherwise.

## Technical Overview

### Architecture
The game is structured into three main components:

- **Kernel:** Manages game logic, processes the playing field, and interacts with configuration files.
- **Controller:** Facilitates communication between the GUI and the kernel, handling data conversion and requests.
- **GUI:** Renders menus and interfaces for user interaction using Tkinter.

![Architecture Diagram](https://github.com/Nazar050802/Tic-tac-toe-game/blob/main/Documentation/pictures/classes_dependencies%20.jpg)

### Dependencies
- Python 3.x
- Tkinter
- [Additional dependencies listed in `requirements.txt`](#installation)

## Contributing

Contributions are welcome! Whether you're reporting bugs, suggesting features, or submitting pull requests, your input helps improve the game.

1. **Fork the Repository**
2. **Create a Feature Branch**
    ```bash
    git checkout -b feature/YourFeature
    ```
3. **Commit Your Changes**
    ```bash
    git commit -m "Add Your Feature"
    ```
4. **Push to the Branch**
    ```bash
    git push origin feature/YourFeature
    ```
5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- **Charles University Faculty of Mathematics and Physics**
- **Programming 1 [NPRG030] Course**
- **Author:** Mozharov Nazar, Prague 2022

---

Feel free to reach out or open an issue if you encounter any problems or have suggestions for improvement!

---
