import os
from utilidades.funciones_utiles import crear_directorio, escribir_csv, pedir_numero, pedir_texto

BASE_DIR = "CONTINENTES"
# ===========================
# Fase 1: Creación Jerárquica
# ===========================
def crear_nivel(ruta_actual, nivel):
    nombres_niveles = {1: "continente", 2: "país", 3: "provincia", 4: "ciudad"}
    nivel_siguiente = nivel + 1
    cantidad = int(pedir_numero(f"¿Cuántos {nombres_niveles[nivel]}es desea crear en {ruta_actual}? "))
    for i in range(cantidad):
        print(f"\n=== {nombres_niveles[nivel].capitalize()} {i+1} en {ruta_actual} ===")
        nombre = pedir_texto(f"Nombre del {nombres_niveles[nivel]}: ")
        poblacion = pedir_numero(f"Población de {nombre}: ")
        superficie = pedir_numero(f"Superficie de {nombre} (km²): ")
        ruta_nueva = os.path.join(ruta_actual, nombre)
        crear_directorio(ruta_nueva)
        datos = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie}
        if nivel == 2: datos["continente"] = os.path.basename(ruta_actual)
        if nivel == 3: datos["pais"] = os.path.basename(ruta_actual)
        if nivel == 4: datos["provincia"] = os.path.basename(ruta_actual)
        nombre_csv = nombre if nivel < 4 else f"Ciudades_{nombre}.csv"
        escribir_csv(os.path.join(ruta_nueva, f"{nombre_csv}.csv"),
                    datos if nivel < 4 else [datos],
                    ["nombre", "poblacion", "superficie"] + (["continente"] if nivel==2 else ["pais"] if nivel==3 else ["provincia"] if nivel==4 else []))
        if nivel < 4:
            crear_nivel(ruta_nueva, nivel_siguiente)
