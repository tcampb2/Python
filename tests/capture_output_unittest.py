
import unittest
import capture_output

class TestCaptureOutput(unittest.TestCase):
	
	def test_with_single_word(self):
		with capture_output.capture_output() as (out, err):
			print("hello")
			self.assertEqual( out.getvalue().strip(), "hello" )
			
	def test_with_no_words(self):
		with capture_output.capture_output() as (out, err):
			self.assertEqual( out.getvalue().strip(), "" )
		

if __name__ == "__main__":
	unittest.main()