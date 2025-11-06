import os
from utilidades.funciones_utiles import leer_csv, escribir_csv
from funciones.funcion_mostrar_filtrar import mostrar_y_filtrar_recursivo

BASE_DIR = "CONTINENTES"
# ============================
# Fase 4: Eliminación de Ítems
# ============================

def eliminar_item_recursivo(ruta_base, nombre_item):
    eliminado = False
    for elemento in os.listdir(ruta_base):
        ruta_actual = os.path.join(ruta_base, elemento)
        if os.path.isdir(ruta_actual):
            if eliminar_item_recursivo(ruta_actual, nombre_item):
                eliminado = True
        elif elemento.endswith(".csv"):
            registros_archivo = leer_csv(ruta_actual)
            nuevos_registros = [r for r in registros_archivo if r.get("nombre", "").lower() != nombre_item.lower()]
            if len(nuevos_registros) != len(registros_archivo):
                escribir_csv(ruta_actual, nuevos_registros, registros_archivo[0].keys())
                eliminado = True
    return eliminado

def eliminar_item():
    if not os.path.exists(BASE_DIR):
        print("No existe la estructura de datos.")
        return
    registros = mostrar_y_filtrar_recursivo(BASE_DIR)
    if not registros:
        print("No hay datos para eliminar.")
        return
    for i, reg in enumerate(registros, start=1):
        print(f"[{i}] {reg.get('nombre', 'Sin nombre')} → {reg.get('ruta')}")
    try:
        indice = int(input("\nIngrese el número del ítem a eliminar: "))
        if indice < 1 or indice > len(registros):
            print(" Índice fuera de rango.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    item = registros[indice - 1]
    confirm = input(f"¿Confirma eliminar '{item['nombre']}'? (s/n): ").lower()
    if confirm != "s":
        print("Operación cancelada.")
        return
    if eliminar_item_recursivo(BASE_DIR, item["nombre"]):
        print(f"Ítem '{item['nombre']}' eliminado correctamente.")
    else:
        print("No se encontró el ítem para eliminar.")
