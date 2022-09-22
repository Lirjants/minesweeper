"""
class for the mines and such that are in different locations
"""


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mine = False
        self.flag = False
        self.number = 0

    # getters
    def get_is_mine(self):
        return self.mine

    def get_is_flag(self):
        return self.flag

    def get_number(self):
        return self.number

    # ismine boolean for status. True means that location contains a mine.
    def make_mine(self, ismine):
        self.mine = ismine

    # isflag boolean for whether location contains a flag (True)
    def make_flag(self, isflag):
        self.flag = isflag

    def click(self):
        print(f"BOOM! @ x: {self.x}, y: {self.y}")

    def raise_number(self):
        self.number += 1
