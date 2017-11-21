from parameterized import parameterized
import unittest.mock as mock
import unittest
import sys
import os
import numpy as np

import capture_output
sys.path.append(os.path.abspath('../machine_learning'))
from decision_tree import Decision_Tree

class DecisionTreeTestCase(unittest.TestCase):

	def setUp(self):
		self.tree = Decision_Tree()

	@parameterized.expand([
		("test_1", [5.0, 6.0, 7.0], 2.0, 16.6666666667),
		("test_2", [5.0, 6.0, 8.0], 2.0, 20.3333333333),
		("test_3", [-5.0, -6.0, -7.0], 2.0, 64.6666666667),
		("test_4", [5.0, -6.0, 7.0], 2.0, 32.6666666667),
		("test_5", [0.0, 0.0, 0.0], 2.0, 4.0)])
	def test_mean_squared_error(self, _, labels, prediction, expected):
		array = np.array(labels)
		self.assertAlmostEqual(self.tree.mean_squared_error(array, prediction), expected, places=6)
		
	@parameterized.expand([
		("test_1", [[5.0], [6.0], [7.0]], [5.0, 6.0, 7.0], "Error: Input data set must be one dimensional"),
		("test_2", [5.0, 6.0, 7.0], [5.0, 6.0], "Error: X and y have different lengths"),
		("test_3", [5.0, 6.0, 7.0], [[5.0], [6.0], [7.0]], "Error: Data set labels must be one dimensional")])
	def test_train_failure(self, _, x, y, expected):
		array1 = np.array(x)
		array2 = np.array(y)
		with capture_output.capture_output() as (out, err):
			self.tree.train(array1, array2)
			self.assertEqual(out.getvalue().strip(), expected)
		
	@parameterized.expand([
		("test_1", [5.0, 6.0, 7.0], [5.0, 6.0, 7.0]),
		("test_2", [5.0, 6.0, 7.0], [-5.0, -6.0, -7.0]),
		("test_3", [5.0, 6.0, 7.0], [5.1, 6.2, 7.3]),
		("test_4", [5.0, 6.0, 7.0], [0.0, 0.0, 0.0]),
		("test_5", [0.0, 0.0, 0.0], [5.0, 6.0, 7.0])])	
	def test_train(self, _, x, y):
		array1 = np.array(x)
		array2 = np.array(y)
		self.tree.train(array1, array2)
		
	def test_predict_failure(self):
		with capture_output.capture_output() as (out, err):
			self.tree.predict(1)
			self.assertEqual(out.getvalue().strip(), "Error: Decision tree not yet trained")
		
	@parameterized.expand([
		("test_1", [5.0, 6.0, 7.0], [5.0, 6.0, 7.0], 1, 6.0),
		("test_2", [5.0, 6.0, 7.0], [-5.0, -6.0, -7.0], 1, -6.0),
		("test_3", [5.0, 6.0, 7.0], [5.1, 6.2, 7.3], 1, 6.2),
		("test_4", [5.0, 6.0, 7.0], [0.0, 0.0, 0.0], 1, 0.0),
		("test_5", [0.0, 0.0, 0.0], [5.0, 6.0, 7.0], 1, 6.0)])	
	def test_predict(self, _, x, y, input, expected):
		array1 = np.array(x)
		array2 = np.array(y)
		self.tree.train(array1, array2)	
		self.assertEqual(self.tree.predict(input), expected)
		
if __name__ == "__main__":   
	unittest.main()