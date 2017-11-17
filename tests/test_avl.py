
__author__ = "Claire DeMars"

import unittest
from parameterized import parameterized
import sys
import os
import random
sys.path.append(os.path.abspath('../data_structures/AVL'))
from AVL import AVL
import capture_output

class TestAvl(unittest.TestCase):

	@parameterized.expand([
			([i for i in range(15)], ),
			([i for i in reversed(range(20))], ),
			( [random.random() for i in range(100) ], )
	])		
	def test__insert_and_preShow__AvlTree__ThingsGetInsertedCorrectlyAndComeOutInSortedOrder(self, input):
		tree = AVL()
		for i in input:
			tree.insert(i)
		expected_result = ""
		for i in sorted(input):
			expected_result+=str(i)
			
		with capture_output.capture_output() as (out, err):
			tree.preShow(tree.root)
			self.assertEqual(out.getValue().strip(),  expected_result)
	


if __name__ == "__main__":
	unittest.main()