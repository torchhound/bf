import unittest
import interpreter

class InterpreterTests(unittest.TestCase):
	"""Tests for interpreter.py"""

	def testInterpreterHelloWorld(self):
		"""Checks output of hello world"""
		self.assertTrue(interpreter.parse("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.") == "Hello World!")

if __name__ == "__main__":
	unittest.main()