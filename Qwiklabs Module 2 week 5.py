#!/usr/bin/env python3
import unittest
from emails import find_email
class TestFile(unittest.TestCase):
  def test_basic(self):
    testcase = [None, "Bree", "Campbell"]
    expected = "breee@abc.edu"
    self.assertEqual(find_email(testcase), expected)
  def test_one_name(self):
    testcase = [None, "John"]
    expected = "Missing parameters"
    self.assertEqual(find_email(testcase), expected)
if __name__ == '__main__':
  unittest.main()

  