
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel


class MyWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        """ Titulo """
        self.setWindowTitle("Calculadora")
        
        """ Layout Básico """
        self.central_widget = QWidget()
        self.v_layout = QVBoxLayout()        
        
        self.central_widget.setLayout(self.v_layout)
        self.setCentralWidget(self.central_widget)  
    
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())  


    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
        
        
        