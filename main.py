import os
import csv
from funciones.funcion_creacion_jerarquica import *
from funciones.funcion_mostrar_filtrar import mostrar_y_filtrar
from funciones.funcion_modificar_item import modificar_item
from funciones.funcion_eliminar_item import eliminar_item
from funciones.funcion_estadisticas_ordenamiento import estadisticas_y_ordenamiento
from utilidades.funciones_utiles import crear_directorio


# ===============================
# Menú
# ===============================
menu = True
while menu:
    crear_directorio(BASE_DIR)
    print("\n" + "-"*13 + " Menu " + "-"*13)
    print("1) Crear estructura jerárquica con datos")
    print("2) Mostrar ítems totales y filtrado (lectura global)")
    print("3) Modificar un ítem existente (Update)")
    print("4) Eliminar un ítem existente (Delete)")
    print("5) Estadísticas y ordenamiento global")
    
    print("• Cualquier otro número para salir")
    try:
        seleccion = int(input("Ingrese una opción: ").strip())
        match seleccion:
            case 1:
                creacion_jerarquica()
            case 2:
                mostrar_y_filtrar()
            case 3:
                modificar_item()
            case 4:
                eliminar_item()
            case 5:
                estadisticas_y_ordenamiento()
            case _:
                print("Saliendo del menú...")
                menu = False
    except ValueError:
        print("Incorrecto. Por favor, solo ingrese números.")


# Construcción de estructura anidada para operaciones recursivas

# Utilidades de FS y CSV


# Reuso de función recursiva para crear estructura en disco desde nodo raíz

