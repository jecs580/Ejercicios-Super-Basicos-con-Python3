def break_words(stuff):
    """Esta funcion dividira las palabras por nosotros."""
    words = stuff.split(' ')
    return words/2

def sort_words(words):
    """Ordena las palabras alafabeticamente."""
    return sorted(words)

def print_first_word(words):
    """Imprime la primera palabra despues de eliminarla"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Imprimee la ultima palabra despues de eliminarla."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Toma un oracion completa y devuelve las palabras ordenas"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Imprime la primera y la ultima palabra de la oracion"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Ordena las palabras para despues imprimir la primera y la ultima ordenada"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)