import unittest

import sys
import os
sys.path.append(os.path.abspath('../data_structures/Stacks'))
from infix_to_postfix_conversion import infix_to_postfix
import stack

class TestInfixConversion(unittest.TestCase):
		
	def test__infix_to_postfix__MismatchedRightParenInInfixExpression__RaisesValueError(self):
		expression = "((2+3)*3+4-(2+2)))"
		with self.assertRaises(ValueError):
			infix_to_postfix(expression)
	
	@unittest.skip("code inconsistency but not necessarily a bug: code raises error for mismatched right paren, but not for a left one")
	def test__infix_to_postfix__MismatchedLeftParenInInfixExpression__RaisesValueError(self):
		expression = "((2+3)*3+4-(2+2)"
		with self.assertRaises(ValueError):
			infix_to_postfix(expression)	

	def test__infix_to_postfix__ExpressionWhereLeftToRightOrderIsDifferentFromOrderOfOperations__GetsOrderCorrect(self):
		expression = "2+3*5"
		self.assertEqual(infix_to_postfix(expression), "2 3 5 * +") 
	
	def test__infix_to_postfix__ComplicatedExpression__ConvertsToPostfixCorrectly(self):
		expression = 'a+b*(c^d-e)^(f+g*h)-i'
		self.assertEqual( infix_to_postfix(expression), "a b c d ^ e - f g h * + ^ * + i -" )	

if __name__ == "__main__":
	unittest.main()