import os
from utilidades.funciones_utiles import leer_csv, pedir_texto

BASE_DIR = "CONTINENTES"
# ================================
# Fase 2: Lectura Global Recursiva
# ================================
def mostrar_y_filtrar_recursivo(ruta_base, atributo=None, valor=None, registros=None):
    if registros is None:
        registros = []
    for elemento in os.listdir(ruta_base):
        ruta_actual = os.path.join(ruta_base, elemento)
        if os.path.isdir(ruta_actual):
            mostrar_y_filtrar_recursivo(ruta_actual, atributo, valor, registros)
        elif elemento.endswith(".csv"):
            filas = leer_csv(ruta_actual)
            for fila in filas:
                fila["ruta"] = ruta_actual
                if atributo and valor:
                    if str(fila.get(atributo, "")).lower() == valor.lower():
                        registros.append(fila)
                else:
                    registros.append(fila)
    return registros

def mostrar_y_filtrar():
    if not os.path.exists(BASE_DIR):
        print("No existe la estructura de datos.")
        return
    print("\nLeyendo todos los archivos CSV...")
    registros = mostrar_y_filtrar_recursivo(BASE_DIR)
    if not registros:
        print("No se encontraron datos en la jerarquía.")
        return
    for i, reg in enumerate(registros, start=1):
        print(f"[{i}] {reg.get('nombre', 'Sin nombre')} → Ruta: {reg['ruta']}")
    print("\n--- FILTRADO ---")
    atributo = pedir_texto("Ingrese atributo a filtrar (nombre, continente, pais, provincia): ").lower()
    valor = pedir_texto("Ingrese valor a buscar: ").lower()
    filtrados = mostrar_y_filtrar_recursivo(BASE_DIR, atributo, valor)
    if filtrados:
        print(f"\n{len(filtrados)} coincidencias encontradas:\n")
        for f in filtrados:
            print(f"→ {f}")
    else:
        print("No se encontraron coincidencias.")
