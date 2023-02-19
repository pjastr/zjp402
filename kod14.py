class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_x(self, value):
        self.__x = value

    x = property(fset=set_x)


point = Point(12, 5)
print(point.x)
point.x = 22
