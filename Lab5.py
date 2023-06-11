# Prepared by: Daundee L. Fernandez

# Student 1: John Luis Magtoto - items under the class arraydictionary
# Student 2: Rainer Mayagma - items under the class DLLmap
from lab1 import Array, DLLNode 

class MapEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def set_value(self, value):
		self.value = value

class DLLMap:
	def __init__(self):
		self.size = 0
		self.head_guard = DLLNode(None)
		self.tail_guard = DLLNode(None)
		self.head_guard.set_next(self.tail_guard)
		self.tail_guard.set_prev(self.head_guard)

	def find_node(self,key):
		node = self.head_guard.get_next()

		if node.get_item()==None:		# If Map is empty, it will return None...
			return None
		else:							# Else, it will traverse the Map and will return the Node if found,
			while node.get_item() != None:		#While the current Node is not empty...
				if node.get_item().get_key() == key:
					return node
				else:
					node = node.get_next()
			return None					# Else if, will return None.

	# If map entry with key, return associated value, otherwise return None.

	def get(self,key):
		node = self.find_node(key)		# Putting the found Node in a variable.
		if node == None:				# If Node not found, will return None.
			return None
		else:
			return node.get_item().get_value()	# else, will return the value of the associated key.

	# Insert entry with key and value into map.
	def put(self,key,value):
		node = self.find_node(key)		# Putting the found Node in a variable.
		entry = MapEntry(key, value)	# Putting new entry in a variable.

		if node == None:				# If node is None or a new entry.
			newNode = DLLNode(entry)	# assigning the new entry to a variable.
			newNode.set_prev(self.tail_guard.get_prev())	#Linking the nodes.
			newNode.set_next(self.tail_guard)
			self.tail_guard.get_prev().set_next(newNode)
			self.tail_guard.set_prev(newNode)
			return None					# If key is a new entry, will return None.
		else:							# Else if map has entry key already, return old value then overwrite it with new value.
			oldValue = node.get_item().get_value()
			node.get_item().set_value(value)
			return oldValue

	# Remove entry from the map.
	def remove(self,key):
		node = self.find_node(key);		# Putting the found Node in a variable.
		if node == None:				# If the Node the be removed is not found...
			return None					# ...it will return None.
		else:							# Else...
			delNode = node				# Putting the found node in a variable.
			delNode.get_prev().set_next(delNode.get_next())	# Linking the nodes.
			delNode.get_next().set_prev(delNode.get_prev())
			return delNode.get_item().get_value()				# Return the associated value of the key of an entry.

	# Iterator functions
	# Key - Iterator for map's keys.

	def keys(self,):
		node = self.head_guard.get_next()
		keys = []						# Keys will be stored inside a list.

		while node.get_item() != None:		# While the current node is not empty...
			keys.append(node.get_item().get_key())	# Append all keys inside the list.
			node = node.get_next()
		return keys						# Returns the list.

	# Values - Iterator for map's values.

	def values(self,):
		node = self.head_guard.get_next()
		values = []						# Values will be stored inside a list.

		while node.get_item() != None:		# While the current node is not empty...
			values.append(node.get_item().get_value())	# Append all values inside the list.
			node = node.get_next()
		return values					# Returns the values.

	# Entries - Iterator for map's entries.

	def entries(self,):
		node = self.head_guard.get_next()
		entries = []					# Entries will be stored inside a list.

		while node.get_item() != None:	# While the current node is not empty...
			entries.append((node.get_item().get_key(), node.get_item().get_value()))	# Append all the entries inside the list.
			node = node.get_next()
		return entries					# Returns the entries.

class Entry:
    #points the key
	def gkey(self):
		return self.key
	#points the value
	def gvalue(self):
		return self.value
	setattr(MapEntry, 'gkey', gkey)
	setattr(MapEntry, 'gvalue', gvalue)
        

class ArrayDictionary:
	def __init__(self, size):
		self.array = Array(size)
		self.size = size

	def insert(self,key,value):

		#doubles the capacity of the array
		if self.array.__getitem__(-2) != None:
			self.array.expand(self.size*2)
			self.size = self.size*2
   
		#no duplicate items
		dupli_item = 0

		for i in range(self.size):
			#normal insertion
			if self.array.__getitem__(i) == None:
				self.array.__setitem__(i, MapEntry(key, value))
				index = i
				break
			#detects duplicate
			else:
				dupli_item = 1
		#makes the duplicate items sit to each other side
		if dupli_item == 1:
			while(key != self.array.__getitem__(index-1).gkey()):
				if (index-1) == 0:
					break
				else:
					init = self.array.__getitem__(index-1)
					self.array.__setitem__(index-1, MapEntry(key, value))
					self.array.__setitem__(index, init)
					index-=1
		return MapEntry(key, value)

	def remove(self,entry):
		for i in range(self.size):
     		#stop when you reach none items
			if self.array.__getitem__(i) == None:
				break
			#removes the entry by locating their key and value
			elif(self.array.__getitem__(i).gkey() == entry.gkey()) and (self.array.__getitem__(i).gvalue() == entry.gvalue()):
				self.array.__setitem__(i, None)
				index = i
				break 

		while(index + 1 != self.size):
			#shifts all forward
			plus1 = self.array.__getitem__(index + 1)
			#shifting forward
			self.array.__setitem__(index + 1, self.array.__getitem__(index))
			#update loc
			self.array.__setitem__(index, plus1)

			index +=1


	def find(self,key):
		for i in range(self.size):
      		#stop when you reach none items
			if self.array.__getitem__(i) == None:
				break
			#get the first similar entry if it duplicates
			elif(self.array.__getitem__(i).gkey() == key):
				return self.array.__getitem__(i).gkey(), self.array.__getitem__(i).gvalue()

	def find_all(self,key):
		#initial 
		entries = []
		for i in range(self.size):
			#stop when you reach none items 
			if(self.array.__getitem__(i) == None):
				break
			#get all the duplicate entries
			elif(self.array.__getitem__(i).gkey() == key):
				entries.append((self.array.__getitem__(i).gkey(), self.array.__getitem__(i).gvalue()))


		return entries

	def entries(self):
		#initial array
		all_entries = []
		for i in range(self.size):
			#stop when you reach none items 
			if(self.array.__getitem__(i) == None):
				break
			#iterates all entries
			else:
				all_entries.append((self.array.__getitem__(i).gkey(), self.array.__getitem__(i).gvalue()))

		return all_entries