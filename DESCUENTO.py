#crear un programa que calcule el descuento en compras en función del monto total de la compra y mostrar el monto final a pagar.
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (int, optional): El porcentaje de descuento (default es 10%).

    Retorna:
    float: El monto del descuento calculado.
    """
    descuento = (monto_total / 100) * porcentaje_descuento
    return descuento
# Llamada 1: Solo se proporciona el monto total de la compra
monto_total = 100
descuento = calcular_descuento(monto_total)
monto_final = monto_total - descuento
print(f"Monto total: {monto_total}, Descuento: {descuento}, Monto final: {monto_final}")

# Llamada 2: Se proporciona el monto total de la compra y el porcentaje de descuento
monto_total = 200
porcentaje_descuento = 10
descuento = calcular_descuento(monto_total, porcentaje_descuento)
monto_final = monto_total - descuento
print(f"Monto total: {monto_total}, Descuento: {descuento}, Monto final: {monto_final}")