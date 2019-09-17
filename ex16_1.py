"""Script para interactuar con el usuario al leer el archivo ex16_sample.txt"""
from sys import argv
script, filename = argv
print(f"Vamos a leer : {filename}.")
print("Si  no quieres que sucesa presiona, CTRL-C (^C).")
print("Si quieres que sucesa preciona ENTER")

input("?")

print("Abriendo el archivo...")
target = open(filename, 'r')
print("Leyendo la primera linea del archivo")
print(target.readline())
print("Si quieres leer la siguiente linea preciona ENTER")
input("?")

print("Leyendo la segunda linea del archivo")
print(target.readline())
print("Si quieres leer otra linea preciona ENTER")
input("?")
print(target.readline())
print("Finalmente lo cerramos")
target.close()