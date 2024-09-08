# Crear matriz 3D para almacenar temperaturas diarias
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

temperaturas = [[[20, 22, 25, 28, 30, 32, 35],  # Ciudad A, Semana 1
                 [18, 20, 22, 25, 28, 30, 32],  # Ciudad A, Semana 2
                 [22, 25, 28, 30, 32, 35, 38],  # Ciudad A, Semana 3
                 [25, 28, 30, 32, 35, 38, 40]],  # Ciudad A, Semana 4

                [[15, 18, 20, 22, 25, 28, 30],  # Ciudad B, Semana 1
                 [12, 15, 18, 20, 22, 25, 28],  # Ciudad B, Semana 2
                 [18, 20, 22, 25, 28, 30, 32],  # Ciudad B, Semana 3
                 [20, 22, 25, 28, 30, 32, 35]],  # Ciudad B, Semana 4

                [[10, 12, 15, 18, 20, 22, 25],  # Ciudad C, Semana 1
                 [8, 10, 12, 15, 18, 20, 22],  # Ciudad C, Semana 2
                 [12, 15, 18, 20, 22, 25, 28],  # Ciudad C, Semana 3
                 [15, 18, 20, 22, 25, 28, 30]]]  # Ciudad C, Semana 4

# Calcular promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    for j, semana in enumerate(semanas):
        suma_temperaturas = 0
        for k, dia in enumerate(dias_semana):
            suma_temperaturas += temperaturas[i][j][k]
        promedio_temperatura = suma_temperaturas / len(dias_semana)
        print(f"Promedio de temperatura en {ciudad} durante la {semana}: {promedio_temperatura:.2f}°C")