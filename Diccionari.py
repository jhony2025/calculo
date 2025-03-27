# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Johnny Vera",
    "edad": 30,
    "ciudad": "Shushufindi",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor al diccionario (ya existe "profesion", pero si fuera nueva, se haría así)
informacion_personal["ocupacion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-789"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)  # Usamos None para evitar error si la clave no existe

# Imprimir el diccionario final
print(informacion_personal)