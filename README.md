Retro Snake Game
Overview

This project is a simple implementation of the classic Snake game using Pygame. The snake moves around the screen, eating food to grow longer. The goal is to eat as much food as possible without colliding with the walls or the snake's own tail.
Requirements

    Python 3.x
    Pygame library

Installation

    Clone the repository:

    bash

git clone https://github.com/TadekT/PythonSnakeProject.git

Install Pygame:

bash

pip install pygame

Run the game:

bash

    python main.py

How to Play

    Use the arrow keys to control the snake.
        Up: Move up
        Down: Move down
        Left: Move left
        Right: Move right
    Eat the food to grow longer.
    Avoid colliding with the walls and the snake's tail.
    Press any arrow key to restart the game after a game over.

Code Structure

    main.py: Contains the main game logic.
        Snake Class: Manages the snake's properties and behavior.
        Food Class: Manages the food's properties and behavior.
        Game Class: Manages the overall game logic, including updating the game state and checking for collisions.

Customization

    Game Settings: Modify cell_size, number_of_cells, and offsetBorder to change the grid size and game area.
    Appearance: Change SCREEN_COLOR and SNAKE_COLOR to customize the game's colors.
    Speed: Adjust the snake's speed by changing the timer interval for SNAKE_UPDATE.

Assets

    food_surface: Place the food image (Graph/FOODmy.png) in the Graph/ directory.

License

This project is open-source and available under the MIT License.
Acknowledgements

    Thanks to the Pygame community for their extensive documentation and support.

Feel free to fork this project, make improvements, and submit pull requests. Enjoy the game!
