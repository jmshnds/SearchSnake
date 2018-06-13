
from gamestate import GameState
from searchproblem import PositionSearchProblem
import search

if __name__ == '__main__':
	# Number of times snake will search for food
	number_of_searches = 5 

	# Set up game
	snakePos = (2, 0)
	foodPos = (3, 2)
	board = []
	board_size = 5
	for _ in range(board_size):
		board.append([0]*board_size)

	# Set up initial gamestate 
	game = GameState(snakePos, foodPos, board)

	# Repeat search n times
	for i in range(number_of_searches+1):
		problem = PositionSearchProblem(game)

		# Get resulting path nodes from performing a search
		path_nodes = search.breadthFirstSearch(problem)

		# Print path nodes
		for node in path_nodes:
			print(node)

		actions = [node.action for node in path_nodes]
		for action in actions[1:]:
			# Draw game board
			for row in game.board:
				print(row)

			# Move snake with chosen action
			game.frame_step(action)

			input("Press enter to continue...")

		# Draw game board one last time (to see win state)
		for row in game.board:
			print(row)

		print("%d food pellets eaten\n" % (i))

		# Move food to continue game with new search
		game.moveFood()
