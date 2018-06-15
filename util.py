class Stack:
	def __init__(self):
		self.items = []

	def push(self, element):
		self.items.append(element)

	def pop(self):
		return self.items.pop()

	def isEmpty(self):
		return len(self.items) == 0

class Queue:
	def __init__(self):
		self.items = []

	def push(self, element):
		self.items.append(element)

	def pop(self):
		return self.items.pop(0)

	def isEmpty(self):
		return len(self.items) == 0

class PriorityQueue(Queue):
	def __init__(self, func=lambda x: 1):
		super().__init__()
		self.priority = func

	# Do binary search on element priorities
	def __binary_search(self, items, target_priority, low, high):
		if low >= high:
			return low # not found, insert at low
		else:
			mid = int((low + high) / 2)
			mid_priority = self.priority(items[mid])
			if mid_priority == target_priority:
				return mid # insert at mid
			elif mid_priority < target_priority:
				return self.__binary_search(items, target_priority, mid, high) # search upper half
			else:
				return self.__binary_search(items, target_priority, low, high) # search lower half

	# Insert element into sorted list based on func result
	def push(self, element):
		insert_index = self.__binary_search(self.items, self.priority(element), 0, len(self.items)-1)
		self.items.insert(insert_index, element)

# pos1 and pos2 are (x, y, ...) tuples
def manhattanDistance(pos1, pos2):
	if len(pos1) != len(pos2):
		raise IndexError('Positions tuples do not have same length')
	result = 0
	for i in range(len(pos1)):
		result += abs(pos2[i] - pos1[i])

