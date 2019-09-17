from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copiando desde {from_file} a {to_file}")

in_file = open(from_file)
'''Obtiene todos los datos que estan dentro del archivo'''
indata = in_file.read()

print(f"El archivo de entrada es {len(indata)} bytes de longitud")

print(f"¿Existe el archivo de salida? {exists(to_file)}")
print("Listo, presione ENTER para continuar, CTRL-C para abortar.")
input()
'''Se crea el archivo y lo ejecutamos en modo de escritura'''
out_file = open(to_file, 'w')
out_file.write(indata)

print("Muy bien, todo listo")

out_file.close()
in_file.close()