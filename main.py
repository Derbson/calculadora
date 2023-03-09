import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from window import MyWindow
from display import Display
from variables import WINDOW_INCO_PATH
from style import setupTheme
from buttons import ButtonsGrind
from info import Info


if __name__ == '__main__':
    # cria app e janela
    app = QApplication(sys.argv)
    setupTheme()
    
    window = MyWindow()
    
    # define icon
    icon = QIcon(str(WINDOW_INCO_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)    
    
    #info
    info = Info('25 * 5')
    window.addWidgetToVLayout(info)
    
    # Display
    display = Display()
    window.addWidgetToVLayout(display)
    
    # Grid
    buttons_grid = ButtonsGrind()
    window.v_layout.addLayout(buttons_grid)
    
    # executa
    window.show()
    app.exec()

