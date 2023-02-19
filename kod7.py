class Person:
    __name = "Jan"


p1 = Person()
# print(p1.__name)
print(p1._Person__name)
p1._Person__name = "Anna"
print(p1._Person__name)
