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
        self.msgFinal = ""

    # metodos
    def iniciarJuego(self):
        print("""
        ------   BIENVENIDO A PREGUNTEC   ------
        Es un Juego de Preguntas Sobre Tecnologia

        por cada pregunta corectamente constestada ganaras '1 punto'
        cada punto sirve para 'reclamar un premio'

        """)
        self.nombre = input("Ingresar Tu Nombre: ")        
        
        jug.setNombre(self.nombre)
    
    def nombreJugador(self):
        return jug.getNombre()   
    
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
            matrizPregunta = cat.getPreguntas()[fila][columna]
            #
            mensaje = "Ingresar un numero entre (0 - 3): "
            preg = f'{matrizPregunta["pregunta"]}: '
            opc = matrizPregunta["opciones"]
            rCorrecta = matrizPregunta["respuesta"]
            nameCat = matrizPregunta["nivel"]

            # self.elegido: es un numero, pero en formato cadena ej: '2'
            self.elegido = self.validarDato(mensaje, preg, opc, nameCat)

            # -----------------------------------
            cont = 0
            if self.elegido == int(rCorrecta):
                print("----- CORRECTO :) -----")
                cont += 1
                
                jug.setPuntos(jug.getPuntos() + cont)
            else:
                print("----- INCORRECTO :( -----")
                salir = 5
                jug.setPuntos(0)
            # ------------------------------------
            
            if salir > 4:
                self.opcion = "a"
                self.msgFinal = "Completaste las rondas: felicitaciones"
            else:
                print("\n---- Vamos a Jugar! -----: ")
                print("Para ingresar al juego. --> (1)")
                print("Para salir --> (Cualquier tecla)")
                self.opcion = input(": ")
                fila += 1

        # llamamos los resultados desde la clase jugador 
        jug.setPremio()
        print(jug.infoJugador(jug.getNombre(), jug.getPuntos(), jug.getPremio(), self.msgFinal))

    #ValidarDato: Metodo que restringe el ingreso de datos tipo cadena,
    # restringe los datos menores a cero y mayores a 3
    def validarDato(self, mensaje, pregunta, opciones, nameCat):
        seleccion = 0
        try:
            print(f"\n---- CATEGORIA {nameCat.upper()} ----")
            print(pregunta)
            
            num = 0
            for i in opciones:
                print(f'   {num}: {i}.')
                num += 1

            print(f"\n{mensaje}")
            seleccion = int(input(": "))
            
            self.es_entero = True
        except:
            print("\n+++++ Error: Deber ser un numero! +++++")
            self.es_entero = False
        
        while seleccion < 0 or seleccion > 3 or self.es_entero == False:
            try:
                print(f"\n---- CATEGORIA {nameCat.upper()} ----")
                print(f"{pregunta}")
                
                num = 0
                for i in opciones:
                    print(f'  {num}: {i}.')
                    num += 1
                
                print(f"\nDebes {mensaje}")
                seleccion = int(input(": "))
                self.es_entero = True
            except:
                print("\n+++++ Error: Deber ser un numero! +++++")
                self.es_entero = False

        return seleccion