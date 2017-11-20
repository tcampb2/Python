__author__ = "Claire DeMars"

import sys
import os
import unittest
import random
import timeout_decorator
from parameterized import parameterized

import capture_output
sys.path.append(os.path.abspath('..'))


class TestSorts(unittest.TestCase):
	
	@parameterized.expand([
		# ("bogosort", ), # hangs
		("bubble_sort", ),
		# ("bucket_sort", "bucket_sort"), # requires non-present dependencies 
		("cocktail_shaker_sort", ),
		("counting_sort", ),
		("cyclesort", "cycle_sort"),
		("gnome_sort", ),
		("heap_sort", ),
		("insertion_sort", ),
		("merge_sort", ),
		("quick_sort", ),
		("radix_sort", "radixsort" ),
		("selection_sort", ),
		("shell_sort", ),
		("timsort", ),
	])
	# @timeout_decorator.timeout(5) # does not work on windows
	def test__mostSorts__workForIntLists(self, sort_file_name, sort_name=""):
		if not sort_name:
			sort_name = sort_file_name
		module = __import__("sorts."+sort_file_name, fromlist=[""])
		function = getattr(module, sort_name)
		
		ints_reverse_ordered = list( reversed( [i for i in range(100)] ) )
		ints_half_reversed_half_sorted = [i for i in range(50)] + list( reversed([i for i in range(50)]) )
		
		for i in [ints_reverse_ordered, ints_half_reversed_half_sorted]:
			self.assertEqual(sorted(i), function(i) )
			
	@parameterized.expand([
		("bubble_sort", ),
		("cocktail_shaker_sort", ),
		("cyclesort", "cycle_sort"),
		("gnome_sort", ),
		("heap_sort", ),
		("insertion_sort", ),
		("merge_sort", ),
		("quick_sort", ),
		("radix_sort", "radixsort" ),
		("selection_sort", ),
		("shell_sort", ),
		("timsort", ),	])
	def test__someSorts__workForFloatLists(self, sort_file_name, sort_name=""):
		if not sort_name:
			sort_name = sort_file_name
		module = __import__("sorts."+sort_file_name, fromlist=[""])
		function = getattr(module, sort_name)
		
		doubles_random = [random.random() for i in range(100)] # avoid seeding random so the source of errors can be traced
		self.assertEqual(sorted(doubles_random), function(doubles_random) )
		
	
	def test__countingsort__worksForStringList(self):
		module = __import__("sorts.countingsort", fromlist=[""])
		function = getattr(module, "countSort")
		string_list = ["cat", "cat", "dog", "Dog", "Dog", "Fish", "bear", "lightweight thermodynamic material", "escarpment", "sleuth", "flotilla", "congeal"]
		self.assertEqual(sorted(string_list), function(string_list) )

	# take extra params
	# ("external-sort", ),
	# ("random_normaldistribution_quicksort", ),
	# ("topological_sort", )



if __name__ == "__main__":
	unittest.main()