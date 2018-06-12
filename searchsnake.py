
from gamestate import GameState
from gamestate import PositionSearchProblem

if __name__ == '__main__':

	snakePos = [0, 0]
	foodPos = [3, 2]
	board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

	game = GameState(snakePos, foodPos, board)
	problem = PositionSearchProblem(game)

	print(game)
	print(problem.getStartState())

	startState = problem.getStartState()
	visited = set()
	fringe = [startState]

	while len(fringe) > 0:
		state = fringe.pop()
		print(state)
		visited.add(state)

		isGoal = problem.isGoalState(state)
		print("Goal: ", isGoal)
		if isGoal:
			break

		successors = problem.getSuccessors(state)
		for successor in successors:
			if successor not in visited:
				fringe.append(successor)

	print("DFS complete!")