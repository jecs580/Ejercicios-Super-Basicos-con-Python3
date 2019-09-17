import sys 
script, encoding, error, from_file, to_file = sys.argv #added from_file and to_file


def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        next_lang = line.strip()
        raw_bytes = next_lang.encode(encoding, errors=errors) #DBES - decode bytes, encode strings. What does encode() do? It encodes the string from next_lang into bytes
        raw_bytes_file = open(to_file, 'a') #APPEND MODE!!!!!!! saving raw_bytes to to_file which was given in terminal as an argument...
        raw_bytes_file.write(str(raw_bytes)) #must apparently be a string according to the error message
        '''target.write(f"{linea1}\n{linea2}\n{linea3}\n")'''
        raw_bytes_file.write("\n") #if I omit this all the utf-8 stuff is in the same line = no newlines for readability
        print("This should be written to the file defined in the to_file argument: ", raw_bytes)
        return main(language_file, encoding, errors)
    
    
languages = open(from_file, encoding="utf-8")

main(languages, encoding, error)
#in terminal: python3 ex23_txt_conversion.py utf-8 strict languages.txt lang_bytes_only.txt