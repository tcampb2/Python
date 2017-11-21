__author__ = "Claire DeMars"

import unittest
import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath('../other'))
from frequency_finder import englishFreqMatchScore

class TestFrequencyFinder(unittest.TestCase):
	
	@parameterized.expand([
		("commonValues", "nn", 1),
		("upperCase", "NN", 1),
		("valuesNeitherCommonNorUncommon", "ss", 0),
		("valuesNeitherCommonNorUncommon", "bb", 0),
		("uncommonValues", "ETAOINSHRDLCUMWFGYPBKJXQZ ETAOINSHRDLCUMWFGYPBKJXQZ v", 1),
	])
	def test(self, testname, message, answer):
		self.assertEqual(englishFreqMatchScore(message), answer)
	# ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

if __name__ == "__main__":
	unittest.main()