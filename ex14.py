from sys import argv
script, user_name = argv
prompt = '> '
print(f"Hola {user_name}, Soy el script {script}.")
print("Me gustaría hacerle algunas preguntas")
print(f"¿Te caigo bien {user_name}?")
likes = input(prompt)

print(f"¿Donde vives {user_name}?")
lives = input(prompt)
print("¿Que tipo de computadora tienes?")
computer = input(prompt)
print(f"""
Muy bien, entoces dijiste "{likes}" sobre, si te caigo bien.
Vives en "{lives}". No estoy seguro de donde es eso.
tienes una computadora "{computer}". Bien.""")