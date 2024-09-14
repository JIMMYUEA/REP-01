def calcular_promedio_temperaturas(temperaturas_quito, temperaturas_latacunga, temperaturas_machala):

  # CANTIDAD DE SEMANAS
  if len(temperaturas_quito) != 4 or len(temperaturas_latacunga) != 4 or len(temperaturas_machala) != 4:
    raise ValueError

  # CALCULO DE PROMEDIOS
  promedio_quito = sum(temperaturas_quito) / len(temperaturas_quito)
  promedio_latacunga = sum(temperaturas_latacunga) / len(temperaturas_latacunga)
  promedio_Machala = sum(temperaturas_Machala) / len(temperaturas_Machala)

  # RETORNO DE RESULTADOS
  return {
    "Quito": promedio_quito,
    "latacunga": promedio_latacunga,
    "Machala": promedio_Machala
  }

# TEMPERATURAS
temperaturas_quito = [25, 27, 26, 28]
temperaturas_latacunga = [21, 26, 23, 24]
temperaturas_Machala = [29, 32, 28, 34]

# IMPRIME PROMEDIO DE TEMPERATURA DURANTE 4 SEMANAS
promedios = calcular_promedio_temperaturas(temperaturas_quito, temperaturas_latacunga, temperaturas_Machala)
print(promedios)