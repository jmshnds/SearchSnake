
from direction import Direction
from snake import Snake
from food import Food
from colors import Color

class GameState:
	def __init__(self, snakePos, foodPos, board):
		self.score = 0
		self.player = Snake(snakePos[0], snakePos[1])
		self.player.grow(5)
		self.food = Food(foodPos[0], foodPos[1])

		# board is a 2D array of positions
		# 0 - empty, 1 - snake, 2 - food
		# [[0,0,0], [0,0,0], [0,0,0]]
		self.board = board

		# place snake and food on board
		for tailPiece in self.player.tail:
			self.board[tailPiece.x][tailPiece.y] = 1

		self.board[self.food.x][self.food.y] = 2

	def frame_step(self, input_actions):
		# input_actions[0] == 1: do nothing
		# input_actions[1] == 1: change direction NORTH
		# input_actions[2] == 1: change direction EAST
		# input_actions[3] == 1: change direction SOUTH
		# input_actions[4] == 1: change direction WEST
		if input_actions[1]:
			self.player.changeDirection(Direction.NORTH)
		elif input_actions[2]:
			self.player.changeDirection(Direction.EAST)
		elif input_actions[3]:
			self.player.changeDirection(Direction.SOUTH)
		elif input_actions[4]:
			self.player.changeDirection(Direction.WEST)

		if self.player.hasEaten(self.food):
			self.score += 1
			# move food
			self.food.x = randint(0, BLOCK_W-1)
			self.food.y = randint(0, BLOCK_H-1)

		self.player.move()

	def getSnakePosition(self):
		return (self.player.x, self.player.y)

	def getFoodPosition(self):
		return (self.food.x, self.food.y)

	def getBoard(self):
		return self.board

class SearchProblem():
	def getStartState(self):
		pass

	def isGoalState(self, state):
		pass

	def getSucessors(self, state):
		pass

	def getCostOfActions(self, actions):
		pass

class PositionSearchProblem(SearchProblem):
	def __init__(self, gameState, costFn = lambda x: 1):
		self.startState = gameState.getSnakePosition()
		self.goalState = gameState.getFoodPosition()
		self.board = gameState.getBoard()
		self.tail = gameState.player.tail
		self.costFn = costFn

	def getStartState(self):
		return self.startState

	def isGoalState(self, state):
		return state == self.goalState

	def getSuccessors(self, state):
		successors = []
		actions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
		for action in actions:
			x, y = state
			if action == Direction.NORTH:
				dx = 0
				dy = -1
			elif action == Direction.EAST:
				dx = 1
				dy = 0
			elif action == Direction.SOUTH:
				dx = 0
				dy = 1
			else:
				dx = -1
				dy = 0

			nextx, nexty = x+dx, y+dy

			# Check if snake crashed into tail
			'''
			for i in range(1, len(self.player.tail)):
			    if self.player.x == self.player.tail[i].x and self.player.y == self.player.tail[i].y:
			    	print("crashed into tail")
			'''
			hitsTail = False
			for tailPiece in self.tail:
				if nextx == tailPiece.x and nexty == tailPiece.y:
					hitsTail = True
					break
			if hitsTail:
				continue

			# Check if the snake has moved off screen
			if nextx < 0 or nextx >= len(self.board) or nexty < 0 or nexty >= len(self.board):
				continue

			cost = self.costFn((nextx, nexty))
			successors.append(((nextx, nexty), action, cost))

		return successors
