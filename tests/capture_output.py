from contextlib import contextmanager
from StringIO import StringIO

# source: https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python

@contextmanager
def capture_output():
	"""
		Usage: 
		with captured_output() as (out, err):
			foo()
		# This can go inside or outside the `with` block
		output = out.getvalue().strip()
		self.assertEqual(output, 'hello world!')
	"""
	new_out, new_err = StringIO(), StringIO()
	old_out, old_err = sys.stdout, sys.stderr
	try:
		sys.stdout, sys.stderr = new_out, new_err
		yield sys.stdout, sys.stderr
	finally:
		sys.stdout, sys.stderr = old_out, old_err

