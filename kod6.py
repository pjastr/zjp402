class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"({self.__class__.__name__} : title='{self.title}" \
               f" author='{self.author}" \
               f" publisher='{self.publisher}" \
               f" year={self.year})\n"

    def __repr__(self):
        return self.__str__()


books = [Book('tytul1', 'autor1', 'publisher1', 1991),
         Book('tytul2', 'autor2', 'publisher2', 1992),
         Book('tytul3', 'autor3', 'publisher3', 1993),
         Book('tytul4', 'autor4', 'publisher4', 1994)]
print(books)
