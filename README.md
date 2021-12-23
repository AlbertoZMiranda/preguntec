PREGUNTEC
Juego de preguntas con diferentes opciones con única respuesta,
el cual está orientado a la tecnología de hay el nombre:
(pregun)tas (tec)nologica: PREGUNTEC

Este juego funciona en la terminal, consta de 5 rondas donde cada ronda presentará una pregunta de manera aleatoria, 
donde debes escribir el número que se encuentra a la izquierda de la pregunta que creas correcta, hasta llegar a la quinta ronda.
vas a ganar un premio cada vez que acierte y se te va a ir mejorando el premio a medida que vas ganando, 
hasta que llegue al premio mayor una super laptop workstation.

INSTRUCCIONES:
* Descargamos los archivos desde github. Creamos una carpeta la cual deseamos que aloje todos los archivos.

* Dejamos el link donde puede descargar el juego: https://github.com/AlbertoZMiranda/preguntec

OBSERVACIÓN: la carpeta modulos/__pycache__/ se crea después de ejecutar por primera vez el programa. 
  si descargas puedes borrar la carpeta (__pycache__/), y después ejecutar el archivo ‘main.py’, para que tu sistema cree su propia carpeta.

* Si estas en windows este programa se creó con la versión de python 3.8, se puede ejecutar en la terminal con el comando python main.py
* En linux para que pueda ejecutarse con normalidad el programa, ejecuta el archivo main.py con el siguiente comando: python3 main.py
* Iniciar juego: ejecutamos el archivo main.py en la terminal, muestra un mensaje de bienvenida y debes ingresar tu nombre.
* Tenemos una pregunta que se hace antes de comenzar cada ronda, La cual es si desea jugar o salir de juego, 
  si deseas jugar marca (1), sino (cualquier otra tecla)

OBSERVACIÓN: La sección de preguntas cuenta con un validador de datos ingresado: el solo va permitir número del cero(0) al tres(3), 
  los cuales hacen referencias a las diferentes opciones de respuestas, si no cumples esta condición se repetirá hasta que eligas 
  la opcion dentro de este rango. no acepta letras, ni números menores de cero(0), ni números mayores a tres(3)

* Estando en preguntas si eliges la opción correcta, se sumará un punto cada vez que aciertes,  y te llevara a una nueva ronda de pregunta, 
  la cual cual mostrará en la parte de arriba cuál es su categoría, el premio va mejorando hasta llegar a una super laptop workstation.
* Si te equivocas en responder el juego se termina y no tienes ningún punto ni premio.
* Tienes opción de salir en alguna ronda y te quedas con los puntos y el premio de la ronda ganada.
* Contamos con los archivos
     main.py
    /modulos/
    /modulos/__init__.py
    /modulos/ronda.py
    /modulos/categoria.py
    /modulos/jugador.py
* main.py: Es el archivo que se va a ejecutar en la terminal.
* /modulos/: es la libreria que agrupa los demas archivo
* /modulos/__init__.py: para que python reconozca a la carpeta modulos como librería se debe crear el archivo __init__.py no se le escribe nada adentro.
* /módulos/ronda.py: es donde se hará las operaciones y/o métodos que necesita el programa para funcionar, de hay se seran llamador por main.py
* /modulos/categoria.py: guarda todas las preguntas, opciones y nombre de categorías.
* /modulos/jugador.py: guarda la información del nombre del jugador, los puntos y premio que el jugador consigue. 
