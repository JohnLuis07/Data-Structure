# CMSC 123 LAB 2 - Stacks
# Prepared by: John Roy Daradal

# Student 1: John Luis F. Magtoto - items under the class ArrayStack
# Student 2: Rainer T. Mayagma - items under the class SLLStack

from lab1 import Array, SLLNode
class ArrayStack:
	def __init__(self,capacity=10):
		self.array = Array(capacity)
		self.size = 0
	
	#returns a size of an empty array
	def is_empty(self):
		return self.size == 0

	#add an item to the top of the array stack
	def push(self,item):
		self.array.__setitem__(self.size, item)
		self.size+=1
		#expand the array if the array is already full
		if self.array[-1] != None:
			self.array.expand(2*(self.size))
    
	#remove and return the top item of the array stack
	def pop(self):
		if self.is_empty():
			raise Exception()		
		else:		
			return self.array.items.pop(-1)

	#returns the last items without removing it unlike the pop
	def top(self):
		if self.is_empty():
			raise Exception()
		else:
			return self.array.__getitem__(self.size-1)

class SLLStack:
	def __init__(self):
		self.top_node = None 
		self.size = 0

	#returns a size of an empty node
	def is_empty(self):
		return self.size == 0

	#add an item to the top of the SLL stack
	def push(self,item):
		if self.top_node == None:
			self.top_node = SLLNode(item)
			self.size+=1
		else:
			latest_node = SLLNode(item)
			latest_node.next = self.top_node
			self.top_node = latest_node
			self.size+=1
	#remove and return the top item of the SLL stack
	def pop(self):
		if self.is_empty():
			raise Exception()
		else:
			popped_node = self.top_node				
			self.top_node = self.top_node.get_next()	
			popped_node.set_next(None)					
			self.size-=1
			return popped_node.get_item()
	#return last inserted item in the SLL stack without removing it
	def top(self):
		if self.is_empty():
			raise Exception()
		else:
			return self.top_node.get_item()