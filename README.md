#def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto de descuento basado en el monto total de la compra y un porcentaje de descuento.
    :param monto_total: float - Monto total de la compra
    :param porcentaje_descuento: float - Porcentaje de descuento (por defecto 10%)
    :return: float - Monto del descuento calculado
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Ejemplo de uso
monto1 = 200
monto2 = 500
porcentaje_descuento_custom = 15

descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, porcentaje_descuento_custom)

print(f"Monto total: ${monto1} - Descuento aplicado: ${descuento1} - Monto final a pagar: ${monto1 - descuento1}")
print(f"Monto total: ${monto2} - Descuento aplicado ({porcentaje_descuento_custom}%): ${descuento2} - Monto final a pagar: ${monto2 - descuento2}")