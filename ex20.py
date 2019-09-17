from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    '''Mueve el puntero al byte inicial del documento'''
    f.seek(0)

def print_a_line(line_count, f):    
    print(line_count, f.readline())

current_file = open(input_file)

print("Primero imprimimos todo el archivo:\n")
print_all(current_file)

print("\nAhora rebobinemos con una cita.")

rewind(current_file)

print("Vamos a imprimir 3 lineas:\n")

'''La variable current_line como un indice de las lineas'''
current_line = 1
print_a_line(current_line, current_file)
'''Es un contracción para la suma su equivalente es: current_line = current_line + 1'''
# current_line = current_line + 1
current_line+=1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line+=1
print_a_line(current_line, current_file)