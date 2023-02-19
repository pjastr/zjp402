class Person:

    def __str__(self):
        return type(self).__name__


p1 = Person()
print(p1)
