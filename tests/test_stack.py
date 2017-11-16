__author__ = "Claire DeMars"

import unittest
import random
from stack import Stack


class TestStack(unittest.TestCase):
		
	def setUp( self, test_data=range(9) ):
		# called for every function that starts with test_
		self._test_data = test_data
		self._stack = Stack(len(self._test_data))
		for i in self._test_data:
			self._stack.push(i)
			
	def helper_check_stack_still_works(self, number_popped):
		num_left = len(self._test_data) - number_popped
		for i in range(num_left):
			look_here = -(i+number_popped+1)
			assert( self._stack.peek() == self._test_data[ look_here ] )
			assert( not self._stack.is_empty() )
			self._stack.pop()
		assert(self._stack.is_empty())
        
	def test_pop_one(self):
		self._stack.pop()
		self.helper_check_stack_still_works(1)
	
	def test_pop_some(self):
		num_to_pop = round( random.random()) *len( self._test_data)
		for i in range(num_to_pop):
			self._stack.pop()
		self.helper_check_stack_still_works(num_to_pop)
	
	def test_pop_all(self):
		num_to_pop = len( self._test_data)
		for i in range(num_to_pop):
			self._stack.pop()
		assert(self._stack.is_empty())
	
	def test_peek(self):
		num_left = len(self._test_data)
		for i in range(num_left):
			look_here = -(i+1)
			assert( self._stack.peek() == self._test_data[ look_here ] )
			self._stack.pop()
				
	def test_is_empty(self):
		len_test_data = len(self._test_data)
		for i in range( len_test_data ):
			assert(self._stack.is_empty() == False )
			self._stack.pop()
		assert(self._stack.is_empty() == True)
		
	def test_size(self):
		len_test_data = len(self._test_data)
		for i in range( len_test_data ):
			self._stack.pop()
			assert( self._stack.size() == len_test_data - i -1 )
		

if __name__ == "__main__":
	unittest.main()
