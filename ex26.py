
# from sys import argv
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
#Le falta cerrar el parentesis de la impresion
print("How much do you weigh?", end=' ')
weight = input()
# No tiene de declarada la variable height en ningun lado
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# No tiene importada la libreria para llamar al metodo
script, filename = argv

# No esta correcto el nombre al que hace referencia al archivo
txt = open(filenme)

print("Here's your file {filename}:")
# No esta correcta el nombre de la variable al que hace referencia le falta una "t"
print(tx.read())

print("Type the filename again:")
file_again = input("> ")

# No puede ejectar el metodo "open" a una variable que almacena "input"
txt_again = open(file_again)

# La forma para llamar al metodo read no esta correcta se coloca un punto en vez del guion bajo
print(txt_again_read())

# La impresion no es incorrecta por que utilza palabras que llevan apostrofes, para que no salga el error, se sugiere que utulice \ antes de la comiila.
print('Let's practice everything.')

# Error al querer utilizar saltos de linea con comillas simples, si hacer uso de los saltos de linea se recomienda utlizar las tiples comillas simples o dobles
print('You\'d need to know \'bout escapes 
      with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# Se debe colocar comillas al inicio y al final de cada oracion que coloquemos
print("--------------)

# Error probocado por la anterior linea
print(poem)

# Se debe colocar comillas al inicio y al final de cada oracion que coloquemos
print(--------------")

# Las operaciones matematicas acompañas de de pares de numeros
five = 10 - 2 + 3 - 

# Falta cerrar parentesis de cierre
print(f"This should be five: {five}"

# Falta cierre de la cabecera de la funcion con los dos puntos ":"
def secret_formula(started)
    # No definida la variable started
    jelly_beans = started * 500
    jars = jelly_beans / 1000

    # No tiene un operador que una la variable con el numero
    crates = jars  100
    # Error provocado por la linea anterior
    return jelly_beans, jars, crates

# Error provocado por no cerrar la cabecera de la funcion anterior
start_point = 10000

# Error provocado por el error en la linea anterior
beans, jars = secret_formula(start_point)

# Error provocador provocado por la anterior-anterior linea
print("With a starting point of: {}".format(start_point))

# La variable crates es una variable local de la funcion secret_formula, no podemos llamarla de manera global
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")

# Error por que la funcion no fue creada correctamente 
formula = secret_formula(startpoint)

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cates = 30
dogs = 15

# la variable cats no esta definida, quiza se referia a cates
if people < cats:
    print "Too many cats! The world is doomed!"

# la variable cats no esta definida, quiza se referia a cates
if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

# Falta los dos puntos ":" para cerrar la cabecera de la condicional
if people > dogs
    print("The world is dry!")
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs
# Falta cerrar la comilla al final de la oracion
    print("People are less than or equal to dogs.)

# Error para condicion de igualdad, es necesario colocar dos signos de igualdad para la comparacion
if people = dogs:
    print("People are dogs.")
