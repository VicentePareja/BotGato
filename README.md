# Juego de Gato (Tic Tac Toe)

Este proyecto es una implementación del clásico juego de Tic Tac Toe (también conocido como Gato), escrito en Python. El proyecto incluye tanto la opción para jugar contra otro jugador humano como contra una computadora.

## Código

El código consta de varias clases que se describen a continuación:

### Clase `Tablero`

La clase `Tablero` representa el tablero del juego. Tiene los siguientes métodos:

- `__init__`: Inicializa un tablero vacío.
- `imprimir`: Imprime el estado actual del tablero.
- `actualizar`: Actualiza el tablero con el movimiento del jugador.
- `es_ganador`: Comprueba si el jugador proporcionado ha ganado el juego.
- `es_empate`: Comprueba si el juego es un empate.

### Clase `Jugador`

La clase `Jugador` representa a un jugador en el juego. Tiene los siguientes métodos:

- `__init__`: Inicializa un jugador con un símbolo específico ("X" o "O").
- `realizar_movimiento`: Solicita al jugador que ingrese un movimiento.

### Clase `Nodo`

La clase `Nodo` representa un nodo en el árbol del juego para el algoritmo Minimax. Tiene los siguientes métodos:

- `__init__`: Inicializa el nodo con el tablero actual y el jugador actual.
- `nodos_hijos`: Genera todos los nodos hijos posibles a partir de la posición actual.
- `minimax`: Implementa el algoritmo Minimax para determinar el mejor movimiento.
- `valor`: Calcula el valor de un nodo específico.
- `escoger`: Escoge el mejor movimiento a realizar.
- `imprimir_nodo`: Imprime el nodo actual y sus nodos hijos.

### Clase `JuegoGato`

La clase `JuegoGato` es la clase principal que maneja el juego. Tiene los siguientes métodos:

- `__init__`: Inicializa el juego con un tablero y dos jugadores.
- `elegir_opcion`: Permite al jugador elegir si quiere jugar contra otro jugador humano o contra la computadora.
- `jugar`: Comienza el juego según la opción elegida.
- `juego_entre_jugadores`: Maneja el juego entre dos jugadores humanos.
- `juego_contra_computadora`: Maneja el juego contra la computadora.

## Prueba

La función `test` permite probar el código. Crea un tablero, un jugador y un nodo, y luego imprime el valor del nodo.

## Ejecución

Para iniciar el juego, ejecute el script principal de Python (`main`). Esto inicializará un juego y permitirá a los jugadores seleccionar si desean jugar contra otro jugador humano o contra la computadora.

```python
if __name__ == "__main__":
    juego = JuegoGato()
    juego.jugar()
```
