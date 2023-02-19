class Book:
    def __init__(self, title, author, publisher, year):
        if type(title) == str:
            self.__title = title
        else:
            self.__title = ""

        if type(author) == str:
            self.__author = author
        else:
            self.__author = ""

        self.__publisher = publisher
        if type(year) == int and year > 0:
            self.__year = year
        else:
            self.__year = 0

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Publisher: {self.__publisher}, Year: {self.__year}"

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if type(value) == str:
            self.__title = value
        else:
            self.__title = ""

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if type(value) == str:
            self.__author = value
        else:
            self.__author = ""

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        self.__publisher = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if isinstance(value, int) and value > 0:
            self.__year = value
        elif isinstance(value, str):
            self.__year = int(value)
        else:
            self.__year = 2023


b1 = Book("Pan Tadeusz", "Adam Mickwicz", "Znak", 2003)
print(b1)
b1.title = 34
print(b1)
b1.year = "2020"
print(b1)
