def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"Tienes {cheese_count} quesos!")
    print(f"Tienes {boxes_of_crackers} cajas de galletas!")
    print("¡Hombre, eso es suficiente para una fiesta!")
    print("Consigue una manta.\n")

# 1
print("Podemos dar los numeros en la funcion directamente:")
cheese_and_crackers(20, 30)

# 2
print("O, podemos usar variables de nuestro script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 3
print("Podemos hacer operaciones matematicas en la llamada de la funcion:")
cheese_and_crackers(10 + 20, 5 + 6)

# 4
print("Y podemos combinar las variables con operaciones matematicas:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

'''Aumentando mas combinaciones'''
# 5
print("Probando con el input")
cheese_and_crackers(input("nro de quesos : "),input("nro de galletas :"))
# 6
print("Probando el input con operadores matematicos")
cheese_and_crackers(int(input("nro de quesos: "))**2, int(input("nro de galletas: "))**2)
# 7
print("Probando el input con operadores matematicos y numeros")
cheese_and_crackers(int(input("nro de quesos: "))+5, int(input("nro de galletas: "))+50)
# 8
print("Probando el input con operadores matematicos y con las variables declaradas")
cheese_and_crackers(int(input("nro de quesos: "))+amount_of_cheese, int(input("nro de galletas: "))+amount_of_crackers)
# 9
print("Probando el input con operadores matemaaticos,con las variables declaradas y con numeros directos")
cheese_and_crackers(int(input("nro de quesos: "))+amount_of_cheese*2, int(input("nro de galletas: "))+amount_of_crackers*2)
