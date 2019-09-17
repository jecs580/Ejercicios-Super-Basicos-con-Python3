'''importamos la biblioteca argv para el manejo de argumentos'''
from sys import argv
''' Cantidad de variables que introduciremos al principio y q seran leidos por argv'''
script, filename = argv
''' Abrimos el archivo txt que mandamos su nombre como argumento al principio'''
txt = open(filename)
'''Imprimimos el nombre del archivo'''
print(f"Aqui esta tu archivo {filename}:")
print(txt.read())
""" ejercicio 7 cerrando los archivos despues de usarlos"""
txt.close()
# comentamos la linea 11 y 14 para el ejecicio 4 
# print("Escriba el nombre del archivo nuevamente:")
file_again = input("> ")
txt_again = open(file_again)
# print(txt_again.read())
""" ejercicio 7 cerrando los archivos despues de usarlos"""
txt_again.close()
"""traduccion de la documentacion de "open"
abierto (archivo, modo = 'r', almacenamiento en búfer = -1, codificación = Ninguno, errores = Ninguno, nueva línea = Ninguno, closefd = Verdadero, abridor = Ninguno)
    Abra el archivo y devuelva una secuencia. Eleve OSError en caso de falla.

    el archivo es una cadena de texto o byte que da el nombre (y la ruta
    si el archivo no está en el directorio de trabajo actual) del archivo a
    abrirse o un descriptor de archivo entero del archivo a ser
    envuelto. (Si se proporciona un descriptor de archivo, se cierra cuando el
    el objeto de E / S devuelto está cerrado, a menos que closefd esté establecido en False).

    mode es una cadena opcional que especifica el modo en que el archivo
    está abierto. El valor predeterminado es 'r', que significa abierto para leer en el texto
    modo. Otros valores comunes son 'w' para escribir (truncando el archivo si
    ya existe), 'x' para crear y escribir en un nuevo archivo, y
    'a' para agregar (que en algunos sistemas Unix, significa que todas las escrituras
    agregar al final del archivo, independientemente de la posición de búsqueda actual).
    En modo texto, si no se especifica la codificación, la codificación utilizada es la plataforma
    dependiente: se llama a locale.getpreferredencoding (False) para obtener el
    codificación local actual. (Para leer y escribir bytes sin procesar use binary
    modo y deje la codificación sin especificar.) Los modos disponibles son:

    ========= ========================================= ======================
    Significado del personaje
    --------- ----------------------------------------- ----------------------
    'r' abierto para lectura (predeterminado)
    'w' abierto para escritura, truncando el archivo primero
    'x' crea un nuevo archivo y ábrelo para escribir
    'a' abierto para escritura, agregando al final del archivo si existe
    modo binario 'b'
    modo de texto 't' (predeterminado)
    '+' abre un archivo de disco para actualizar (lectura y escritura)
    Modo de nueva línea universal 'U' (en desuso)
    ========= ========================================= ======================

    El modo predeterminado es 'rt' (abierto para leer texto). Para binario aleatorio
    acceso, el modo 'w + b' se abre y trunca el archivo a 0 bytes, mientras que
    'r + b' abre el archivo sin truncamiento. El modo 'x' implica 'w' y
    genera un `FileExistsError` si el archivo ya existe.

    Python distingue entre archivos abiertos en modo binario y de texto,
    incluso cuando el sistema operativo subyacente no lo hace. Archivos abiertos en
    el modo binario (agregando 'b' al argumento de modo) devuelve el contenido como
    bytes de objetos sin ninguna decodificación. En modo texto (por defecto, o cuando
    't' se agrega al argumento de modo), el contenido del archivo es
    devuelto como cadenas, habiéndose descodificado primero los bytes utilizando un
    codificación dependiente de la plataforma o utilizando la codificación especificada si se proporciona.

    El modo 'U' está en desuso y generará una excepción en futuras versiones
    de pitón. No tiene ningún efecto en Python 3. Use newline para controlar
    modo universal de nuevas líneas.

    El almacenamiento en búfer es un número entero opcional que se utiliza para establecer la política de almacenamiento en búfer.
    Pase 0 para desactivar el almacenamiento en búfer (solo permitido en modo binario), 1 para seleccionar
    almacenamiento en línea (solo utilizable en modo texto) y un entero> 1 para indicar
    El tamaño de un búfer de fragmentos de tamaño fijo. Cuando no hay argumento de almacenamiento en búfer
    dada, la política de almacenamiento en búfer predeterminada funciona de la siguiente manera:

    * Los archivos binarios están almacenados en fragmentos de tamaño fijo; el tamaño del búfer
      se elige usando una heurística tratando de determinar el dispositivo subyacente
      "tamaño de bloque" y retrocediendo en `io.DEFAULT_BUFFER_SIZE`.
      En muchos sistemas, el búfer normalmente tendrá una longitud de 4096 u 8192 bytes.

    * Archivos de texto "interactivos" (archivos para los que isatty () devuelve True)
      usar el buffering de línea. Otros archivos de texto usan la política descrita anteriormente
      para archivos binarios

    codificación es el nombre de la codificación utilizada para decodificar o codificar
    expediente. Esto solo debe usarse en modo texto. La codificación predeterminada es
    depende de la plataforma, pero cualquier codificación compatible con Python puede ser
    pasado Consulte el módulo de códecs para ver la lista de codificaciones compatibles.

    errores es una cadena opcional que especifica cómo deben codificarse los errores
    manejarse --- este argumento no debe usarse en modo binario. Pasar
    'estricto' para generar una excepción ValueError si hay un error de codificación
    (el valor predeterminado de Ninguno tiene el mismo efecto), o pase 'ignorar' para ignorar
    errores (Tenga en cuenta que ignorar los errores de codificación puede conducir a la pérdida de datos).
    Consulte la documentación de codecs.register o ejecute 'help (codecs.Codec)'
    para obtener una lista de las cadenas de error de codificación permitidas.

    nueva línea controla cómo funciona la nueva línea universal (solo se aplica al texto
    modo). Puede ser Ninguno, '', '\ n', '\ r' y '\ r \ n'. Funciona como
    sigue:

    * En la entrada, si la nueva línea es Ninguna, el modo de nueva línea universal es
      habilitado Las líneas en la entrada pueden terminar en '\ n', '\ r' o '\ r \ n', y
      estos se traducen a '\ n' antes de volver a
      llamador. Si es '', el modo de nueva línea universal está habilitado, pero la línea
      las terminaciones se devuelven a la persona que llama sin traducir. Si tiene alguno de
      el otro legal
"""