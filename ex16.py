from sys import argv
script, filename = argv
aux=open(filename).read()
print(aux)
print(f"Vamos a borrar: {filename}.")
print("Si  no quieres que sucesa presiona, CTRL-C (^C).")
print("Si quieres que sucesa preciona ENTER")

input("?")

print("Abriendo el archivo...")
target = open(filename, 'w')
print("Truncando el archivo.¡Adios!")
target.truncate()

print("Ahora te voy a pedir 3 lineas")

linea1 = input("linea 1: ")
linea2 = input("linea 2: ")
linea3 = input("linea 3: ")

print("Voy a escribir esto en el archivo.")
'''ejercicio 3. acortando la escritura en una sola linea usando formatos y escapes'''
target.write(f"{linea1}\n{linea2}\n{linea3}\n")
# target.write(linea1)
# target.write("\n")
# target.write(linea2)
# target.write("\n")
# target.write(linea3)
# target.write("\n")

print("Finalmente lo cerramos")
target.close()

'''ejercicio 4.Escribimos el "w"  para especificar el modo en que queremos que se ejecute el archivo'''