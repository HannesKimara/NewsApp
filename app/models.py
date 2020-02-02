class Source:
    """
    Source Class to define Source Objects
    """
    def __init__(self, source_id, name, description, category, language, country):
        self.id = source_id
        self.name = name
        self.description = description
        self.category = category
        self.language = language
        self.country = country

class Article:
    """
    Article Class to define Article Objects
    """
    def __init__(self, article_id, author, title, link, image_url, description, published_at):
        self.id = article_id
        self.author = author
        self.title = title
        self.link = link
        self.image_url = image_url
        self.description = description
        self.published_at = published_at 