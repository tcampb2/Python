import sys
import os
sys.path.append(os.path.abspath('../machine_learning'))

from parameterized import parameterized
import scoring_functions
import unittest.mock as mock
import unittest

class ScoringTestCase(unittest.TestCase):

	@parameterized.expand([
		("test_1", [5.0, 6.0, 7.0], [5.0, 6.0, 7.0], 0.0),
		("test_2", [5.0, 6.0, 7.0], [4.0, 5.0, 6.0], 1.0),
		("test_3", [5.0, 6.0, 7.0], [5.1, 6.2, 7.3], 0.2),
		("test_4", [-5.0, -6.0, -7.0], [5.0, 6.0, 7.0], 12.0),
		("test_5", [5.0, 6.0, 7.0], [-5.0, -6.0, -7.0], 12.0),
		("test_6", [5.0, 6.0, 7.0], [0.0, 0.0, 0.0], 6.0),
		("test_7", [0.0, 0.0, 0.0], [5.0, 6.0, 7.0], 6.0),
		("test_8", [-5.0, 6.0, -7.0], [5.0, -6.0, 7.0], 12.0)])
	def test_mae(self, _, predict, actual, expected):
		self.assertAlmostEqual(scoring_functions.mae(predict, actual), expected, places=3)
		
	@parameterized.expand([
		("test_1", [5.0, 6.0, 7.0], [5.0, 6.0, 7.0], 0.0),
		("test_2", [5.0, 6.0, 7.0], [4.0, 5.0, 6.0], 1.0),
		("test_3", [5.0, 6.0, 7.0], [5.1, 6.2, 7.3], 0.046667),
		("test_4", [-5.0, -6.0, -7.0], [5.0, 6.0, 7.0], 146.666666667),
		("test_5", [5.0, 6.0, 7.0], [-5.0, -6.0, -7.0], 146.666666667),
		("test_6", [5.0, 6.0, 7.0], [0.0, 0.0, 0.0], 36.666666667),
		("test_7", [0.0, 0.0, 0.0], [5.0, 6.0, 7.0], 36.666666667),
		("test_8", [-5.0, 6.0, -7.0], [5.0, -6.0, 7.0], 146.666666667)])
	def test_mse(self, _, predict, actual, expected):
		self.assertAlmostEqual(scoring_functions.mse(predict, actual), expected, places=6)
		
if __name__ == "__main__":   
	unittest.main()