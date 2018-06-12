from util import Stack
from util import Queue

class Node:
	def __init__(self, state, parent=None, action=None, path_cost=0):
		self.state = state
		self.parent = parent
		self.action = action
		if parent:
			self.path_cost = parent.path_cost + path_cost
			self.depth = parent.depth + 1
		else:
			self.path_cost = path_cost
			self.depth = 0

	def __repr__(self):
		return "<Node %s, %s>" % (self.state, self.action,)

	def nodePath(self):
		x, result = self, [self]
		while x.parent:
			result.append(x.parent)
			x = x.parent
		result = result[::-1]
		return result

	def expand(self, problem):
		return [Node(next, self, act, cost) for (next, act, cost) in problem.getSuccessors(self.state)]

def graphSearch(problem, fringe):
	startState = problem.getStartState()
	fringe.push(Node(startState))
	visited = set()

	while not fringe.isEmpty():
		node = fringe.pop()
		if problem.isGoalState(node.state):
			return node.nodePath()
		if not node.state in visited:
			visited.add(node.state)
			nextNodes = node.expand(problem)

			for nextNode in nextNodes:
				fringe.push(nextNode)

def depthFirstSearch(problem):
	return graphSearch(problem, Stack())

def breadthFirstSearch(problem):
	return graphSearch(problem, Queue())
