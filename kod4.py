class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} {self.age}"


people = [Person("Jan", 30), Person("Katarzyna", 40)]
print(people)
print(people[0])
