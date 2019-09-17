print("Practiquemos todo")
print('Necesitarias saber acerca de los escapes, Que hacen:')
print('\n Lineas nuevas y \t pestañas.')

poema = """
\tEl mundo estancador
con logica facilmente planteada
no puede diseminar \n las necesidades de amor
ni prender la pasion desde la intuicion
y requiere una expresion
\n\tDonde no hay ninguno.
"""

print("--------------")
print(poema)
print("--------------")


cinco = 10 - 2 + 3 - 6
print(f"Esto deberia ser: {cinco}")

def formula_secreta(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = formula_secreta(start_point)

print("Con un punto de inicio: {}".format(start_point))
print(f"Tendriamos {beans} frijoles, {jars} frascos, y {crates} cajas.")

start_point = start_point / 10

print("Tambien podemos hacerlo de esta manera:")
formula = formula_secreta(start_point)
"""Lista de cadenas devueltas de la funcion"""
print("Tendriamos {} frijoles, {} frascos, y {} cajas.".format(*formula))