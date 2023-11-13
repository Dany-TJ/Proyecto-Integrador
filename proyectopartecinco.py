import os
import random

class Juego:
    def __init__(self, mapa, pos_inicial, pos_final):
        self.mapa = mapa
        self.posicion_inicial = pos_inicial
        self.posicion_final = pos_final

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(self):
        for fila in self.mapa:
            print(''.join(fila))

    def mover_jugador(self, direccion):
        px, py = self.posicion_inicial

        if direccion == 'w':
            if py > 0 and self.mapa[py-1][px] != '#':
                py -= 1
        elif direccion == 's':
            if py < len(self.mapa) - 1 and self.mapa[py+1][px] != '#':
                py += 1
        elif direccion == 'a':
            if px > 0 and self.mapa[py][px-1] != '#':
                px -= 1
        elif direccion == 'd':
            if px < len(self.mapa[0]) - 1 and self.mapa[py][px+1] != '#':
                px += 1

        self.posicion_inicial = (px, py)

    def jugar(self):
        px, py = self.posicion_inicial

        while (px, py) != self.posicion_final:
            self.mapa[py][px] = 'P'
            self.limpiar_pantalla()
            self.mostrar_mapa()
            self.mapa[py][px] = '.'

            # Leer tecla del usuario
            direccion = input("Ingrese la dirección (arriba: w, abajo: s, izquierda: a, derecha: d): ")
            self.mover_jugador(direccion)

        self.limpiar_pantalla()
        self.mostrar_mapa()
        print("¡Has llegado a la meta!")


class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        # Obtener una lista de archivos en la carpeta de mapas
        archivos = os.listdir(path_a_mapas)

        # Elegir un archivo al azar
        nombre_archivo = random.choice(archivos)

        # Componer el path completo
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            contenido = archivo.read()

        # Obtener el mapa y las posiciones del contenido del archivo
        contenido = contenido.strip().split('\n')
        dimensiones = contenido[0].split()
        filas = contenido[1:-2]
        pos_inicial = tuple(map(int, contenido[-2].split()))
        pos_final = tuple(map(int, contenido[-1].split()))

        # Llamar al constructor de la clase padre con los valores obtenidos
        super().__init__(filas, pos_inicial, pos_final)


if __name__ == "__main__":
    laberinto = JuegoArchivo("path_a_tu_carpeta_de_mapas")
    laberinto.jugar()
