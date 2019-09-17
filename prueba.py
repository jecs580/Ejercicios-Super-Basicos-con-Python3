from sys import argv
script, filename = argv
print(f"Aqui esta tu archivo {filename}:")
with open(filename,"r") as file1:
    '''Vuelve las lineas de todo el archivo en una lista'''
    data=file1.readlines(6)
    print(data)
# print (file1.closed)
# print(data)
# print(type(data))