from direction import Direction

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
				dx, dy = 0, -1
			elif action == Direction.EAST:
				dx, dy = 1, 0
			elif action == Direction.SOUTH:
				dx, dy = 0, 1
			else:
				dx, dy = -1, 0

			nextx, nexty = x+dx, y+dy

			# Check if snake crashed into tail
			hitsTail = False
			for tailPiece in self.tail:
				if nextx == tailPiece.x and nexty == tailPiece.y:
					hitsTail = True
					break
			if hitsTail:
				continue # Do not add this successor state

			# Check if the snake has moved off screen
			if nextx < 0 or nextx >= len(self.board) or nexty < 0 or nexty >= len(self.board):
				continue # Do not add this successor state

			cost = self.costFn((nextx, nexty))
			successors.append(((nextx, nexty), action, cost))

		return successors
