import os
from utilidades.funciones_utiles import leer_csv, escribir_csv
from funciones.funcion_mostrar_filtrar import mostrar_y_filtrar_recursivo

BASE_DIR = "CONTINENTES"

def modificar_item_recursivo(ruta_base, nombre_item, atributo, nuevo_valor):
    """
    Recorre todo el árbol a partir de ruta_base y modifica todas las
    coincidencias del nombre_item en cualquier CSV. Devuelve la cantidad
    de archivos (CSV) que fueron actualizados.
    """
    modificaciones = 0
    try:
        entradas = os.listdir(ruta_base)
    except FileNotFoundError:
        return 0
    for elemento in entradas:
        ruta_actual = os.path.join(ruta_base, elemento)
        if os.path.isdir(ruta_actual):
            # sumar las modificaciones que se produzcan en subdirectorios
            modificaciones += modificar_item_recursivo(ruta_actual, nombre_item, atributo, nuevo_valor)
        elif elemento.lower().endswith(".csv"):
            registros_archivo = leer_csv(ruta_actual)
            if not registros_archivo:
                continue
            actualizado = False
            # Actualizar todas las filas que coincidan en ese archivo
            for fila in registros_archivo:
                if fila.get("nombre", "").lower() == nombre_item.lower():
                    # convertir a string para escribir en CSV; mantener consistencia
                    fila[atributo] = str(nuevo_valor)
                    actualizado = True
            if actualizado:
                # asegurar una lista de fieldnames ordenada
                fieldnames = list(registros_archivo[0].keys())
                escribir_csv(ruta_actual, registros_archivo, fieldnames)
                modificaciones += 1
    return modificaciones

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
        # permitir crear atributos nuevos opcionalmente:
        confirmar = input(f"El atributo '{atributo}' no existe en el registro. ¿Desea crearlo igualmente? (s/n): ").lower()
        if confirmar != "s":
            print("Atributo inválido. Operación cancelada.")
            return
    nuevo_valor = input(f"Ingrese nuevo valor para {atributo}: ").strip()
    if atributo in ["poblacion", "superficie"]:
        try:
            nuevo_valor = float(nuevo_valor)
        except ValueError:
            print("Debe ingresar un valor numérico válido.")
            return
    # ahora pedimos la cantidad de archivos modificados
    cantidad_modificados = modificar_item_recursivo(BASE_DIR, item["nombre"], atributo, nuevo_valor)
    if cantidad_modificados > 0:
        print(f"Ítem '{item['nombre']}' modificado correctamente en {cantidad_modificados} archivo(s).")
    else:
        print("No se pudo modificar el ítem (no se encontraron coincidencias en los CSV).")
