
from gamestate import GameState
from searchproblem import PositionSearchProblem
import search

if __name__ == '__main__':
	# Set up game
	snakePos = (2, 0)
	foodPos = (3, 2)
	board = []
	n = 5
	for _ in range(n):
		board.append([0]*n)
	print(board)

	# Set up gamestate and search problem
	game = GameState(snakePos, foodPos, board)
	problem = PositionSearchProblem(game)

	# Get resulting path nodes from performing a search
	nodes = search.breadthFirstSearch(problem)
	for node in nodes:
		print(node)

	actions = [node.action for node in nodes]
	for action in actions[1:]:
		# Draw game board
		for row in game.board:
			print(row)

		# Move snake with chosen action
		game.frame_step(action)

		input("Press enter to continue...")

	# Draw game board one last time
	for row in game.board:
		print(row)
