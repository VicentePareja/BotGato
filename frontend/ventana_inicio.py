# ventena_inicio.py

import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout,
                             QDesktopWidget)
from PyQt5.QtCore import pyqtSignal
import parametros as p
from PyQt5.QtGui import QPixmap

ruta = "frontend\ventanas\VentanaInicio.ui"

window_name, base_class = uic.loadUiType(ruta)


class VentanaInicio(window_name, base_class):
    senal_ranking = pyqtSignal()
    senal_principal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.crear_elementos()
        self.move(350, 30)

    def crear_elementos(self):
        self.logo_inicio = QPixmap(p.RUTA_LOGO)
        self.Logo.setPixmap(self.logo_inicio)
        self.Logo.setScaledContents(True)

        self.Boton_Jugar.clicked.connect(self.abrir_principal)

        self.Boton_Rankings.clicked.connect(self.abrir_rankings)

    def abrir_principal(self):
        self.hide()
        self.senal_principal.emit()

    def abrir_rankings(self):
        self.hide()
        self.senal_ranking.emit()

    def test(self):
        print("testtt")


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.excepthook = hook
    app = QApplication([])
    Ventana_de_testeo = VentanaInicio()
    Ventana_de_testeo.show()
    app.exec()
