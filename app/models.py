class Source:
    """
    Source Class to define source objects
    """
    def __init__(self, source_id, name, description, category, language, country):
        self.id = source_id
        self.name = name
        self.description = description
        self.category = category
        self.language = language
        self.country = country