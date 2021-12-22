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
        self.elegido = ""

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

        print("\n---- Vamos a Jugar! -----: ")
        print("Para ingresar al juego. --> (1)")
        print("Para salir --> (Cualquier tecla)")
        self.opcion = input(": ")

        #salir = para salir por decision propia        
        salir = 0
        # fila = la utilizo para subir de categoria de preguntas
        fila = 0
        while self.opcion == '1':
            salir += 1
            
            # elige aleatoriamente una de las cinco opciones
            columna = random.randint(0, 4) 

            # ------------------------------------
            mensaje = "\nIngresar un numero entre (0 - 4): "
            preg = f'{cat.getPreguntas()[fila][columna]["pregunta"]}: '
            self.elegido = self.validarDato(mensaje, preg)

            # ------------------------------------

            print(salir)
            print("\n---- Vamos a Jugar! -----: ")
            print("Para ingresar al juego. --> (1)")
            print("Para salir --> (Cualquier tecla)")
            self.opcion = input(": ")
            if salir > 4:
                self.opcion = "a"
            fila += 1 
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