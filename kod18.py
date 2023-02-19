x = "Olsztyn"
y = x[:: -1][:: -1]
print(x == y)
print(x is y)
print(id(x) == id(y))
print(id(x))
print(id(y))
