# Matriz de horas trabajadas por recurso
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 8, 7, 8],
    ["Luis", 9, 10, 9, 8, 10],
    ["María", 8, 8, 8, 8, 8]
]

# Función para calcular total y clasificación
def calcular_horas(recurso):
    nombre = recurso[0]
    horas = recurso[1:]

    total_horas = sum(horas)

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion


# Mostrar resultados
print("REPORTE SEMANAL DE HORAS\n")

for recurso in recursos:
    nombre, total, clasificacion = calcular_horas(recurso)

    print(f"Recurso: {nombre}")
    print(f"Total de horas: {total}")
    print(f"Clasificación: {clasificacion}")
    print("-" * 30)