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

    def setPremio(self, premio):
        self.premio = premio
    def getPremio(self):
        return self.premio

    # Metodo
    def infoJugador(self, nombre, puntos, premio):
        self.info = f"""
        Premios: {self.premio}
         Nombre: {self.setNombre}
         Puntos: {self.puntos}
        """
    
    