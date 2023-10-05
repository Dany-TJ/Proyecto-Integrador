#Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas
# y sólo terminará cuando se presione la tecla ↑ indicada como UP

#De la biblioteca "readcher" importamos la función llamada "readkey" para recibir 
#información o interactuar por medio del teclado y "Key"
from readchar import readkey, key
print("Bienvenido(a), ¡pronto iniciará ésta travesía!")
print("recuerda que al presionar la tecla ↑  terminas el juego")
while True:
    tecla = readkey()
    if tecla == key.UP:
        print("¡Hemos terminado el juego, hasta la proxima!")
        break
    print(tecla)
