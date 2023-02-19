class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name


jack1 = Person('Jack', 23)
jack2 = Person('Jack', 40)
print(jack1 == jack2)
print(jack1 is jack2)
