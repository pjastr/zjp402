class Person:
    name = "Jan"

    def __repr__(self):
        return "Nazwa %s" % self.name


p1 = Person()
p1.name = "Sylwia"
print(p1)
