# CMSC 123 LAB 1 - Arrays and Linked Lists
# Prepared by: John Roy Daradal

# Student 1: John Luis F. Magtoto - items under the class array and sll node
# Student 2: Rainer T. Mayagma - items under the class dll node

class Array:
	def __init__(self,capacity):
		self.capacity = capacity 
		self.items = []
		for i in range(capacity):		# initialize array with None items
			self.items.append(None)

	def __getitem__(self,index):
		# Allows you to use syntax array[index]
		return self.items[index] 

	def __setitem__(self,index,item):
		# Allows you to use syntax array[index] = item
		self.items[index] = item

	def expand(self,new_capacity):
		#Creates a bigger array, with new_capacity, and transfer current items
		bigger_array = []
		self.capacity = new_capacity
		for i in range(self.capacity):
			bigger_array.append(None)
		for i in range(len(self.items)):
			bigger_array[i] = self.items[i]
		self.items = bigger_array

class SLLNode:
	def __init__(self,item=None,next_node=None):
		self.item = item 
		self.next = next_node

	# Getter and Setter Methods
	# Use self.item and self.next

	#allows the program to give the specific element in the node
	def get_item(self):
		return self.item

	#enables to manipulate or change the elements inside the node
	def set_item(self,item):
		self.item = item

	#points the next element in the node
	def get_next(self):
		return self.next	

	#manipulate or change the next element of the chosen one
	def set_next(self,next_node):
		self.next = next_node

class DLLNode:
	def __init__(self,item=None,prev_node=None,next_node=None):
		self.item = item 
		self.prev = prev_node
		self.next = next_node

	# Getter and Setter Methods
	# Use self.item, self.prev, and self.next

	#allows to gain access to the specific element inside the nodes
	def get_item(self):
		return self.item

	#enables to manipulate or change the elements inside the node
	def set_item(self,item):
		self.item = item

	#points the previous element in the node
	def get_prev(self):
		return self.prev

	#manipulate or change the previous element of the current element
	def set_prev(self,prev_node):
		self.prev = prev_node

	#points the next element in the node 
	def get_next(self):
		return self.next

	#manipulate or change the next element of the current element
	def set_next(self,next_node):
		self.next = next_node