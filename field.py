"""
class for field (x,y) that contains location objects and handles communication between UI and objects
"""
import location
from random import randint


class Field:
    def __init__(self, xmax, ymax):
        self.coordlist = []
        self.xmax = xmax
        self.ymax = ymax
        for y in range(self.ymax):
            xlist = []
            for x in range(self.xmax):
                obj = location.Location(x, y)
                xlist.append(obj)
            self.coordlist.append(xlist)

    # getters
    def get_object(self, x, y):
        return self.coordlist[y][x]

    def get_coordlist(self):
        return self.coordlist

    def set_mines(self, how_many):
        counter = 0
        while counter < how_many:
            x = randint(0, self.xmax - 1)
            y = randint(0, self.ymax - 1)
            if not self.coordlist[y][x].get_is_mine():
                self.coordlist[y][x].make_mine(True)
                counter += 1
                # print(f"In field - x: {x}, y: {y}")

    def click(self, x, y):
        loc = self.coordlist[y][x]
        if loc.get_is_mine():
            # Field: lose game
            print("Field: lose game")
            return False    # is mine. Lose game

    def count_numbers(self):
        for y in self.coordlist:
            for loc in y:
                if loc.get_is_mine():
                    # no need for number. Number is 9 for mines
                    pass
                else:
                    # if location is on the border, index would be out of range
                    # upper row
                    if loc.x != 0 and loc.y != 0:    # upper left corner
                        if self.coordlist[loc.y - 1][loc.x - 1].get_is_mine():
                            loc.raise_number()
                    if loc.y != 0:  # above
                        if self.coordlist[loc.y - 1][loc.x].get_is_mine():
                            loc.raise_number()
                    if loc.x != self.xmax - 1 and loc.y != 0:    # upper right corner
                        if self.coordlist[loc.y - 1][loc.x + 1].get_is_mine():
                            loc.raise_number()
                    # same row
                    if loc.x != 0:  # left
                        if self.coordlist[loc.y][loc.x - 1].get_is_mine():
                            loc.raise_number()
                    if loc.x != self.xmax - 1:  # right
                        if self.coordlist[loc.y][loc.x + 1].get_is_mine():
                            loc.raise_number()
                    # lower row
                    if loc.x != 0 and loc.y != self.ymax - 1:    # lower left corner
                        if self.coordlist[loc.y + 1][loc.x - 1].get_is_mine():
                            loc.raise_number()
                    if loc.y != self.ymax - 1:  # below
                        if self.coordlist[loc.y + 1][loc.x].get_is_mine():
                            loc.raise_number()
                    if loc.x != self.xmax - 1 and loc.y != self.ymax - 1:    # lower right corner
                        if self.coordlist[loc.y + 1][loc.x + 1].get_is_mine():
                            loc.raise_number()


if __name__ == '__main__':
    # unit tests
    kentt?? = Field(10, 10)
    print(kentt??.get_coordlist())
    testobj = kentt??.get_coordlist()[2][5]  # (y, x)
    print("x: 5, y: 2")
    print(testobj)
    print(testobj.get_is_mine())
    testobj.make_mine(True)
    print(testobj.get_is_mine())
    testobj2 = kentt??.get_coordlist()[1][5]
    testobj2.make_mine(True)
    testobj_yv = kentt??.get_coordlist()[1][4]
    testobj_o = kentt??.get_coordlist()[2][6]
    testobj_a = kentt??.get_coordlist()[3][5]
    """
       4  5  6
    1[yv][X][2] yv = 2      [0,0][0,1][0,2]
    2[ 2][X][o]  o = 2      [1,0][1,1][1,2]
    3[ 1][a][1]  a = 1      [2,0][2,1][2,2]
    """
    kentt??.count_numbers()
    print(testobj_yv.get_number())
    print(testobj_o.get_number())
    print(testobj_a.get_number())
    """
       1  2  3
    1[yv][X][2]     [0,0][0,1][0,2]
    2[ 2][X][o]     [1,0][1,1][1,2]
    3[ 1][a][1]     [2,0][2,1][2,2]
    """
    kentt??2 = Field(5, 4)
    testobj1 = kentt??2.get_coordlist()[0][0]  # (y, x)
    testobj2 = kentt??2.get_coordlist()[2][2]  # (y, x)
    testobj1.make_mine(True)
    testobj2.make_mine(True)
    kentt??2.count_numbers()
    lista = []
    for rivi in kentt??2.get_coordlist():
        listarivi = []
        for miina in rivi:
            if miina.get_is_mine():
                listarivi.append("X")
            else:
                listarivi.append(str(miina.get_number()))
        lista.append(listarivi)
    for rivi in lista:
        print(rivi)
