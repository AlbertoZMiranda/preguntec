from modulos import jugador
from modulos import categoria
import random

jug = jugador.Jugador()
cat = categoria.Categorias()

class Ronda():

    # Constructor
    def __init__(self):
        self.nombre = ""
        self.es_entero = False
        self.opcion = ""

    # metodos
    def iniciarJuego(self):
        self.nombre = input("Ingresar Nombre: ") 
        
        
        jug.setNombre(self.nombre)
        
    
    def nombreJugador(self):
        print(jug.getNombre())
    

    # Metodos
    def cargarCuestionario(self):
        cat.setPreguntas()

    def Preguntar(self):
        # mens = "Ingresar un numero entre (0 - 4): "
        # preg = f'{cat.getPreguntas()[0][0]["pregunta"]}: '
        # self.validarDato(mens, preg)
        print("Seleccionar Opcion: ")
        print("1 - Para ingresar Datos.")
        print("cualquier tecla - para salir")
        self.opcion = input(": ")

        salir = 0
        while self.opcion == '1':
            salir += 1
            # cuerpo del juego

            
            print("Seleccionar Opcion: ")
            print("1 - Para ingresar Datos.")
            print("cualquier tecla - para salir")
            self.opcion = input(": ")
            if salir > 2:
                self.opcion = "a"
        else:
            print(f"\nSaliste del juego {jug.getNombre()}")
            print("Puntos: ")
            print("Premios")


    def validarDato(self, mensaje, pregunta):
        seleccion = 0
        try:
            print(mensaje)
            seleccion = int(input(pregunta))
            self.es_entero = True
        except:
            print("Error: Deber ser un numero")
            self.es_entero = False
        
        while seleccion < 0 or seleccion > 4 or self.es_entero == False:
            try:
                print(mensaje)
                seleccion = int(input(pregunta))
                self.es_entero = True
            except:
                print("Error: Deber ser un numero")
                self.es_entero = False

        return seleccion