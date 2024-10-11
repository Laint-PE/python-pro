# Diccionario actualizado con más palabras
diccionario_moderno = {
    "CRINGE": "Literalmente pena ajena",
    "LOL": "Que es gracioso o sorprendente",
    "LMAO": "Demasiada risa la verdad",
    "ROFL": "Respuesta a una broma",
    "CREEPY": "Que da miedo",
    "AFK": "Lejos del teclado",
    "GG": "Buen juego",
    "BRB": "Ahorita vuelvo",
    "NOOB": "Novato, principiante",
}

# Saludo e instrucciones
print("¡Hola! Bienvenido al diccionario moderno.")
print("Puedes escribir palabras en mayúsculas para saber su significado.")
print("Vamos a preguntarte 5 palabras. ¡Empecemos!")

# Bucle para pedir 5 palabras
for i in range(5):
    duda = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    # Verificar si la palabra está en el diccionario
    if duda in diccionario_moderno.keys():
        print("El significado de", duda, "es:", diccionario_moderno[duda])
    else:
        print("Lo siento, no se encontró la palabra. Sorry :*v")

print("¡Gracias por usar el diccionario moderno!")
