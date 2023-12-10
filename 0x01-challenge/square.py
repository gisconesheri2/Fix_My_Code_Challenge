#!/usr/bin/python3
"""square model class"""


class square():
    """square model class"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """initialize the width and height class values"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        # self.height = self.width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """perimeter of the square"""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """pretty representaion of the class"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
