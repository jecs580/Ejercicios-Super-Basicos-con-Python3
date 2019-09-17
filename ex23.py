
import sys
script, input_encoding, error = sys.argv
def main(language_file, encoding, errors):
    line = language_file.readline()
    
    '''Probamos si la linea tiene algo, vale decir que si esta vacia devolvera False'''
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
        ''''Metodo que nos devuelve la linea eliminando el "\n" (Al final y al comienzo)'''
        next_lang = line.strip()
        ''''Codificamos la cadena en bytes'''
        raw_bytes = next_lang.encode(encoding, errors=errors)
        ''''Decodificamos los bytes'''
        cooked_string = raw_bytes.decode(encoding, errors=errors)

        print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")
main(languages, input_encoding, error)

# Nro 2
''''Cuando le mandamos una codificacion que no existe python lo nota y nos devuelve el valor: 
    "Codificacion desconocida"'''