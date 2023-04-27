# clase tablero. Es un tablero, ve si hay un ganador y se actualiza.

class Tablero:
    def __init__(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]

    def imprimir(self):
        for fila in self.tablero:
            print(" | ".join(fila))
            print("-" * 9)

    def actualizar(self, fila, columna, jugador):
        try:
            if self.tablero[fila][columna] == " ":
                self.tablero[fila][columna] = jugador.simbolo
                return True, ""
            else:
                return False, "Celda ocupada. Intenta de nuevo."
        except IndexError:
            return False, "Coordenadas inválidas. Ingresa valores entre 0 y 2."

    def es_ganador(self, jugador):
        simbolo = jugador.simbolo
        for fila in self.tablero:
            if fila.count(simbolo) == 3:
                return True

        for columna in range(3):
            if [self.tablero[fila][columna] for fila in range(3)].count(simbolo) == 3:
                return True

        if [self.tablero[i][i] for i in range(3)].count(simbolo) == 3:
            return True

        if [self.tablero[i][2 - i] for i in range(3)].count(simbolo) == 3:
            return True

        return False

    def es_empate(self):
        return all(celda != " " for fila in self.tablero for celda in fila)

# Clase jugador, recuerda el simbolo del mismo y realiza los movimientos en el tablero.


class Jugador:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def realizar_movimiento(self):
        while True:
            try:
                fila = int(
                    input(f"Jugador {self.simbolo}, ingresa la fila (0-2): "))
                columna = int(
                    input(f"Jugador {self.simbolo}, ingresa la columna (0-2): "))
                return fila, columna
            except ValueError:
                print("Por favor, ingresa números enteros válidos.")

# Un nodo es una unidad que sabe la posición actual del tablero y quién está jugando.
# También, es capaz de identificar cuales son la siguiente jugadas posibles y el "valor de ellas"


class Nodo:

    def __init__(self, tablero, jugador_actual, ultimo_movimiento=None):
        self.tablero = tablero
        self.jugador_actual = jugador_actual
        self.ultimo_movimiento = ultimo_movimiento
        self.hijos = []

    def calcular_valor(self):

        ganador = self.tablero.es_ganador(self.jugador_actual)
        empate = self.tablero.es_empate()

        if ganador:
            return 1
        elif empate:
            return 0
        elif any(celda == " " for fila in self.tablero.tablero for celda in fila):
            return None
        else:
            return -1

    def nodos_hijos(self):
        siguiente_jugador = Jugador(
            "O") if self.jugador_actual.simbolo == "X" else Jugador("X")
        hijos = []

        for fila in range(3):
            for columna in range(3):
                if self.tablero.tablero[fila][columna] == " ":
                    nuevo_tablero = Tablero()
                    nuevo_tablero.tablero = [fila.copy()
                                             for fila in self.tablero.tablero]

                    nuevo_tablero.actualizar(
                        fila, columna, self.jugador_actual)
                    hijo = Nodo(nuevo_tablero, siguiente_jugador)
                    hijos.append(hijo)

        return hijos

    def minimax(self, maximizando):
        self.valor = self.calcular_valor()
        if self.valor is not None:
            return self.valor, None

        if maximizando:
            mejor_valor = float('-inf')
            mejor_movimiento = None
            for hijo in self.nodos_hijos():
                valor_hijo, _ = hijo.minimax(False)
                if valor_hijo > mejor_valor:
                    mejor_valor = valor_hijo
                    mejor_movimiento = hijo
            return mejor_valor, mejor_movimiento

        else:
            mejor_valor = float('inf')
            mejor_movimiento = None
            for hijo in self.nodos_hijos():
                valor_hijo, _ = hijo.minimax(True)
                if valor_hijo < mejor_valor:
                    mejor_valor = valor_hijo
                    mejor_movimiento = hijo
            return mejor_valor, mejor_movimiento

    def imprimir_nodo(self):
        print(f"Jugador actual: {self.jugador.simbolo}")
        print("Posición actual del tablero:")
        self.tablero.imprimir()
        hijos = self.nodos_hijos()

        print("Posiciones de los nodos hijos:")
        for i, hijo in enumerate(hijos, start=1):
            print(f"Hijo {i}:")
            hijo.tablero.imprimir()

# Corre que almacena el juego. Esta posee un tablero y dos jugadores. También pregunta si se desea
# jugar contra otro jugador o contra la computadora


class JuegoGato:
    def __init__(self):
        self.tablero = Tablero()
        self.jugador_x = Jugador("X")
        self.jugador_o = Jugador("O")
        self.jugador_actual = self.jugador_x

    def elegir_opcion(self):
        print("Opciones de juego:")
        print("1. Jugar contra otro jugador")
        print("2. Jugar contra la computadora")

        while True:
            try:
                opcion = int(input("Elige una opción (1 o 2): "))
                if opcion in (1, 2):
                    return opcion
                else:
                    print("Opción inválida. Ingresa 1 o 2.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")

    def jugar(self):
        opcion = self.elegir_opcion()

        if opcion == 1:
            self.juego_entre_jugadores()
        elif opcion == 2:
            self.juego_contra_computadora()

    def juego_entre_jugadores(self):
        while True:
            self.tablero.imprimir()

            if self.tablero.es_ganador(self.jugador_x):
                print("¡El jugador X ha ganado!")
                break
            elif self.tablero.es_ganador(self.jugador_o):
                print("¡El jugador O ha ganado!")
                break
            elif self.tablero.es_empate():
                print("¡Es un empate!")
                break

            movimiento_valido = False
            while not movimiento_valido:
                fila, columna = self.jugador_actual.realizar_movimiento()
                movimiento_valido, mensaje_error = self.tablero.actualizar(
                    fila, columna, self.jugador_actual)

                if not movimiento_valido:
                    print(mensaje_error)

            self.jugador_actual = self.jugador_o if self.jugador_actual == self.jugador_x else self.jugador_x

    def juego_contra_computadora(self):
        while True:
            self.tablero.imprimir()

            if self.tablero.es_ganador(self.jugador_x):
                print("¡El jugador X ha ganado!")
                break
            elif self.tablero.es_ganador(self.jugador_o):
                print("¡La computadora ha ganado!")
                break
            elif self.tablero.es_empate():
                print("¡Es un empate!")
                break

            if self.jugador_actual == self.jugador_x:
                movimiento_valido = False
                while not movimiento_valido:
                    fila, columna = self.jugador_actual.realizar_movimiento()
                    movimiento_valido, mensaje_error = self.tablero.actualizar(
                        fila, columna, self.jugador_actual)

                    if not movimiento_valido:
                        print(mensaje_error)
            else:
                nodo = Nodo(self.tablero, self.jugador_actual)
                _, mejor_movimiento = nodo.minimax(True)
                mejor_fila, mejor_columna = mejor_movimiento.ultimo_movimiento
                self.tablero.actualizar(
                    mejor_fila, mejor_columna, self.jugador_actual)

            self.jugador_actual = self.jugador_o if self.jugador_actual == self.jugador_x else self.jugador_x


if __name__ == "__main__":
    juego = JuegoGato()
    juego.jugar()
