class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.__width, self.__height)

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return (2 * self.__width) + (2 * self.__height)

    def get_diagonal(self):
        return (self.__width ** 2 + self.__height ** 2) ** 0.5

    def get_picture(self):
        if self.__width > 50 or self.__height > 50:
            return "Too big for picture."
        else:
            return ("{:*<{}}\n".format("", self.__width)) * self.__height

    def get_amount_inside(self, shape_instance):
        return (self.__width * self.__height) // (shape_instance.__width * shape_instance.__height)


class Square(Rectangle):
    def __init__(self, side):
        self.__side = side
        super().__init__(side, side)

    def __repr__(self):
        return "Square(side={})".format(self.__side)

    def set_height(self, height):
        self.__side = height
        super().set_height(height)

    def set_width(self, width):
        self.__side = width
        super().set_width(width)

    def set_side(self, side):
        self.__side = side
        super().set_width(side)
        super().set_height(side)
