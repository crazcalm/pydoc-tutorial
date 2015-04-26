"""
This is the Doc stings located at the top of the file.
"""

# This is a comment located at the top of the file


class Hello:
    """
    This is the doc string located within the Hello class.
    """
    def __init__(self, name):
        """
        This is a doc string located within the __init__ method of the
        Hello class.

        :name: String
        :return: None
        """
        # This is a comment located in a class method
        self.name = name

    def hi(self):
        """
        This is a doc string located within the hi method the Hello class.
        """
        print("hi {}".format(self.name))


def hello_world():
    """
    This is a doc string located within a the function hello_world.
    """
    print("hello world")
