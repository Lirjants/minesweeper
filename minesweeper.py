"""
main-file that starts the game
Creates the GUI

TODO:
-resizing (size fixed for now)
-always 10 mines
-always 10x10 field
-pictures are working, but numbers missing
- y, x now working, I think
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
        self.icon_size = 14

        self.setWindowTitle("Minesweeper")

        # game field. Grid (x, y) of Location objects
        self.field = field.Field(xmax, ymax)

        # put mines on field
        self.field.set_mines(how_many_mines)

        # Make the grid into a layout
        self.layout = QGridLayout()
        for y in range(ymax):
            for x in range(xmax):
                # show which ones are mines
                if self.field.get_object(x, y).get_is_mine():
                    buttonm = QPushButton()
                    buttonm.setIcon(QIcon("mine.png"))
                    # How large is the button (width, height):
                    buttonm.setFixedSize(QSize(self.icon_size, self.icon_size))
                    # How large is the picture (width, height):
                    buttonm.setIconSize(QSize(self.icon_size, self.icon_size))
                    buttonm.clicked.connect(self.field.get_object(x, y).click)
                    self.layout.addWidget(buttonm, y, x)
                    # self.layout.addWidget(Color('red'), y, x)
                    # print(f"In main - x: {x}, y: {y}")
                else:
                    self.layout.addWidget(Color('gray'), y, x)
        # test
        # layout.addWidget(Color('blue'), 2, 8)
        # print("Blue is x: 8, y: 2")

        # spaces around locations (3 pixels)
        self.layout.setSpacing(3)

        self.grid = QWidget()
        self.grid.setLayout(self.layout)

        # Fixed size for now
        self.setFixedSize(400, 300)

        # Set the central widget of the Window.
        self.setCentralWidget(self.grid)

    def show_location(self, x, y):
        loc = self.field.get_object(x, y)
        if loc.get_is_mine():
            self.lose_game()
        elif loc.get_number() > 0:
            number_image = QPixmap(f"{loc.get_number()}.png", self.icon_size, self.icon_size)
            image_label = QLabel()
            image_label.setPixmap(number_image)
            self.layout.addWidget(image_label, y, x)
            # set layout if needed
        # elif loc.get_number() == 0:   # show all connecting zeros

    def lose_game(self):
        pass


# Application GUI
app = QApplication([])

# first always 10x10 field with 10 mines
window = MainWindow(15, 20, 10)
window.show()  # show window.

# execute the app
app.exec()
