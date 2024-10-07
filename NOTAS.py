#Creación del archivo my_notes.txt y escritura de notas personales
with open("my_notes.txt", "w") as file:
    file.write("Nota 1: Comprar leche en el supermercado\n")
    file.write("Nota 2: Llamar a mi amigo para felicitarlo por su graduacion \n")
    file.write("Nota 3: Estudiar para el examen de programacion mañana\n")
#Apertura del archivo my_notes.txt y lectura del contenido
with open("my_notes.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()