__author__ = "Claire DeMars"

import unittest
import sys
import os
from parameterized import parameterized
import random
from filecmp import cmp


sys.path.append(os.path.abspath('../hashes'))
from chaos_machine import ChaosMachine


# Initialization
class TestChaosMachine(unittest.TestCase):

	def test(self):
		# Initialization
		machine = ChaosMachine()

		random.seed(2) # random value so get same result each time
		message = random.sample(range(0xFFFFFFFF), 100)
		for chunk in message:
			machine.push(chunk)
		
		output = []
		temp_output = open("temp_output.txt", "w+")
		for i in range(10):
			temp_output.write("%s" % format(machine.pull(), '#04x') + "\n")
			# temp_output.write(repr(machine.buffer_space) + "\n")
			# temp_output.write(repr(machine.params_space) + "\n")
			
		temp_output.close()

		self.assertTrue(cmp("temp_output.txt", "test_chaos_machine.txt" ) )
		os.remove("temp_output.txt")
		

if __name__ == "__main__":
	unittest.main()
	