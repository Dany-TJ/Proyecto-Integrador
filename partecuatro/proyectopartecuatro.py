import os
from typing import List, Tuple

def crear_laberinto(laberinto_str: str) -> List[List[str]]:
    return [list(fila) for fila in laberinto_str.split("\n")]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mapa(mapa: List[List[str]]):
    for fila in mapa:
        print(''.join(fila))

def main_loop(mapa: List[List[str]], pos_inicial: Tuple[int, int], pos_final: Tuple[int, int]):
    px, py = pos_inicial

    while (px, py) != pos_final:
        mapa[py][px] = 'P'
        limpiar_pantalla()
        mostrar_mapa(mapa)
        mapa[py][px] = '.'

        # Leer tecla del usuario
        direccion = input("Ingrese la dirección (arriba: w, abajo: s, izquierda: a, derecha: d): ")

        if direccion == 'w':
            if py > 0 and mapa[py-1][px] != '#':
                py -= 1
        elif direccion == 's':
            if py < len(mapa) - 1 and mapa[py+1][px] != '#':
                py += 1
        elif direccion == 'a':
            if px > 0 and mapa[py][px-1] != '#':
                px -= 1
        elif direccion == 'd':
            if px < len(mapa[0]) - 1 and mapa[py][px+1] != '#':
                px += 1

    limpiar_pantalla()
    mostrar_mapa(mapa)
    print("¡Has llegado a la meta!")

# Definir el mapa y las posiciones inicial y final
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = crear_laberinto(laberinto)
posicion_inicial = (0, 0)
posicion_final = (len(mapa[0]) - 1, len(mapa) - 1)

main_loop(mapa, posicion_inicial, posicion_final)