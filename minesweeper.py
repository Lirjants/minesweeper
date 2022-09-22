"""
main-file that starts the game
Creates the GUI

TODO:
-resizing (size fixed for now)
-always 10 mines
-always 10x10 field
-pictures
+ y, x now working, I think
-statusbar
- look at QPixmap.swap()
- location:
    self.clicked = False -> .click changes, then show_location updates the field
    loc.x and loc.y to use getters instead
"""

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QPalette, QColor, QIcon, QPixmap
import field


# a placeholder class to draw solid colors until pictures are made
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


# Subclass QMainWindow to customize application's main window
class MainWindow(QMainWindow):
    def __init__(self, xmax, ymax, how_many_mines):
        super().__init__()
        self.xmax = xmax
        self.ymax = ymax
        self.icon_size = 28

        self.setWindowTitle("Minesweeper")

        # game field. Grid (x, y) of Location objects
        self.field = field.Field(xmax, ymax)

        # put mines on field and count numbers
        self.field.set_mines(how_many_mines)
        self.field.count_numbers()

        # Make the grid into a layout
        self.layout = QGridLayout()
        for y in range(ymax):
            for x in range(xmax):
                buttonm = QPushButton()
                buttonm.setIcon(QIcon("closed.png"))
                # How large is the button (width, height):
                buttonm.setFixedSize(QSize(self.icon_size, self.icon_size))
                # How large is the picture (width, height):
                buttonm.setIconSize(QSize(self.icon_size, self.icon_size))
                buttonm.clicked.connect(
                    lambda state, x_coord=x, y_coord=y:
                    self.show_location(x_coord, y_coord))
                # buttonm.clicked.connect(self.field.get_object(x, y).click)
                self.layout.addWidget(buttonm, y, x)

        # spaces around locations (2 pixels)
        self.layout.setSpacing(2)

        self.grid = QWidget()

        self.grid.setLayout(self.layout)

        # Fixed size for now
        self.setFixedSize(600, 450)

        # Set the central widget of the Window.
        self.setCentralWidget(self.grid)

    def show_location(self, x, y):
        loc = self.field.get_object(x, y)
        # print(f"x: {loc.x}, y: {loc.y}")
        if loc.get_clicked():
            return
        if loc.get_is_mine():
            loc.click()
            self.lose_game()
        else:
            loc.click()
            number_image = QPixmap(f"{loc.get_number()}.png")   # get number picture
            number_image = number_image.scaled(self.icon_size, self.icon_size)  # resize
            image_label = QLabel()  # make label for widget
            image_label.setPixmap(number_image)     # put picture in label
            self.layout.addWidget(image_label, loc.y, loc.x)    # put widget in the grid
            # set layout if needed
            if loc.get_number() == 0:   # show all connecting zeros
                if x != 0 and y != 0:   # upper left corner
                    self.show_location(x - 1, y - 1)
                if y != 0:  # above
                    self.show_location(x, y - 1)
                if x != self.xmax - 1 and y != 0:   # upper right corner
                    self.show_location(x + 1, y - 1)
                if x != 0:  # left
                    self.show_location(x - 1, y)
                if x != self.xmax - 1:  # right
                    self.show_location(x + 1, y)
                if x != 0 and y != self.ymax - 1:   # lower left corner
                    self.show_location(x - 1, y + 1)
                if y != self.ymax - 1:  # below
                    self.show_location(x, y + 1)
                if y != self.ymax - 1 and x != self.xmax - 1:   # lower right corner
                    self.show_location(x + 1, y + 1)

    def lose_game(self):
        # show the whole field
        # print("You lost.")
        for y in range(self.ymax - 1):
            for x in range(self.xmax - 1):
                self.show_location(x, y)

    def win_game(self):
        pass


# Application GUI
app = QApplication([])

# first always 10x10 field with 10 mines
window = MainWindow(15, 20, 25)
window.show()  # show window.

# execute the app
app.exec()
