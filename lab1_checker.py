import unittest
from Lab_1_starter_code import Array, SLLNode, DLLNode

class TestLab2(unittest.TestCase):

	def setUp(self):
		#setup for array tests
		
		self.arr = Array(10)
		for x in range(10):
			self.arr[x] = x

		#setup for SLLNode Tests

		self.n1 = SLLNode("E", None)
		self.n2 = SLLNode("D", self.n1)
		self.n3 = SLLNode("C", self.n2)
		self.n4 = SLLNode("B", self.n3)
		self.n5 = SLLNode("A", self.n4)

		#setup for DLLNode Tests

		self.nd1 = DLLNode("E", None, None)
		self.nd2 = DLLNode("D", None, self.nd1)
		self.nd3 = DLLNode("C", None, self.nd2)
		self.nd4 = DLLNode("B", None, self.nd3)
		self.nd5 = DLLNode("A", None, self.nd4)

		self.nd1.set_prev(self.nd2)
		self.nd2.set_prev(self.nd3)
		self.nd3.set_prev(self.nd4)
		self.nd4.set_prev(self.nd5)
		self.nd5.set_prev(None)

	# Array Tests
	def test_GetItem(self):
		for x in range(10):
			result = self.arr.__getitem__(x)
			self.assertEqual(result, x)

		self.assertRaises(IndexError, self.arr.__getitem__, self.arr.capacity)
		self.assertRaises(IndexError, self.arr.__getitem__, -abs(self.arr.capacity+1))

	def test_SetItem(self):
		self.arr.__setitem__(3, None)
		result = self.arr.__getitem__(3)
		self.assertEqual(result, None)

		self.assertRaises(IndexError, self.arr.__setitem__, 10, None)
		self.assertRaises(IndexError, self.arr.__setitem__, -11, None)

	def test_expand(self):
		prev_cap = self.arr.capacity
		self.arr.expand(20)
		result = self.arr.capacity
		self.assertEqual(result, 20)

		for x in range(prev_cap):
			self.assertEqual(self.arr[x], x)
		for x in range(prev_cap,result):
			self.assertEqual(self.arr[x], None)

		self.assertRaises(Exception, self.arr.expand, 19)

	# End of Array tests

	# SLLNode tests
	def test_SLL_get(self):
		nodes = ["A","B","C","D","E"]
		index = 0
		current = self.n5
		next_ = current.get_next()

		while(True):
			self.assertEqual(current.get_item(), nodes[index])
			next_ = current.get_next()
			index += 1
			if index == 5:
				break;
			self.assertEqual(current.get_next().get_item(), nodes[index])
			current = next_

	def test_SLL_set_item(self):
		nodes = ["E","C","D","B","A"]
		index = 0

		self.n5.set_item("E")
		self.n4.set_item("C")
		self.n3.set_item("D")
		self.n2.set_item("B")
		self.n1.set_item("A")

		current = self.n5
		next_ = current.get_next()

		while(True):
			self.assertEqual(current.get_item(), nodes[index])
			next_ = current.get_next()
			index += 1
			if index == 5:
				break
			self.assertEqual(current.get_next().get_item(), nodes[index])
			current = next_

	def test_SLL_set_next(self):
		nodes = ["E","C","D","B","A"]
		index = 0

		self.n5.set_next(None)
		self.n4.set_next(self.n5)
		self.n3.set_next(self.n2)
		self.n2.set_next(self.n4)
		self.n1.set_next(self.n3)


		current = self.n1
		next_ = current.get_next()

		while(True):
			self.assertEqual(current.get_item(), nodes[index])
			next_ = current.get_next()
			index += 1
			if index == 5:
				break
			self.assertEqual(current.get_next().get_item(), nodes[index])
			current = next_
		
	# end of SLLNode tests

	# DLLNode tests
	def test_DLL_get(self):
		nodes = ["A","B","C","D","E"]
		index = 0

		# get_next test
		current = self.nd5
		next_ = current.get_next()

		while(True):
			self.assertEqual(current.get_item(), nodes[index])
			next_ = current.get_next()
			index += 1
			if index == 5:
				break
			self.assertEqual(current.get_next().get_item(), nodes[index])
			current = next_

		# get_prev test
		index = 4
		current = self.nd1
		prev_ = current.get_prev()

		while(True):
			self.assertEqual(current.get_item(), nodes[index])
			prev_ = current.get_prev()
			index -= 1
			if index == -1:
				break
			self.assertEqual(current.get_prev().get_item(), nodes[index])
			current = prev_

	def test_DLL_set_item(self):
		nodes = ["E","C","D","B","A"]
		index = 0

		self.nd5.set_item("E")
		self.nd4.set_item("C")
		self.nd3.set_item("D")
		self.nd2.set_item("B")
		self.nd1.set_item("A")

		current = self.nd5
		next_ = current.get_next()

		while(True):
			self.assertEqual(current.get_item(), nodes[index])
			next_ = current.get_next()
			index += 1
			if index == 5:
				break
			self.assertEqual(current.get_next().get_item(), nodes[index])
			current = next_

	def test_DLL_set_prev_next(self):
		nodes = ["E","C","D","B","A"]
		index = 0

		self.nd5.set_next(None)
		self.nd4.set_next(self.nd5)
		self.nd3.set_next(self.nd2)
		self.nd2.set_next(self.nd4)
		self.nd1.set_next(self.nd3)

		self.nd5.set_prev(self.nd4)
		self.nd4.set_prev(self.nd2)
		self.nd3.set_prev(self.nd1)
		self.nd2.set_prev(self.nd3)
		self.nd1.set_prev(None)


		current = self.nd1
		next_ = current.get_next()

		while(True):
			self.assertEqual(current.get_item(), nodes[index])
			next_ = current.get_next()
			index += 1
			if index == 5:
				break
			self.assertEqual(current.get_next().get_item(), nodes[index])
			current = next_

		# get_prev test
		index = 4
		current = self.nd5
		prev_ = current.get_prev()

		while(True):
			self.assertEqual(current.get_item(), nodes[index])
			prev_ = current.get_prev()
			index -= 1
			if index == -1:
				break
			self.assertEqual(current.get_prev().get_item(), nodes[index])
			current = prev_

if __name__ == '__main__':
	unittest.main()