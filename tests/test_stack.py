__author__ = "Claire DeMars"

import unittest
import random
from parameterized import parameterized
import sys
import os

sys.path.append(os.path.abspath('../data_structures/Stacks'))
from stack import Stack


# run with these params: increasing order, random ordered, >100 items
class TestStack(unittest.TestCase):
		

	def setUp(self):
		random.seed()
		
	def helper_fill_stack( self, test_data):
		self._stack = Stack(len(test_data))
		for i in test_data:
			self._stack.push(i)
						

	@parameterized.expand([
		([i for i in range(15)], ),
		([i for i in reversed(range(20))], ),
		( [random.random() for i in range(100) ], ),
	])		
	def test__pop__ItemsInStack__ItemsInsertedAndPoppedInCorrectOrder(self, test_data):
		self.helper_fill_stack(test_data)
		for i in reversed(test_data):
			self.assertEqual( 2, self._stack.pop() )
	
	
	@parameterized.expand([
		([i for i in range(15)], ),
	])		
	def test__is_empty_and_pop(self, test_data):
		self.helper_fill_stack(test_data)
		for i in range(len(test_data) ):
			self.assertFalse( self._stack.is_empty() )
			self._stack.pop()
		self.assertTrue( self._stack.is_empty() )
			
	@parameterized.expand([
		([i for i in range(15)], ),
		([i for i in reversed(range(20))], ),
		( [random.random() for i in range(100) ], )
	])				
	def test__peek__TopElement__IsDisplayed(self, test_data):
		self.helper_fill_stack(test_data)
		self.assertEqual( self._stack.peek(), test_data[-1])
		
	@parameterized.expand([
		([i for i in range(15)], ),
		([i for i in reversed(range(20))], ),
		( [random.random() for i in range(100) ], )
	])			
	def test__peek_and_pop(self, test_data):
		self.helper_fill_stack(test_data)
		for i in reversed(test_data ) :
			self.assertEqual( i, self._stack.peek() )
			self._stack.pop()	
	
	@parameterized.expand([
		([i for i in range(15)], ),
		([i for i in reversed(range(20))], ),
		( [random.random() for i in range(100) ], )
	])			
	def test__size__FullStack__SizeIsCorrect(self, test_data):
		self.helper_fill_stack(test_data)
		self.assertEqual (self._stack.size(), len(test_data) )
		
	@parameterized.expand([
		([i for i in range(15)], ),
		([i for i in reversed(range(20))], ),
		( [random.random() for i in range(100) ], )
	])			
	def test__size_and_pop(self, test_data):
		self.helper_fill_stack(test_data)
		counter = self._stack.size()
		for i in range(counter):
			self.assertEqual (self._stack.size(), counter)
			self._stack.pop()
			counter -= 1
			
			
	
if __name__ == "__main__":
	unittest.main()