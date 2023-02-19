class Product:

    def __init__(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            self.__name = ""


p1 = Product("Apple")
print("Name:", p1.name)
p2 = Product(344)
print("Name:", p2.name)
p1.name = True
print("Name:", p1.name)
