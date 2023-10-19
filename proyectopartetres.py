"""Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:
Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal  e imprimir el nuevo número hasta el número 50.
La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.
Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os"""
import os 
from readchar import readkey, key
def borrar_terminal():
    os.system('cls' if os.name=='nt' else 'clear')
numero=0
while True:
        tecla=readkey()
        if  tecla=="n":
            if numero < 50:
                borrar_terminal()
                numero=numero+1
                print(numero)
            elif numero==50:
                 break