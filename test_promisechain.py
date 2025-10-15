# test_promisechain.py
"""
Tests for PromiseChain module.
"""

import unittest
from promisechain import PromiseChain

class TestPromiseChain(unittest.TestCase):
    """Test cases for PromiseChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PromiseChain()
        self.assertIsInstance(instance, PromiseChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PromiseChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
