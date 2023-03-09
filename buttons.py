from PySide6.QtWidgets import QPushButton, QGridLayout
from utils import isNumOrDot, isEmpty
from variables import MEDIUM_FONT_SIZE

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrind(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C','◀','^','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['','0','.', '='],
        ]
        
        self._makeGrid()
        
        
    def _makeGrid(self):
        for index_row,row in enumerate(self._grid_mask):
            for index_button,button_text in enumerate(row):
                button = Button(button_text)
                
                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, index_row, index_button)
                
                
                
                
                