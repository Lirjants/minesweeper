"""
main-file that starts the game
Creates the GUI

TODO:
-resizing (size fixed for now)
-always 10 mines
-always 10x10 field
-pictures are working, but numbers missing
-y=x and x=y in coordinate calls annoyingly
"""

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QAbstractButton
from PyQt6.QtGui import QPalette, QColor, QIcon
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

        self.setWindowTitle("Minesweeper")

        # game field. Grid (x, y) of Location objects
        self.field = field.Field(xmax, ymax)

        # put mines on field
        self.field.set_mines(how_many_mines)

        # Make the grid into a layout
        layout = QGridLayout()
        for y in range(ymax):
            for x in range(xmax):
                # show which ones are mines
                if self.field.get_object(x, y).get_is_mine():
                    buttonm = QPushButton()
                    buttonm.setIcon(QIcon("mine.png"))
                    buttonm.setFixedSize(QSize(14, 14))  # How large is the button (width, height)
                    buttonm.setIconSize(QSize(14, 14))  # How large is the picture (width, height)
                    buttonm.clicked.connect(self.field.get_object(x, y).click)
                    layout.addWidget(buttonm, y, x)
                    # layout.addWidget(Color('red'), y, x)
                    # print(f"In main - x: {x}, y: {y}")
                else:
                    layout.addWidget(Color('gray'), y, x)
        # test
        # layout.addWidget(Color('blue'), 2, 8)
        # print("Blue is x: 8, y: 2")

        # spaces around locations (3 pixels)
        layout.setSpacing(3)

        grid = QWidget()
        grid.setLayout(layout)

        # Fixed size for now
        self.setFixedSize(400, 300)

        # Set the central widget of the Window.
        self.setCentralWidget(grid)


# Application GUI
app = QApplication([])

# first always 10x10 field with 10 mines
window = MainWindow(15, 20, 10)
window.show()  # show window.

# execute the app
app.exec()
