class Categorias():
    
    #Constructor
    def __init__(self):
        self.preguntas = []

    
    # Getter and Setter
    def setPreguntas(self):
        self.preguntas = [
            [ # Primera Categoria Logica
                {
                    "pregunta":"¿Que grupo continúa en la siguiente serie: a12r,b9q,c6p?",
                    "opciones":[
                                "c5t",
                                "d3s",
                                "s5z",
                                "d3o" # Ok
                                ],
                    "respuesta": "3",
                    "nivel": "LOGICA"
                },
                {
                    "pregunta":"¿Si me encuentro en una maratón y en plena carrera mi persona le gana al segundo, en qué posición llego?",
                    "opciones":[
                                "El Primero",
                                "El Segundo",# Ok
                                "El Tercero",
                                "El Ganador"
                                ],
                    "respuesta": "1",
                    "nivel": "LOGICA"
                },
                {
                    "pregunta":"¿Qué cantidad de huesos en el cuerpo humano?",
                    "opciones":[
                                "206",
                                "106",
                                "216",
                                "226"
                                ],
                    "respuesta": "0",
                    "nivel": "LOGICA"
                },
                {                            
                    "pregunta":"¿SACO es a ASCO como 7683 es a...?",
                    "opciones":[
                                "3867",
                                "6783", # Ok
                                "3678",
                                "8376"
                                ],
                    "respuesta": "1",
                    "nivel": "LOGICA"
                },
                {
                    "pregunta":"¿Algunos meses tienen 31 días, algunos meses tienen 30 días. ¿Cuántos tienen 28 días?",
                    "opciones":[
                                "Dos",
                                "Ninguno.",
                                "Febrero", 
                                "Todos" # Ok
                                ],
                    "respuesta": "3",
                    "nivel": "LOGICA"
                }
            ],
            [ # Segunda Categoria -> Hardware
                {
                    "pregunta":"¿Qué es la placa base?",
                    "opciones":[
                                "Es un periférico de entrada.",
                                "Lugar donde se conectan los periféricos.",
                                "Es la fuente de alimentación.",
                                "Tarjeta con un gran circuito impreso."
                                ],
                    "respuesta": "3",
                    "nivel": "HARDWARE"
                },
                {
                    "pregunta":"¿Que es el hardware?",
                    "opciones":[
                                "Componentes virtuales del PC",
                                "Componentes fisicos del PC",
                                "Película de acción muy conocida",
                                "Disco duro y los archivos que contiene"
                                ],
                    "respuesta": "1",
                    "nivel": "HARDWARE"
                },
                {
                    "pregunta":"¿El puerto vga es para conectar el.. ?",
                    "opciones":[
                                "Monitor",
                                "Teclado",
                                "Memoria USB",
                                "Energia"
                                ],
                    "respuesta": "0",
                    "nivel": "HARDWARE"
                },
                {
                    "pregunta":"¿La función del Mouse es?",
                    "opciones":[
                                "La unidad de procesador.",
                                "Desplazar el cursor en la pantalla.",
                                "Mostrar la información guardada.",
                                "Almacenar información."
                            ],
                    "respuesta": "1",
                    "nivel": "HARDWARE"
                },
                {
                    "pregunta":"¿En cual componente del computador se guarda la información de manera permanente?",
                    "opciones":[
                                "Procesador",
                                "Memoria Ram",
                                "Disco Duro",
                                "Tarjeta Madre"
                                ],
                    "respuesta": "2",
                    "nivel": "HARDWARE"
                }
            ],
            [ # Tercera Categoria -> Programación
                {
                    "pregunta":"¿Que es lenguaje de alto nivel?",
                    "opciones":[
                                "Es el lenguaje de programación que entiende directamente la computadora o máquina.",
                                "Son programas cuya finalidad es 'traducir' las instrucciones enviadas a una máquina.",
                                "Son los que más se parecen al lenguaje natural, ya que se usan palabras o comandos del lenguaje humano.",# Ok
                                "Es un lenguaje Binario"
                                ],
                    "respuesta": "2",
                    "nivel": "PROGRAMACIÓN"
                },
                {
                    "pregunta":"¿Selecciona el tipo de dato referencia?",
                    "opciones":[
                                "Byte",
                                "String", # Ok
                                "Int",
                                "Float"
                                ],                          
                    "respuesta": "1",
                    "nivel": "PROGRAMACIÓN"
                },
                {
                    "pregunta":"¿Traduce el codigo mientras lo ejecuta?",
                    "opciones":[
                                "Compilador",
                                "Imperativo",
                                "Interprete", # Ok
                                "Programación Orientada a Objeto"
                                ],
                    "respuesta": "2",
                    "nivel": "PROGRAMACIÓN"
                },
                {
                    "pregunta":"¿Significado de Clase?",
                    "opciones":[
                                "Es una variable de tipo entero cuyo valor acumula cada vez que pasa por ella.",
                                "Fracciones de codigos que permiten realizar algun tipo de procedimiento especifico.",
                                "Un paradigma de programacion.",
                                "Es una plantilla para la creación de varios objetos."
                                ],
                    "respuesta": "3",
                    "nivel": "PROGRAMACIÓN"
                },
                {
                    "pregunta":"¿Cual es el lenguaje que ha revolucionado la web?",
                    "opciones":[
                                "Javascript.", # Ok
                                "Go.",
                                "Rust.",
                                "Python."
                                ],
                    "respuesta": "0",
                    "nivel": "PROGRAMACIÓN"
                } 
            ],
            [# Cuarta Categoria -> POO
                {
                    "pregunta":"¿Qué elementos crees que definen a un objeto?",
                    "opciones":[
                                "Sus cardinalidad y su tipo",
                                "Sus atributos y sus métodos",
                                "La forma en que establece comunicación e intercambia mensajes",
                                "Su interfaz y los eventos asociados"
                                ],
                    "respuesta": "1",
                    "nivel": "PROGRAMACIÓN ORIENTADA A OBJETO"
                },
                {
                    "pregunta":"¿Qué código de los siguientes tiene que ver con la herencia?",
                    "opciones":[
                                "public class Componente extends Producto",
                                "public class Componente inherit Producto",
                                "public class Componente implements Producto",
                                "public class Componente belong to Producto"
                                ],
                    "respuesta": "0",
                    "nivel": "PROGRAMACIÓN ORIENTADA A OBJETO"
                },
                {
                    "pregunta":"¿Qué significa instanciar una clase?",
                    "opciones":[
                                "Duplicar una clase",
                                "Crear un objeto a partir de la clase",
                                "Eliminar una clase",
                                "Conectar dos clases entre sí"
                                ],
                    "respuesta": "1",
                    "nivel": "PROGRAMACIÓN ORIENTADA A OBJETO"
                },
                {
                    "pregunta":"¿Qué significa sobrecargar (overload) un método?",
                    "opciones":[
                                "Crear un método con el mismo nombre pero diferentes argumentos",
                                "Editarlo para modificar su comportamiento",
                                "Cambiarle el nombre dejándolo con la misma funcionalidad",
                                "Añadirle funcionalidades a un método",
                                ],
                    "respuesta": "0",
                    "nivel": "PROGRAMACIÓN ORIENTADA A OBJETO"
                },
                {
                    "pregunta":"¿Cual no es un modificador de acceso?",
                    "opciones":[
                                "Public",
                                "Private",
                                "Static",
                                "Protected"
                                ],
                    "respuesta": "2",
                    "nivel": "PROGRAMACIÓN ORIENTADA A OBJETO"
                } 
            ],
            [# Quinta Categoria -> SQL
                {
                    "pregunta":"¿Cuál es el tipo de declaración que NO admite SQL?",
                    "opciones":[
                                "DDL",
                                "DML",
                                "DCL",
                                "XML"
                                ],
                    "respuesta": "3",
                    "nivel": "SQL"
                }, 

                {
                    "pregunta":"¿Qué es ‘join’?",
                    "opciones":[
                                "Combina filas de tablas distintas",
                                "Es una representacion virtual de varias tablas",
                                "Para organizar filas",
                                "Muestra todo lo que contiene una tabla"
                                ],
                    "respuesta": "0",
                    "nivel": "SQL"
                },
                {
                    "pregunta":"¿De que trata DDL (Data Definition Language)?",
                    "opciones":[
                                "proceso en el que accedes a la base de datos desde las formas más altas hacia las más bajas.",
                                "Ayuda a insertar, actualizar, borrar y recuperar datos de una base de datos.", # DML
                                "Permite controlar el acceso a la base de datos. Puede conceder o revocar el acceso.", # DCL
                                "Permite llevar a cabo operaciones tales como; Create, Delete, Alter" # DDL
                                ],
                    "respuesta": "3",
                    "nivel": "SQL"
                },
                {
                    "pregunta":"¿Sabes qué es una Primary Key?",
                    "opciones":[
                                "Es el proceso que define la exactitud de los datos que se almacenan en la base de datos.",
                                "Métodos para mejorar el rendimiento.",
                                "Una columna conjunto de columnas que identifican de manera única cada fila de la tabla.",
                                "Significa la inexistencia de un carácter, ya sea porque es desconocido o no está disponible."
                                ],
                    "respuesta": "2",
                    "nivel": "SQL"
                },
                {
                    "pregunta":"¿Qué Significa RDBMS ?",
                    "opciones":[
                                "procesamiento de transacciones en línea que sigue las reglas de normalización de datos",
                                "sistemas de gestión de bases de datos relacionales",
                                "es un índice que no reorganiza la tabla en el orden del índice",
                                "es una colección de registros y su información en una sola vista."
                                ],
                    "respuesta": "1",
                    "nivel": "SQL"
                } 
            ]
        ]

    def getPreguntas(self):
        return self.preguntas