from parameterized import parameterized
import unittest.mock as mock
import unittest
import sys
import os
import numpy as np
import random

import capture_output
sys.path.append(os.path.abspath('../machine_learning'))
from perceptron import Perceptron

class PerceptronTestCase(unittest.TestCase):

	def setUp(self):
		self.perceptron = Perceptron(samples, exit)
		random.seed(1)

	def test_trannig(self):
		with capture_output.capture_output() as (out, err):
			self.perceptron.trannig()
			self.assertEqual(out.getvalue().strip(), "Epoch:\n 286\n------------------------")

	def test_sort(self):
		with capture_output.capture_output() as (out, err):
			self.perceptron.trannig()
			
		for i in range(10):
			array = []
			for j in range(3):
				array.append(random.randrange(-10, 10))
			with capture_output.capture_output() as (out, err):
				self.perceptron.sort(array)
				self.assertEqual(out.getvalue().strip(), "Sample:  " + 
				expected_output[i][0] + "\nclassification: " + expected_output[i][1])

	def test_sign(self):
		self.assertEqual(self.perceptron.sign(1), 1)
		self.assertEqual(self.perceptron.sign(-1), -1)

samples = [
    [-0.6508, 0.1097, 4.0009],
    [-1.4492, 0.8896, 4.4005],
    [2.0850, 0.6876, 12.0710],
    [0.2626, 1.1476, 7.7985],
    [0.6418, 1.0234, 7.0427],
    [0.2569, 0.6730, 8.3265],
    [1.1155, 0.6043, 7.4446],
    [0.0914, 0.3399, 7.0677],
    [0.0121, 0.5256, 4.6316],
    [-0.0429, 0.4660, 5.4323],
    [0.4340, 0.6870, 8.2287],
    [0.2735, 1.0287, 7.1934],
    [0.4839, 0.4851, 7.4850],
    [0.4089, -0.1267, 5.5019],
    [1.4391, 0.1614, 8.5843],
    [-0.9115, -0.1973, 2.1962],
    [0.3654, 1.0475, 7.4858],
    [0.2144, 0.7515, 7.1699],
    [0.2013, 1.0014, 6.5489],
    [0.6483, 0.2183, 5.8991],
    [-0.1147, 0.2242, 7.2435],
    [-0.7970, 0.8795, 3.8762],
    [-1.0625, 0.6366, 2.4707],
    [0.5307, 0.1285, 5.6883],
    [-1.2200, 0.7777, 1.7252],
    [0.3957, 0.1076, 5.6623],
    [-0.1013, 0.5989, 7.1812],
    [2.4482, 0.9455, 11.2095],
    [2.0149, 0.6192, 10.9263],
    [0.2012, 0.2611, 5.4631]

]

exit = [-1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1]

expected_output = [
	["[-1, -2, -7, 5]", "P1"],
	["[-1, 4, 5, 2]", "P2"],
	["[-1, -4, -7, 5]", "P1"],
	["[-1, -10, 2, 3]", "P1"],
	["[-1, 9, -10, 4]", "P1"],
	["[-1, -2, -3, 8]", "P1"],
	["[-1, -7, 0, -10]", "P2"],
	["[-1, -10, -10, 7]", "P1"],
	["[-1, -10, 2, -4]", "P1"],
	["[-1, 3, -10, 6]", "P1"]
]
		
if __name__ == "__main__":   
	unittest.main()