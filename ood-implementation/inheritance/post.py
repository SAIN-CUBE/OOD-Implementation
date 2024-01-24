class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display_post(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Author: {self.author}")

class Article(Post):
    def __init__(self, title, content, author, category):
        super().__init__(title, content, author)
        self.category = category

    def display_article(self):
        self.display_post()
        print(f"Category: {self.category}")

class Review(Post):
    def __init__(self, title, content, author, rating):
        super().__init__(title, content, author)
        self.rating = rating

    def display_review(self):
        self.display_post()
        print(f"Rating: {self.rating}")
