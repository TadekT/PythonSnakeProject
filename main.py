# @Autor : Tadeusz Toporkiewicz 
# 29. Stwórz prostą grę wężyk w Pythonie z użyciem biblioteki Pygame. Gra powinna polegać
# na ruchu węża, zbieraniu punktów i unikaniu przeszkód. Wykorzystaj moduły do organizacji
# kodu, obsługę błędów i wyjątków oraz generatory. Dodatkowo, zaimplementuj prostą
# sztuczną inteligencję w grze, korzystając z frameworka Keras do nauki maszynowej.
import random
import pygame
import sys
from pygame.math import Vector2
pygame.init()
# Setting up fonts
gameTitleFont = pygame.font.Font(None,60)
gameScoreFont = pygame.font.Font(None,60)

# Setting up colors
SCREEN_COLOR = (173,200,100)
SNAKE_COLOR = (30,70,10)

# Setting up cell size and grid dimensions
cell_size = 30
number_of_cells = 25

# Offset for border
offsetBorder = 75

# Snake class to manage snake properties and behavior
class Snake:
    def __init__(self):
        self.snakeBody = [Vector2(6,9),Vector2(5,9),Vector2(4,9)]
        self.direction = Vector2(1, 0)
        self.addSegment = False
        
    # Drawing the snake    
    def drawSnake(self):
        for segment in self.snakeBody:
            segment_rect = (offsetBorder + segment.x * cell_size,offsetBorder + segment.y * cell_size, cell_size , cell_size)
            pygame.draw.rect(screen,SNAKE_COLOR,segment_rect,19,7)
            
    # Updating the snake's position
    def update(self):
        self.snakeBody.insert(0,self.snakeBody[0] + self.direction)
        if self.addSegment == True:
            self.addSegment = False
        else:
            self.snakeBody = self.snakeBody[:-1]
            
   # Resetting the snake to the initial position
    def reset(self):
        self.snakeBody = [Vector2(6,9),Vector2(5,9),Vector2(4,9)]
        self.direction = Vector2(1,0)
            
# Food class to manage food properties and behavior     
class Food:
    def __init__(self, Body):
        self.position = self.generateRandomPosition(Body)
     
    # Drawing the food   
    def drawFood(self):
        food_rect = pygame.Rect(offsetBorder + self.position.x * cell_size, offsetBorder + self.position.y*cell_size,cell_size,cell_size)
        screen.blit(food_surface,food_rect)
    
   # Generating a random cell on the grid
    def generateRandomCell(self):
        x = random.randint(0,number_of_cells - 1)
        y = random.randint(0,number_of_cells - 1)
        return Vector2(x,y)
        
   # Generating a random position that is not occupied by the snake 
    def generateRandomPosition(self, body):
        posit = self.generateRandomCell()
        while posit in body:
            posit = self.generateRandomCell()
        return posit

# Game class to manage overall game logic 
class Game:
    def __init__(self):
        self.snake_ = Snake()
        self.food_ = Food(self.snake_.snakeBody)
        self.state_ = "RUNGAME"
        self.gameScore_ = 0
    
    # Drawing the game components   
    def drawGame(self):
        self.snake_.drawSnake()
        self.food_.drawFood() 
    
    # Updating the game state
    def update(self):
        if self.state_ == "RUNGAME":
            self.snake_.update()
            self.checkFoodCollision()
            self.checkWallCollision()
            self.checkCollisionWithTail()
    
     # Checking if the snake has collided with food        
    def checkFoodCollision(self):
        if self.snake_.snakeBody[0] == self.food_.position:
            self.food_.position = self.food_.generateRandomPosition(self.snake_.snakeBody)
            self.snake_.addSegment = True
            self.gameScore_ += 1
            
    # Handling game over situation
    def gameOver(self):
        self.snake_.reset()
        self.food_.position = self.food_.generateRandomPosition(self.snake_.snakeBody)
        self.state_ = "STOPGAME"
        self.gameScore_ = 0
        
    # Checking if the snake has collided with the wall
    def checkWallCollision(self):
        if self.snake_.snakeBody[0].x == number_of_cells or self.snake_.snakeBody[0].x == -1:
            self.gameOver()
        if self.snake_.snakeBody[0].y == number_of_cells or self.snake_.snakeBody[0].y == -1:
            self.gameOver()
    
    # Checking if the snake has collided with its own tail
    def checkCollisionWithTail(self):
        tail = self.snake_.snakeBody[1:] # snake body without head 
        if self.snake_.snakeBody[0] in tail: # Is snake head touch a tail?
            self.gameOver() # YEP HEAD TOUCH A TAIL!!!!! 

        
# Setting up the game screen
screen = pygame.display.set_mode((2*offsetBorder + cell_size * number_of_cells, 2*offsetBorder + cell_size * number_of_cells))
pygame.display.set_caption("Retro Snake")
clock = pygame.time.Clock()

# Creating game instance and loading food surface
game_ = Game()
food_surface = pygame.image.load("Graph/FOODmy.png")

# Setting up custom event for snake update
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE,180)

# Main game loop    
while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game_.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_.state_ == "STOPGAME":
                game_.state_ = "RUNGAME"
            if event.key == pygame.K_UP and game_.snake_.direction != Vector2(0,1):
                game_.snake_.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game_.snake_.direction != Vector2(0,-1):
                game_.snake_.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and game_.snake_.direction != Vector2(1,0):
                game_.snake_.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game_.snake_.direction != Vector2(-1,0):
                game_.snake_.direction = Vector2(1, 0)
                
                
    # Drawing the game screen
    screen.fill(SCREEN_COLOR)
    pygame.draw.rect(screen,SNAKE_COLOR,(offsetBorder-5,offsetBorder-5,cell_size*number_of_cells+10,cell_size*number_of_cells+10),5) 
    game_.drawGame()
    titleSurface = gameTitleFont.render("Simple Snake",True,SNAKE_COLOR)
    gameScoreSurface = gameScoreFont.render(f"Score : {str(game_.gameScore_)}",True,SNAKE_COLOR)
    screen.blit(titleSurface,(300, 850))
    screen.blit(gameScoreSurface,(offsetBorder-5, 20))
    pygame.display.update()
    clock.tick(60)
    
