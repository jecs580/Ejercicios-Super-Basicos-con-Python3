def add(a, b):
    print(f"Sumando {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Restando {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplicando {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividiendo {a} / {b}")
    return a / b


print("Hagamos algo de matematicas con solo funciones!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Edad: {age}, Altura: {height}, Peso: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Aqui hay un rompecabezas")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
'''Formula real'''
what1= age+(height-(weight*(iq/2)))

print("Eso se convierte en: ", what)
print("Formula real",what1)

'''Ejercicio 4, escribiendo una formula usando las funciones'''
r=2
pi= 3.1416
perimetro_circulo=multiply(multiply(2,r),pi)
print(f"Perimetro del circulo: {perimetro_circulo}")