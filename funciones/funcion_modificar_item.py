import os
from utilidades.funciones_utiles import leer_csv, escribir_csv
from funciones.funcion_mostrar_filtrar import mostrar_y_filtrar_recursivo

BASE_DIR = "CONTINENTES"
# ===========================================
# Fase 3: Modificación y Eliminación de Ítems
# ===========================================
def modificar_item_recursivo(ruta_base, nombre_item, atributo, nuevo_valor):
    for elemento in os.listdir(ruta_base):
        ruta_actual = os.path.join(ruta_base, elemento)
        if os.path.isdir(ruta_actual):
            if modificar_item_recursivo(ruta_actual, nombre_item, atributo, nuevo_valor):
                return True
        elif elemento.endswith(".csv"):
            registros_archivo = leer_csv(ruta_actual)
            actualizado = False
            for fila in registros_archivo:
                if fila.get("nombre", "").lower() == nombre_item.lower():
                    fila[atributo] = str(nuevo_valor)
                    actualizado = True
            if actualizado:
                escribir_csv(ruta_actual, registros_archivo, registros_archivo[0].keys())
                return True
    return False

def modificar_item():
    if not os.path.exists(BASE_DIR):
        print("No existe la estructura de datos.")
        return
    registros = mostrar_y_filtrar_recursivo(BASE_DIR)
    if not registros:
        print("No hay datos para modificar.")
        return
    for i, reg in enumerate(registros, start=1):
        print(f"[{i}] {reg.get('nombre', 'Sin nombre')} → {reg.get('ruta')}")
    try:
        indice = int(input("\nIngrese el número del ítem a modificar: "))
        if indice < 1 or indice > len(registros):
            print("Índice fuera de rango.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    item = registros[indice - 1]
    atributo = input("Ingrese atributo a modificar: ").strip().lower()
    if atributo not in item:
        print("Atributo inválido.")
        return
    nuevo_valor = input(f"Ingrese nuevo valor para {atributo}: ").strip()
    if atributo in ["poblacion", "superficie"]:
        nuevo_valor = float(nuevo_valor)
    if modificar_item_recursivo(BASE_DIR, item["nombre"], atributo, nuevo_valor):
        print(f"Ítem '{item['nombre']}' modificado correctamente.")
    else:
        print("No se pudo modificar el ítem.")
