import unittest
from app.models import Source

class TestSource(unittest.TestCase):
    """
    Test Case to test behaviour of Source Class
    """

    def setUp(self):
        """
        Setup method that runs before every test
        """

        self.new_source = Source(5, "The Source", "Gotham Tales", "general", "en", "us")

    def test_instance(self):
        """
        Test to check if new_source is of instance Source
        """

        self.assertTrue(isinstance(self.new_source, Source))