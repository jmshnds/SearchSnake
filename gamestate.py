
from random import randint
from direction import Direction
from snake import Snake
from food import Food
from colors import Color

class GameState:
	def __init__(self, snakePos, foodPos, board):
		self.score = 0
		self.player = Snake(snakePos[0], snakePos[1])
		self.player.grow(1)
		self.food = Food(foodPos[0], foodPos[1])

		# board is a 2D array of positions
		# 0 - empty, 1 - snake, 2 - food
		# [[0,0,0], [0,0,0], [0,0,0]]
		self.board = board

		# place snake and food on board
		for tailPiece in self.player.tail:
			self.board[tailPiece.y][tailPiece.x] = 1

		self.board[self.food.y][self.food.x] = 2

	def frame_step(self, input_actions):
		self.player.changeDirection(input_actions)

		self.player.move()

		if self.player.hasEaten(self.food):
			self.score += 1
			self.player.grow(2)
		
		# Update game board (Note: x and y coordinates are flipped)
		tailPos = [(tailPiece.x, tailPiece.y) for tailPiece in self.player.tail]
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				if (i, j) in tailPos:
					self.board[j][i] = 1
				elif (i, j) == (self.food.x, self.food.y):
					self.board[j][i] = 2
				else:
					self.board[j][i] = 0

	def getSnakePosition(self):
		return (self.player.x, self.player.y)

	def getFoodPosition(self):
		return (self.food.x, self.food.y)

	def getBoard(self):
		return self.board

	def moveFood(self):
		# Place food at random location that is not occupied
		while self.food.x == self.player.x or self.food.y == self.player.y:
			self.food.x = randint(0, len(self.board)-1)
			self.food.y = randint(0, len(self.board)-1)

		self.board[self.food.y][self.food.x] = 2
