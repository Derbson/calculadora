import sys
from PySide6.QtWidgets import QApplication
from window import MyWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    app.exec()

