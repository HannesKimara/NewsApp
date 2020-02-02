import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    """
    Test Case to test behaviour of Article Class
    """
    def setUp(self):
        """
        Setup method that runs before every test
        """
        self.new_article = Article(3, "Hannes Kimara", "Hannes Kimara", "https://hanneskimara.com", "https://hanneskimara.com/stash/images/1", "The Article with the Information", "2020-01-15T09:10:59Z")

    def test_instance(self):
        """
        Test to check if new_article is of instance Article
        """

        self.assertTrue(isinstance(self.new_article, Article))