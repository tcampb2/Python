from parameterized import parameterized
import unittest.mock as mock
import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.abspath('../machine_learning'))
import scoring_functions

class ScoringTestCase(unittest.TestCase):

	@parameterized.expand([
		("test_1", [5.0, 6.0, 7.0], [5.0, 6.0, 7.0], 0.0),
		("test_2", [5.0, 6.0, 7.0], [4.0, 5.0, 6.0], 1.0),
		("test_3", [5.0, 6.0, 7.0], [5.1, 6.2, 7.3], 0.2),
		("test_4", [5.0, 6.0, 7.0], [0.0, 0.0, 0.0], 6.0),
		("test_5", [0.0, 0.0, 0.0], [5.0, 6.0, 7.0], 6.0)])
	def test_mae(self, _, predict, actual, expected):
		self.assertAlmostEqual(scoring_functions.mae(predict, actual), expected, places=3)
		
	@parameterized.expand([
		("test_1", [5.0, 6.0, 7.0], [5.0, 6.0, 7.0], 0.0),
		("test_2", [5.0, 6.0, 7.0], [4.0, 5.0, 6.0], 1.0),
		("test_3", [5.0, 6.0, 7.0], [5.1, 6.2, 7.3], 0.046667),
		("test_4", [5.0, 6.0, 7.0], [0.0, 0.0, 0.0], 36.666666667),
		("test_5", [0.0, 0.0, 0.0], [5.0, 6.0, 7.0], 36.666666667)])
	def test_mse(self, _, predict, actual, expected):
		self.assertAlmostEqual(scoring_functions.mse(predict, actual), expected, places=6)
		
	@parameterized.expand([
		("test_1", [5.0, 6.0, 7.0], [5.0, 6.0, 7.0], 0.0),
		("test_2", [5.0, 6.0, 7.0], [4.0, 5.0, 6.0], 1.0),
		("test_3", [5.0, 6.0, 7.0], [5.1, 6.2, 7.3], 0.216024689),
		("test_4", [5.0, 6.0, 7.0], [0.0, 0.0, 0.0], 6.055300708),
		("test_5", [0.0, 0.0, 0.0], [5.0, 6.0, 7.0], 6.055300708),])
	def test_rmse(self, _, predict, actual, expected):
		self.assertAlmostEqual(scoring_functions.rmse(predict, actual), expected, places=6)
		
	@parameterized.expand([
		("test_1", [5.0, 6.0, 7.0], [5.0, 6.0, 7.0], 0.0),
		("test_2", [5.0, 6.0, 7.0], [4.0, 5.0, 6.0], 0.157939033),
		("test_3", [5.0, 6.0, 7.0], [5.1, 6.2, 7.3], 0.028414108),
		("test_4", [5.0, 6.0, 7.0], [0.0, 0.0, 0.0], 1.942596666),
		("test_5", [0.0, 0.0, 0.0], [5.0, 6.0, 7.0], 1.942596666)])
	def test_rmsle(self, _, predict, actual, expected):
		self.assertAlmostEqual(scoring_functions.rmsle(predict, actual), expected, places=6)
		
if __name__ == "__main__":   
	unittest.main()