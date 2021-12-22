class Jugador():
    
    # Constructor
    def __init__(self):
        self.nombre = ""
        self.puntos = 0
        self.premio = ""
        self.info = ""

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
        self.premio = ['No hay premio', 'Televisor 24', 'Portatil 500 GB 4GB Ram', 'Iphone 11', 'Pulsar 200cc','Portatil t15 2da generacion']
    def getPremio(self):
        return self.premio[self.puntos]

    # Metodo
    def infoJugador(self, nombre, puntos, premio):
        self.info = ""
        self.setNombre = nombre
        self.premio = premio
        self.puntos = puntos

        self.info = f" Nombre: {self.setNombre} \n Puntos: {self.puntos} \nPremios: {self.premio}"         
        return self.info
    