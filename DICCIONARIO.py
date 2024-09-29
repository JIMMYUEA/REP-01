#Creación del diccionario
informacion_personal = {
    "Nombre": "Jimmy Proaño",
    "Edad": 23,
    "Ciudad": "Quito",
    "Profesion": "Ingeniero"
}
#Accediendo y modificando el valor asociado con la clave "ciudad"
informacion_personal["Ciudad"] = "Riobamba"
#Agregando una nueva clave-valor al diccionario
informacion_personal["Profesion_Actual"] = "Auxiliar"
#Verificando si la clave "Teléfono" existe en el diccionario caso contrario colocar uno ficticio
if "telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0987694378"
    #Eliminando la clave "edad" del diccionario
    del informacion_personal["Edad"]

print(informacion_personal)