#!/usr/bin/python3
"""Module to test User class"""
import unittest
import json
import pycodestyle
import datetime

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test User class implementation"""
    def test_doc_module(self):
        """Module documentation"""
        doc = User.__doc__
        self.assertGreater(len(doc), 1)

    def test_pycodestyle(self):
        """Test that models/user.py conforms to Pycodestyle."""
        style_guide = pycodestyle.StyleGuide(version='2.8')
        file_to_check = 'models/user.py'
        result = style_guide.check_files([file_to_check])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_test_base_model(self):
        """Test that tests/test_models/test_user.py conforms to Pycodestyle."""
        style_guide = pycodestyle.StyleGuide(version='2.8')
        file_to_check = 'tests/test_models/test_user.py'
        result = style_guide.check_files([file_to_check])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)


if __name__ == '__main__':
    unittest.main()
