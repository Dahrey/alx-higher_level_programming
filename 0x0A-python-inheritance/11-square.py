#!/usr/bin/python3
"""
Module that defines a Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a Square instance
        Args:
            size (int): The size of the square
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the square description: [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.width, self.height)

if __name__ == "__main__":
    Square = __import__('11-square').Square

    s = Square(13)

    print(s)
    print(s.area())

