from PySide6.QtWidgets import QPushButton, QGridLayout
import math
from PySide6.QtCore import Slot
from utils import isNumOrDot, isEmpty, isValidNumber
from variables import MEDIUM_FONT_SIZE
from display import Display

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
    def __init__(self, display: Display, info,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C','◀','^','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['','0','.', '='],
        ]
        
        self.info = info        # informações que ficam logo acima do display
        self.display = display
        self._equation = ''     # info
        self._equationInitialValue = 'Sua conta' # info = "Sua conta"
        self._left = None      # valor adicionado a calculadora antes da operação
        self._right = None     # valor adicionado a calculadora após a operação
        self._op = None        # operação a ser usada /*-+^
        
        self.equation = self._equationInitialValue # info
        self._makeGrid()
        
    # info    
    @property
    def equation(self):
        return self._equation
    
    # info
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
    
    # grid de botões            
    def _makeGrid(self):
        for index_row,row in enumerate(self._grid_mask):
            for index_button,button_text in enumerate(row):
                button = Button(button_text)
                
                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, index_row, index_button)
                slot = self._makeSlot(
                    self._insertButtonTextToDisplay, button)
                
                self._connectButtonClicked(button, slot)
    
    # função de cria funções de click          
    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
        
    def _configSpecialButton(self, button):
        text = button.text()

        if text == "C":
            self._connectButtonClicked(button,self._clear)
        
        if text == "◀":
            self._connectButtonClicked(button,self.display.backspace)
        
        if text in "+-*/^":
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button)
                )
        
        if text in "=":
            self._connectButtonClicked(button, self._eq)
            
    # função recursiva que cria outras funções(Slots)
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
                
        return realSlot
    
    # adiciona os valores dos butoões númericos no display
    def _insertButtonTextToDisplay(self, button):
        button_text = button.text()
        
        newDisplayValue = self.display.text() + button_text
        
        if not isValidNumber(newDisplayValue):
            return
        
        self.display.insert(button_text)
        
    # limpa o display e retorna equation para o valor inicial
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
    
    # metodo de operadores /*-+^
    def _operatorClicked(self, button):
        button_text = button.text()
        display_text = self.display.text()
        self.display.clear()
        
        if not isValidNumber(display_text) and self._left is None:
            self.equation = 'nenhum valor'
            return
        
        if self._left is None:
            self._left = float(display_text)
        
        self._op = button_text
        self.equation = f'{self._left} {self._op} ??'
        
    
    # resultado      
    def _eq(self):
        display_text  = self.display.text()
        
        if not isValidNumber(display_text):
            self.equation = 'nada para fazer'
            return
        
        self._right = float(display_text)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'
        
        try:
            if '^' in self.equation:
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self.equation = 'zero division error'
        except OverflowError:
            self.equation = 'Número muito grande'
        
        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._right = None
        self._left = result

        if result == 'error':
            self._left = None
        