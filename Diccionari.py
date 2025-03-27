# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Johnn Verano", # Nombre ficticio de la persona
    "edad": 30,
    "ciudad": "Shushufindi",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito" # Se cambia la ciudad a otra diferente

# Agregar una nueva clave-valor al diccionario (ya existe "profesion", pero si fuera nueva, se haría así)
informacion_personal["ocupacion"] = "Desarrollador de Software" # Se agrega una nueva clave con la ocupación

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-789" # Se agrega un número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)  # Se elimina la clave "edad" para que no esté en la información

# Imprimir el diccionario final
print(informacion_personal) # Se muestra el diccionario actualizado
