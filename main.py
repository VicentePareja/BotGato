# main.py
from backend import JuegoGato
from frontend import TicTacToeGUI
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    juego = JuegoGato()
    gui = TicTacToeGUI(juego)
    gui.show()
    sys.exit(app.exec_())
