# test_oauth2provider.py
"""
Tests for OAuth2Provider module.
"""

import unittest
from oauth2provider import OAuth2Provider

class TestOAuth2Provider(unittest.TestCase):
    """Test cases for OAuth2Provider class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OAuth2Provider()
        self.assertIsInstance(instance, OAuth2Provider)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OAuth2Provider()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
