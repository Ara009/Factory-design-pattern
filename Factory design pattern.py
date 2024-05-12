from abc import ABCMeta,abstractstaticmethod

class shape(metaclass=ABCMeta):
    @abstractstaticmethod
    def shape_method():
        """shape interface"""

class Triange(shape):
    def __init__(self):
        self.name="basic Triangle shape"
    def shape_method(self):
        print(self.name)

class Circle(shape):
    def __init__(self):
        self.name="basic Circle shape"
    def shape_method(self):
        print(self.name)
class Square(shape):
    def __init__(self):
        self.name="basic Square shape"
    def shape_method(self):
        print(self.name)

shape1 = Triange()

shape2 = Circle()

shape3 = Square()


class factoryshape:
    @staticmethod
    def build_shape(shape_type):
        if shape_type == "Triangle":
            return Triange()
        if shape_type == "Circle":
            return Circle()
        if shape_type == "Square":
            return Square()
        else:
            print("invalid entry")
if __name__=='__main__':
    choice = input("Enter the shape you want?")
    shapes = factoryshape.build_shape(choice)
    shapes.shape_method()
