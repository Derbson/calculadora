
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel

class MyWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.central_widget = QWidget()
        self.v_layout = QVBoxLayout()
        
        self.label = QLabel('Hello Pedro')
        
        self.v_layout.addWidget(self.label)
        
        self.central_widget.setLayout(self.v_layout)
        self.setCentralWidget(self.central_widget)
        


