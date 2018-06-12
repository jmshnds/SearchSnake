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