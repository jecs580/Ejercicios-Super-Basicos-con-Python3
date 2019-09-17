# Este es como tus scripts con argv
def print_two(*args):
    arg1, arg2 ,arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, args3: {arg3}")
# ese *args en realidad no tiene setido, solo podemos hacer esto
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

 # Esto solo toma un argumento
def print_one(arg1):
    print(f"arg1: {arg1}")

# Esto no toma un argumento
def print_none():
    print("No tengo nada")


print_two("Zed","Shaw","todo")
print_two_again("Zed","Shaw")
print_one("Primero!")
print_none()