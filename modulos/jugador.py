class Jugador():
    
    # Constructor
    def __init__(self):
        self.nombre = ""
        self.puntos = 0
        self.premio = ""
        self.info = ""
        self.acumPremios = []

    # Getter and Setter
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    
    def setPuntos(self, puntos):
        self.puntos = puntos
    def getPuntos(self):
        return self.puntos

    def setPremio(self):
        self.premio = ['No hay premio','Un Perfume Salvaje', 'Audifonos Senses', 'Un Portatil 500 GB 4GB Ram', 'Un Iphone 11','Un Portatil Lenovo ThinkPad t15 2da generacion']
    def getPremio(self):
        return self.premio[self.puntos]
           

    # Metodo
    def infoJugador(self, nombre, puntos, premio, msgF):
        self.info = ""
        self.setNombre = nombre
        self.premio = premio
        self.puntos = puntos

        msg = ""
        if self.puntos == 5:
            msg = "Terminaste Todas Las rondas: Felicitaciones"

        self.info = f"\n--- TERMINO EL JUEGO {msg.upper()}---\n Nombre: {self.setNombre} \n Puntos: {self.puntos} \nPremios: {self.premio}"         
        return self.info
    