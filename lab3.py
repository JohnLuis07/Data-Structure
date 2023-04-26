# CMSC 123 LAB 3 - Queues
# Prepared by: John Roy Daradal

# Student 1: John Luis F. Magtoto - items under the class ArrayQueue
# Student 2: Rainer T. Mayagma - items under the class SLLQueue

from lab1 import Array, SLLNode 

class ArrayQueue:
	def __init__(self,capacity=10):
		self.array = Array(capacity)
		self.size = 0

	def is_empty(self):
		return self.size == 0

	def enqueue(self,item):
     	#expands the array twice its capacity if the array is full
		if self.array[-1] != None:			
			self.array.expand(self.array.capacity*2)				#

		#appends the items in the array and update its size
		self.array.__setitem__(self.size, item)			        
		self.size += 1 									

	def dequeue(self):
		#declares the front as the 0 index of the array
		front_item = self.array[0]	
		#informs if the array is empty
		if self.is_empty():										
			raise Exception("Array is Empty")		

		for i in range(1, self.size):
			#removes the first item and move the items back to front
			self.array[i - 1] = self.array[i]
			#makes the last item as none
			if self.array[i] == self.array[self.size - 1]:
				self.array[i] = None  							
		#updates the size
		self.size -= 1
		return front_item

	#tells what item is the front 
	def front(self):
		#informs you if the array is empty
		if self.is_empty():				
			raise Exception("Array is Empty")			
		return self.array[0]								


 
class SLLQueue:
	def __init__(self):
		self.head_node = None
		self.tail_node = None
		self.size = 0

	def is_empty(self):
		return self.size == 0

	def enqueue(self,item):	
		new_node = SLLNode(item)
		if self.head_node == None:  # updates head,tail node, and size if it is the first node added
			self.head_node = new_node
			self.tail_node = self.head_node
			self.size += 1
	
		else:  # adds new node after tail node and its size
			self.tail_node.next = new_node
			self.tail_node = self.tail_node.get_next()
			self.size += 1
		
	def dequeue(self):		
				# gives the raise exception if queue is empty
		if self.is_empty():
			raise Exception('Empty queue: cannot dequeue')

		# assigning head node to variable (temp).Removing head node and its link
		temp = self.head_node
		self.head_node = self.head_node.get_next()
		temp.next = None
		self.size -= 1

		# resetting head and tail node
		if self.head_node == None:
			self.tail_node = None

		# returning the item of head node
		return temp.get_item()

	def front(self):
				# raise exception is queue has no front
		if self.is_empty():
			raise Exception('Empty queue: no front')

		# returning the item of head node
		return self.head_node.get_item()


