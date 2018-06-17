
from colors import Color
from gamestate import GameState
from searchproblem import PositionSearchProblem
from util import manhattanDistance
import pygame
import search
import sys

BOARD_SIZE = 25
NUMBER_OF_SEARCHES = 10 # Number of times snake will search for food
BLOCK_S = 10

pygame.init()
clock = pygame.time.Clock()
draw = pygame.draw
screen = pygame.display.set_mode((BOARD_SIZE*BLOCK_S, BOARD_SIZE*BLOCK_S))
pygame.display.set_caption("Search Snake")

def process_args():
	options = {'searchFunc': search.depthFirstSearch,
				'supplementFunc': False}
	for arg in sys.argv[1:]:
		if arg == 'dfs':
			options['searchFunc'] = search.depthFirstSearch
		elif arg == 'bfs':
			options['searchFunc'] = search.breadthFirstSearch
		elif arg == 'greedy':
			options['searchFunc'] = search.greedySearch
			options['supplementFunc'] = True
	return options

if __name__ == '__main__':
	options = process_args() # Get search type

	# Set up game
	snakePos = (2, 0)
	foodPos = (3, 2)
	board = []
	for _ in range(BOARD_SIZE):
		board.append([0]*BOARD_SIZE)

	# Set up initial gamestate 
	game = GameState(snakePos, foodPos, board)

	suppFunc = lambda node: manhattanDistance(node.state, (game.food.x, game.food.y))

	# Repeat search n times
	for search_num in range(NUMBER_OF_SEARCHES):
		# Set up search problem
		problem = PositionSearchProblem(game)

		# Get resulting path nodes from performing a search
		#path_nodes = search.greedySearch(problem, lambda node: manhattanDistance(node.state, (game.food.x, game.food.y)))
		if not options['supplementFunc']:
			path_nodes = options['searchFunc'](problem)
		else:
			path_nodes = options['searchFunc'](problem, suppFunc)

		# Print path nodes
		'''
		for node in path_nodes:
			print(node)
		'''
		
		# Check if a path was found
		if path_nodes is None:
			print("Could not find path")
			pygame.quit()
			exit()

		actions = [node.action for node in path_nodes]

		for action in actions:
			# Make call to pygame event and check if windows is closed
			if pygame.QUIT in [event.type for event in pygame.event.get()]:
				pygame.quit()
				exit()

			# Draw game board
			screen.fill(Color.WHITE)
			for tailPiece in game.player.tail:
				draw.rect(screen, Color.RED, (BLOCK_S*tailPiece.x, BLOCK_S*tailPiece.y, BLOCK_S, BLOCK_S))
			draw.rect(screen, Color.GREEN, (BLOCK_S*game.food.x, BLOCK_S*game.food.y, BLOCK_S, BLOCK_S))
			pygame.display.update()
			clock.tick(12)

			# Move snake with chosen action
			if action is not None:
				game.frame_step(action)

		# Draw game board one last time
		screen.fill(Color.WHITE)
		for tailPiece in game.player.tail:
			draw.rect(screen, Color.RED, (BLOCK_S*tailPiece.x, BLOCK_S*tailPiece.y, BLOCK_S, BLOCK_S))
		draw.rect(screen, Color.GREEN, (BLOCK_S*game.food.x, BLOCK_S*game.food.y, BLOCK_S, BLOCK_S))
		pygame.display.update()
		clock.tick(12)

		print("%d food pellets eaten" % (search_num+1))

		# Move food to continue game with new search
		game.moveFood()

	pygame.quit()
	exit()
