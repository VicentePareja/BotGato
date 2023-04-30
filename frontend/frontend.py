# frontend.py
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QSize
import sys


class TicTacToeGUI(QWidget):
    def __init__(self, juego):
        super().__init__()

        self.juego = juego
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Tic Tac Toe')

        layout = QVBoxLayout()
        grid = QGridLayout()
        grid.setSpacing(5)

        self.buttons = []

        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = QPushButton(' ')
                button.setFixedSize(QSize(100, 100))
                button.clicked.connect(
                    lambda _, fila=i, columna=j: self.realizar_jugada(fila, columna))
                grid.addWidget(button, i, j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        layout.addLayout(grid)
        self.setLayout(layout)

    def realizar_jugada(self, fila, columna):
        if self.juego.tablero.tablero[fila][columna] == " ":
            self.juego.tablero.actualizar(
                fila, columna, self.juego.jugador_actual)
            self.buttons[fila][columna].setText(
                self.juego.jugador_actual.simbolo)

            if self.juego.tablero.es_ganador(self.juego.jugador_actual):
                QMessageBox.information(
                    self, "Tic Tac Toe", f"¡El jugador {self.juego.jugador_actual.simbolo} ha ganado!")
                self.close()
            elif self.juego.tablero.es_empate():
                QMessageBox.information(self, "Tic Tac Toe", "¡Es un empate!")
                self.close()
            else:
                self.juego.cambiar_jugador()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    from backend import JuegoGato
    juego = JuegoGato()
    gui = TicTacToeGUI(juego)
    gui.show()

    sys.exit(app.exec_())
